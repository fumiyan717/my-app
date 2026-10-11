import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps
from scipy.ndimage import gaussian_filter, binary_fill_holes

OUT_DIR = "assets/costumes"
os.makedirs(OUT_DIR, exist_ok=True)

img_3d = Image.open("さかなパーカー３D.jpg").convert("RGB")
arr_3d = np.array(img_3d)

# 1. Save pristine Sample Texture Maps
diff_map = img_3d.crop((2315, 240, 2650, 575)) # 335x335
norm_map = img_3d.crop((2315, 656, 2650, 991)) # 335x335
rough_map = img_3d.crop((2315, 1060, 2650, 1395)) # 335x335

diff_map.save(f"{OUT_DIR}/diffuse_hoodie_pattern.png")
norm_map.save(f"{OUT_DIR}/normal_hoodie_pattern.png")
rough_map.save(f"{OUT_DIR}/roughness_hoodie_pattern.png")

# Also save normal map resized for VRM tops
norm_tops = Image.new("RGBA", (1024, 2048), (128, 128, 255, 255))
norm_tile = norm_map.resize((256, 256), Image.Resampling.LANCZOS)
for tx in range(0, 1024, 256):
    for ty in range(0, 2048, 256):
        norm_tops.paste(norm_tile, (tx, ty))
norm_tops.save(f"{OUT_DIR}/normal_hoodie.png")

# 2. Extract and Clean FRONT Torso from 3D model
front_raw = Image.open('assets/front_line_gone.png').convert('RGB')
arr_f = np.array(front_raw)
cx_f = 234

# Inpaint BR indicator on front hem
for y in range(470, arr_f.shape[0]):
    for x in range(340, arr_f.shape[1]):
        d_c = (x - 363)**2 + (y - 485)**2
        d_l = abs((y - 485) - (x - 363)) / np.sqrt(2)
        if d_c <= 220 or (d_l <= 5.0 and x >= 360 and y >= 480):
            mx = int(cx_f - (x - cx_f))
            if 0 <= mx < arr_f.shape[1]:
                arr_f[y, x] = arr_f[y, mx]

# Also clear the indicator line near right cuff (outside torso, x > 430)
for y in range(350, 480):
    for x in range(430, arr_f.shape[1]):
        arr_f[y, x] = arr_f[y, 400]

front_clean = Image.fromarray(arr_f)
front_clean.save('assets/front_clean_final.png')

# 3. Extract and Clean BACK Torso from 3D model
back_raw = Image.open('assets/back_circles_flawless.png').convert('RGB')
arr_b = np.array(back_raw)
cx_b = 250

# Inpaint last hem circle at (128, 496)
for y in range(480, 520):
    for x in range(112, 145):
        if (x - 128)**2 + (y - 496)**2 <= 180:
            mx = int(cx_b + (cx_b - x))
            if 0 <= mx < arr_b.shape[1]:
                arr_b[y, x] = arr_b[y, mx]

# Inpaint any remaining pointer lines outside (x < 70 or x > 430)
for y in range(450, 550):
    for x in range(0, 75):
        arr_b[y, x] = arr_b[y, 90]
    for x in range(425, arr_b.shape[1]):
        arr_b[y, x] = arr_b[y, 400]

back_clean = Image.fromarray(arr_b)
back_clean.save('assets/back_clean_final.png')

# 4. Extract front and back torso bounding boxes
# In front_clean (size 460 x 550):
# Torso is centered around cx_f = 234.
# Width ~ 320 (x: 74 to 394). Height ~ 440 (y: 100 to 540)
# (y=100 is below the chin/neck opening)
torso_f = front_clean.crop((74, 95, 394, 535)).resize((540, 560), Image.Resampling.LANCZOS)

# In back_clean (size 460 x 550):
# Torso is centered around cx_b = 250.
# Width ~ 320 (x: 90 to 410). Height ~ 440 (y: 95 to 535)
torso_b = back_clean.crop((90, 95, 410, 535)).resize((540, 560), Image.Resampling.LANCZOS)

# 5. Extract Sleeve from 3D model
# In front_clean, left sleeve (character's right arm) is x: 10..120, y: 110..470
sleeve_src = front_clean.crop((10, 110, 120, 470)).resize((180, 240), Image.Resampling.LANCZOS)

