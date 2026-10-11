import numpy as np
from PIL import Image

# Load front with lines removed
front = Image.open('assets/front_line_gone.png').convert('RGBA')
arr = np.array(front)
H, W, _ = arr.shape
cx = 234

# Inpaint BR hem circle at (363, 485)
for y in range(460, H):
    for x in range(330, W):
        d_c = (x - 363)**2 + (y - 485)**2
        d_l = abs((y - 485) - (x - 363)) / np.sqrt(2)
        if d_c <= 220 or (d_l <= 5.0 and x >= 355 and y >= 475):
            mx = int(cx - (x - cx))
            if 0 <= mx < W:
                arr[y, x, :3] = arr[y, mx, :3]

# Fill neck opening with navy interior lining
# In patch_hood_rim, V neck dips to y = 125 at x = 234
for y in range(65, 130):
    for x in range(180, 290):
        # if skin
        p = arr[y, x]
        if p[0] > 180 and p[1] > 140 and p[2] > 130 and p[0] > p[2]:
            arr[y, x] = [18, 26, 44, 255]

# Inpaint hair strands over the hood fabric (x in 155..185 and 280..315, y in 65..125)
for y in range(65, 125):
    for x in range(155, 185):
        p = arr[y, x]
        # hair is brown [70..140, 50..100, 40..80]
        if p[0] > 60 and p[0] < 140 and p[1] > 40 and p[1] < 100 and p[2] < 90:
            arr[y, x] = arr[y, x - 25]
    for x in range(280, 315):
        p = arr[y, x]
        if p[0] > 60 and p[0] < 140 and p[1] > 40 and p[1] < 100 and p[2] < 90:
            arr[y, x] = arr[y, x + 25]

# Completely wipe anything above the hood rim (y < 65)
arr[:65, :, 3] = 0

# Wipe any lines above y < 90 on the right (x > 310)
for y in range(65, 90):
    for x in range(310, W):
        arr[y, x, 3] = 0

# Wipe anything above the chin in the center (y < 95, x in 185..280)
for y in range(65, 95):
    for x in range(185, 280):
        arr[y, x, 3] = 0

# Cut hands below cuffs:
for y in range(435, H):
    for x in range(0, 68):
        arr[y, x, 3] = 0
    for x in range(398, W):
        arr[y, x, 3] = 0

# Cut below hem:
for y in range(474, H):
    for x in range(0, W):
        arr[y, x, 3] = 0

# Clear text on left (x < 18) and lines on right (x > 430)
for y in range(0, H):
    for x in range(0, 18):
        arr[y, x, 3] = 0
    for x in range(430, W):
        arr[y, x, 3] = 0

# Wipe background
bg = (arr[:, :, 0] > 195) & (arr[:, :, 1] > 200) & (arr[:, :, 2] > 210)
arr[bg, 3] = 0

img_clean = Image.fromarray(arr)
bbox = img_clean.getbbox()
cropped = img_clean.crop(bbox)

cw, ch = cropped.size
scale = min(230 / cw, 230 / ch)
nw, nh = int(cw * scale), int(ch * scale)
resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)

icon = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
px = (256 - nw) // 2
py = (256 - nh) // 2
icon.paste(resized, (px, py), resized)
icon.save('assets/costumes/icon_hoodie.png')
print('Saved assets/costumes/icon_hoodie.png')