# Feathering function
def feather_image(img, radius=16):
    w, h = img.size
    mask = Image.new("L", (w, h), 255)
    draw = ImageDraw.Draw(mask)
    for i in range(radius):
        val = int(255 * (i / radius))
        draw.rectangle([i, i, w - 1 - i, h - 1 - i], outline=val)
    mask = mask.filter(ImageFilter.GaussianBlur(radius // 3))
    orig_a = img.split()[3] if len(img.split()) == 4 else Image.new("L", (w, h), 255)
    final_a = Image.composite(orig_a, Image.new("L", (w, h), 0), mask)
    res = img.copy().convert("RGBA")
    res.putalpha(final_a)
    return res

# 6. Compose TOPS texture
tops_default = Image.open(f"{OUT_DIR}/tops_default.png").convert("RGBA")
tops_alpha = tops_default.split()[3]
hoodie_navy = (24, 36, 60, 255)

canvas_tops = Image.new("RGBA", (1024, 2048), hoodie_navy)

# Tile diffuse fish pattern as base fabric
tile = diff_map.resize((256, 256), Image.Resampling.LANCZOS)
for tx in range(0, 1024, 256):
    for ty in range(0, 2048, 256):
        canvas_tops.paste(tile, (tx, ty))

# Paste front and back torso
f_feather = feather_image(torso_f, 16)
b_feather = feather_image(torso_b, 16)
canvas_tops.paste(f_feather, (242, 260), f_feather)
canvas_tops.paste(b_feather, (242, 1260), b_feather)

# Paste sleeves
sl_feather = feather_image(sleeve_src, 14)
sr_feather = ImageOps.mirror(sl_feather)
canvas_tops.paste(sl_feather, (48, 195), sl_feather)
canvas_tops.paste(sr_feather, (796, 195), sr_feather)
canvas_tops.paste(sl_feather, (48, 1225), sl_feather)
canvas_tops.paste(sr_feather, (796, 1225), sr_feather)

# Apply VRM alpha mask
res_tops = canvas_tops.copy()
res_tops.putalpha(tops_alpha)
res_tops.save(f"{OUT_DIR}/tops_hoodie.png")
print("Generated assets/costumes/tops_hoodie.png")

# 7. Compose BOTTOMS texture (Navy shorts with double white sporty piping)
bottoms_default = Image.open(f"{OUT_DIR}/bottoms_default.png").convert("RGBA")
bottoms_alpha = bottoms_default.split()[3]

canvas_bot = Image.new("RGBA", (1024, 1024), hoodie_navy)
b_draw = ImageDraw.Draw(canvas_bot)

# Sporty double white piping at bottom hem:
# Bottom hem of shorts in VRM is around y = 560..617
b_draw.rectangle([0, 560, 1024, 617], fill=(245, 248, 255, 255))
b_draw.rectangle([0, 576, 1024, 588], fill=hoodie_navy)
b_draw.rectangle([0, 550, 1024, 560], fill=(14, 20, 36, 255)) # hem shadow

# Front seams & fly
b_draw.line([(240, 80), (280, 420)], fill=(14, 22, 38, 255), width=3)
b_draw.line([(784, 80), (744, 420)], fill=(14, 22, 38, 255), width=3)
b_draw.line([(512, 0), (512, 450)], fill=(12, 18, 32, 255), width=4)

# Side white piping along lateral seams
b_draw.rectangle([0, 0, 18, 560], fill=(245, 248, 255, 255))
b_draw.rectangle([1006, 0, 1024, 560], fill=(245, 248, 255, 255))

res_bot = canvas_bot.copy()
res_bot.putalpha(bottoms_alpha)
res_bot.save(f"{OUT_DIR}/bottoms_hoodie.png")
print("Generated assets/costumes/bottoms_hoodie.png")

# 8. Generate 3D Fish Hoodie Icon (256x256 transparent PNG)
# Using front view of the hoodie from 3D model
hoodie_icon_src = front_clean.crop((50, 70, 420, 540)).copy()
# Remove background
arr_icon = np.array(hoodie_icon_src)
bg_icon = (arr_icon.mean(axis=2) > 195) & (arr_icon[:, :, 2] > 185)
# Skin (face/chin)
skin_icon = (arr_icon[:, :, 0] > 200) & (arr_icon[:, :, 1] > 160) & (arr_icon[:, :, 2] > 150) & (arr_icon[:, :, 0] > arr_icon[:, :, 2])
invalid_icon = bg_icon | skin_icon

alpha_icon = np.ones((arr_icon.shape[0], arr_icon.shape[1]), dtype=np.float32)
alpha_icon[invalid_icon] = 0.0
alpha_icon = binary_fill_holes(alpha_icon > 0.5).astype(np.float32)
alpha_icon_smooth = gaussian_filter(alpha_icon, sigma=1.0)

icon_rgba = np.zeros((arr_icon.shape[0], arr_icon.shape[1], 4), dtype=np.uint8)
icon_rgba[:, :, :3] = arr_icon
icon_rgba[:, :, 3] = (alpha_icon_smooth * 255).astype(np.uint8)

icon_hoodie_img = Image.fromarray(icon_rgba)
# Crop to bbox
bbox = icon_hoodie_img.getbbox()
if bbox:
    icon_cropped = icon_hoodie_img.crop(bbox)
else:
    icon_cropped = icon_hoodie_img

# Resize to fit 230x230
iw, ih = icon_cropped.size
scale = min(230 / iw, 230 / ih)
nw, nh = int(iw * scale), int(ih * scale)
icon_resized = icon_cropped.resize((nw, nh), Image.Resampling.LANCZOS)

final_icon = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
px = (256 - nw) // 2
py = (256 - nh) // 2
final_icon.paste(icon_resized, (px, py), icon_resized)
final_icon.save(f"{OUT_DIR}/icon_hoodie.png")
print("Generated assets/costumes/icon_hoodie.png")

# Also save 3D hood texture for Three.js 3D accessory
diff_map.resize((512, 512), Image.Resampling.LANCZOS).save(f"{OUT_DIR}/hood_pattern.png")
print("Generated assets/costumes/hood_pattern.png")
