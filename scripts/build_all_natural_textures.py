import os
import random
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageEnhance

OUT_DIR = "assets/costumes"
os.makedirs(OUT_DIR, exist_ok=True)

tops_default = Image.open(f"{OUT_DIR}/tops_default.png").convert("RGBA")
bottoms_default = Image.open(f"{OUT_DIR}/bottoms_default.png").convert("RGBA")

tops_alpha = tops_default.split()[3]
bottoms_alpha = bottoms_default.split()[3]

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

def apply_alpha(canvas, mask):
    res = canvas.copy()
    res.putalpha(mask)
    return res

# -------------------------------------------------------------
# 1. さかなパーカー (Fish Hoodie)
# -------------------------------------------------------------
print("Processing 1. さかなパーカー...")
hoodie_src = Image.open("さかなパーカー.png").convert("RGBA")
hoodie_navy = (20, 31, 54, 255)
canvas_tops = Image.new("RGBA", (1024, 2048), hoodie_navy)

f_crop = hoodie_src.crop((440, 260, 1060, 910))
f_crop_res = f_crop.resize((540, 560), Image.Resampling.LANCZOS)
f_feathered = feather_image(f_crop_res, 18)
canvas_tops.paste(f_feathered, (242, 265), f_feathered)

s_crop = hoodie_src.crop((160, 420, 360, 680))
s_l = s_crop.resize((180, 240), Image.Resampling.LANCZOS)
s_feathered_l = feather_image(s_l, 14)
s_feathered_r = ImageOps.mirror(s_feathered_l)

canvas_tops.paste(s_feathered_l, (48, 195), s_feathered_l)
canvas_tops.paste(s_feathered_r, (796, 195), s_feathered_r)
canvas_tops.paste(s_feathered_l, (48, 1225), s_feathered_l)
canvas_tops.paste(s_feathered_r, (796, 1225), s_feathered_r)

b_crop = hoodie_src.crop((460, 270, 1040, 660)).resize((540, 460), Image.Resampling.LANCZOS)
b_feathered = feather_image(b_crop, 18)
canvas_tops.paste(b_feathered, (242, 1300), b_feathered)

apply_alpha(canvas_tops, tops_alpha).save(f"{OUT_DIR}/tops_hoodie.png")

canvas_bot = Image.new("RGBA", (1024, 1024), hoodie_navy)
b_draw = ImageDraw.Draw(canvas_bot)
b_draw.line([(240, 80), (280, 340)], fill=(14, 22, 38, 255), width=3)
b_draw.line([(784, 80), (744, 340)], fill=(14, 22, 38, 255), width=3)
b_draw.rectangle([0, 560, 1024, 617], fill=(15, 23, 40, 255))
apply_alpha(canvas_bot, bottoms_alpha).save(f"{OUT_DIR}/bottoms_hoodie.png")

# -------------------------------------------------------------
# 2. 蒼藍の袴（袴１）
# -------------------------------------------------------------
print("Processing 2. 蒼藍の袴（袴１）...")
h1_src = Image.open("袴１.png").convert("RGBA")
h1_indigo = (26, 42, 74, 255)
canvas_tops = Image.new("RGBA", (1024, 2048), h1_indigo)

h1_torso = h1_src.crop((260, 140, 820, 660)).resize((540, 560), Image.Resampling.LANCZOS)
h1_f_feather = feather_image(h1_torso, 16)
canvas_tops.paste(h1_f_feather, (242, 260), h1_f_feather)

h1_back = h1_src.crop((320, 220, 760, 640)).resize((540, 560), Image.Resampling.LANCZOS)
h1_b_feather = feather_image(h1_back, 16)
canvas_tops.paste(h1_b_feather, (242, 1260), h1_b_feather)

h1_sleeve = h1_src.crop((120, 180, 280, 360)).resize((180, 240), Image.Resampling.LANCZOS)
h1_sl = feather_image(h1_sleeve, 14)
h1_sr = ImageOps.mirror(h1_sl)
canvas_tops.paste(h1_sl, (48, 195), h1_sl)
canvas_tops.paste(h1_sr, (796, 195), h1_sr)
canvas_tops.paste(h1_sl, (48, 1225), h1_sl)
canvas_tops.paste(h1_sr, (796, 1225), h1_sr)

apply_alpha(canvas_tops, tops_alpha).save(f"{OUT_DIR}/tops_hakama1.png")

h1_pants = h1_src.crop((240, 630, 840, 1450)).resize((1024, 617), Image.Resampling.LANCZOS)
canvas_bot = Image.new("RGBA", (1024, 1024), h1_indigo)
canvas_bot.paste(h1_pants, (0, 0), h1_pants)
apply_alpha(canvas_bot, bottoms_alpha).save(f"{OUT_DIR}/bottoms_hakama1.png")

# -------------------------------------------------------------
# 3. 墨炭の袴（袴２）
# -------------------------------------------------------------
print("Processing 3. 墨炭の袴（袴２）...")
h2_src = Image.open("袴２.png").convert("RGBA")
h2_charcoal = (74, 75, 80, 255)
canvas_tops = Image.new("RGBA", (1024, 2048), h2_charcoal)

h2_torso = h2_src.crop((270, 140, 810, 660)).resize((540, 560), Image.Resampling.LANCZOS)
h2_f_feather = feather_image(h2_torso, 16)
canvas_tops.paste(h2_f_feather, (242, 260), h2_f_feather)

h2_back = h2_src.crop((320, 220, 760, 640)).resize((540, 560), Image.Resampling.LANCZOS)
h2_b_feather = feather_image(h2_back, 16)
canvas_tops.paste(h2_b_feather, (242, 1260), h2_b_feather)

h2_sleeve = h2_src.crop((120, 180, 280, 360)).resize((180, 240), Image.Resampling.LANCZOS)
h2_sl = feather_image(h2_sleeve, 14)
h2_sr = ImageOps.mirror(h2_sl)
canvas_tops.paste(h2_sl, (48, 195), h2_sl)
canvas_tops.paste(h2_sr, (796, 195), h2_sr)
canvas_tops.paste(h2_sl, (48, 1225), h2_sl)
canvas_tops.paste(h2_sr, (796, 1225), h2_sr)

apply_alpha(canvas_tops, tops_alpha).save(f"{OUT_DIR}/tops_hakama2.png")

h2_pants = h2_src.crop((240, 600, 840, 1450)).resize((1024, 617), Image.Resampling.LANCZOS)
canvas_bot = Image.new("RGBA", (1024, 1024), h2_charcoal)
canvas_bot.paste(h2_pants, (0, 0), h2_pants)
apply_alpha(canvas_bot, bottoms_alpha).save(f"{OUT_DIR}/bottoms_hakama2.png")

# -------------------------------------------------------------
# 4. シック黒Tシャツ
# -------------------------------------------------------------
print("Processing 4. シック黒Tシャツ...")
bt_src = Image.open("黒Tシャツ.png").convert("RGBA")
bt_black = (28, 28, 30, 255)
canvas_tops = Image.new("RGBA", (1024, 2048), bt_black)

bt_torso = bt_src.crop((260, 180, 820, 880)).resize((540, 560), Image.Resampling.LANCZOS)
bt_f_feather = feather_image(bt_torso, 16)
canvas_tops.paste(bt_f_feather, (242, 260), bt_f_feather)

bt_back = bt_src.crop((320, 280, 760, 800)).resize((540, 560), Image.Resampling.LANCZOS)
bt_b_feather = feather_image(bt_back, 16)
canvas_tops.paste(bt_b_feather, (242, 1260), bt_b_feather)

bt_sleeve = bt_src.crop((120, 260, 280, 440)).resize((180, 240), Image.Resampling.LANCZOS)
bt_sl = feather_image(bt_sleeve, 14)
bt_sr = ImageOps.mirror(bt_sl)
canvas_tops.paste(bt_sl, (48, 195), bt_sl)
canvas_tops.paste(bt_sr, (796, 195), bt_sr)
canvas_tops.paste(bt_sl, (48, 1225), bt_sl)
canvas_tops.paste(bt_sr, (796, 1225), bt_sr)

apply_alpha(canvas_tops, tops_alpha).save(f"{OUT_DIR}/tops_black_t.png")

canvas_bot = Image.new("RGBA", (1024, 1024), (22, 22, 24, 255))
b_draw = ImageDraw.Draw(canvas_bot)
b_draw.rectangle([0, 0, 1024, 70], fill=(28, 28, 32, 255))
b_draw.line([(0, 70), (1024, 70)], fill=(40, 40, 46, 255), width=2)
b_draw.arc([160, 40, 360, 200], start=30, end=150, fill=(38, 38, 44, 255), width=2)
b_draw.arc([664, 40, 864, 200], start=30, end=150, fill=(38, 38, 44, 255), width=2)
apply_alpha(canvas_bot, bottoms_alpha).save(f"{OUT_DIR}/bottoms_black_t.png")

# -------------------------------------------------------------
# 5. 書道師範 (Shodo)
# -------------------------------------------------------------
print("Processing 5. 書道師範...")
shodo_src = Image.open("書道.png").convert("RGBA")
shodo_white = (245, 245, 248, 255)
canvas_tops = Image.new("RGBA", (1024, 2048), shodo_white)

# Clean torso: remove brush and strap cleanly
shodo_torso = shodo_src.crop((300, 240, 780, 620)).copy()
s_draw = ImageDraw.Draw(shodo_torso)
s_draw.polygon([(340, 0), (480, 0), (480, 160), (370, 70)], fill=shodo_white)
s_draw.rectangle([390, 140, 480, 360], fill=shodo_white)
# Re-add subtle ink spray
s_draw.ellipse([420, 30, 428, 38], fill=(20, 20, 22, 220))
s_draw.ellipse([440, 50, 446, 56], fill=(20, 20, 22, 200))
s_draw.ellipse([410, 70, 415, 75], fill=(20, 20, 22, 180))
s_draw.ellipse([430, 180, 436, 186], fill=(20, 20, 22, 210))

shodo_torso_res = shodo_torso.resize((540, 560), Image.Resampling.LANCZOS)
shodo_f_feather = feather_image(shodo_torso_res, 16)
canvas_tops.paste(shodo_f_feather, (242, 260), shodo_f_feather)

shodo_back = Image.new("RGBA", (540, 560), shodo_white)
sb_draw = ImageDraw.Draw(shodo_back)
for offset_x, offset_y, r in [(270, 270, 68), (300, 235, 48), (240, 300, 42), (330, 300, 38), (220, 235, 32)]:
    sb_draw.ellipse([offset_x - r, offset_y - r, offset_x + r, offset_y + r], fill=(20, 20, 24, 255))
random.seed(42)
for _ in range(40):
    dx = random.randint(140, 410)
    dy = random.randint(140, 430)
    dr = random.randint(2, 8)
    sb_draw.ellipse([dx - dr, dy - dr, dx + dr, dy + dr], fill=(20, 20, 24, 230))

shodo_b_feather = feather_image(shodo_back, 16)
canvas_tops.paste(shodo_b_feather, (242, 1260), shodo_b_feather)

shodo_sleeve = shodo_src.crop((120, 320, 260, 460)).resize((180, 240), Image.Resampling.LANCZOS)
shodo_sl = feather_image(shodo_sleeve, 14)
shodo_sr = ImageOps.mirror(shodo_sl)
canvas_tops.paste(shodo_sl, (48, 195), shodo_sl)
canvas_tops.paste(shodo_sr, (796, 195), shodo_sr)
canvas_tops.paste(shodo_sl, (48, 1225), shodo_sl)
canvas_tops.paste(shodo_sr, (796, 1225), shodo_sr)

apply_alpha(canvas_tops, tops_alpha).save(f"{OUT_DIR}/tops_shodo.png")

shodo_pants = shodo_src.crop((240, 640, 840, 1300)).resize((1024, 617), Image.Resampling.LANCZOS)
canvas_bot = Image.new("RGBA", (1024, 1024), (32, 50, 78, 255))
canvas_bot.paste(shodo_pants, (0, 0), shodo_pants)
apply_alpha(canvas_bot, bottoms_alpha).save(f"{OUT_DIR}/bottoms_shodo.png")

# -------------------------------------------------------------
# 6. 仙人道服 (Sennin)
# -------------------------------------------------------------
print("Processing 6. 仙人道服...")
sennin_src = Image.open("仙人.png").convert("RGBA")
sennin_blue = (28, 54, 88, 255)
canvas_tops = Image.new("RGBA", (1024, 2048), sennin_blue)

sennin_torso = sennin_src.crop((280, 280, 800, 880)).resize((540, 560), Image.Resampling.LANCZOS)
sennin_f_feather = feather_image(sennin_torso, 16)
canvas_tops.paste(sennin_f_feather, (242, 260), sennin_f_feather)

sennin_back = sennin_src.crop((300, 300, 780, 650)).resize((540, 560), Image.Resampling.LANCZOS)
sennin_b_feather = feather_image(sennin_back, 16)
canvas_tops.paste(sennin_b_feather, (242, 1260), sennin_b_feather)

sennin_sleeve = sennin_src.crop((30, 300, 260, 640)).resize((180, 240), Image.Resampling.LANCZOS)
sennin_sl = feather_image(sennin_sleeve, 14)
sennin_sr = ImageOps.mirror(sennin_sl)
canvas_tops.paste(sennin_sl, (48, 195), sennin_sl)
canvas_tops.paste(sennin_sr, (796, 195), sennin_sr)
canvas_tops.paste(sennin_sl, (48, 1225), sennin_sl)
canvas_tops.paste(sennin_sr, (796, 1225), sennin_sr)

apply_alpha(canvas_tops, tops_alpha).save(f"{OUT_DIR}/tops_sennin.png")

sennin_pants = sennin_src.crop((280, 860, 800, 1400)).resize((1024, 617), Image.Resampling.LANCZOS)
canvas_bot = Image.new("RGBA", (1024, 1024), sennin_blue)
canvas_bot.paste(sennin_pants, (0, 0), sennin_pants)
apply_alpha(canvas_bot, bottoms_alpha).save(f"{OUT_DIR}/bottoms_sennin.png")

# -------------------------------------------------------------
# 7. 忍び装束 (Ninja)
# -------------------------------------------------------------
print("Processing 7. 忍び装束...")
ninja_src = Image.open("忍者.png").convert("RGBA")
ninja_navy = (28, 44, 72, 255)
canvas_tops = Image.new("RGBA", (1024, 2048), ninja_navy)

ninja_torso = ninja_src.crop((310, 280, 770, 720)).resize((540, 560), Image.Resampling.LANCZOS)
ninja_f_feather = feather_image(ninja_torso, 16)
canvas_tops.paste(ninja_f_feather, (242, 260), ninja_f_feather)

ninja_back = ninja_src.crop((340, 320, 740, 680)).resize((540, 560), Image.Resampling.LANCZOS)
ninja_b_feather = feather_image(ninja_back, 16)
canvas_tops.paste(ninja_b_feather, (242, 1260), ninja_b_feather)

ninja_sleeve = ninja_src.crop((180, 320, 320, 520)).resize((180, 240), Image.Resampling.LANCZOS)
ninja_sl = feather_image(ninja_sleeve, 14)
ninja_sr = ImageOps.mirror(ninja_sl)
canvas_tops.paste(ninja_sl, (48, 195), ninja_sl)
canvas_tops.paste(ninja_sr, (796, 195), ninja_sr)
canvas_tops.paste(ninja_sl, (48, 1225), ninja_sl)
canvas_tops.paste(ninja_sr, (796, 1225), ninja_sr)

apply_alpha(canvas_tops, tops_alpha).save(f"{OUT_DIR}/tops_ninja.png")

ninja_pants = ninja_src.crop((280, 740, 800, 1360)).resize((1024, 617), Image.Resampling.LANCZOS)
canvas_bot = Image.new("RGBA", (1024, 1024), (26, 40, 66, 255))
canvas_bot.paste(ninja_pants, (0, 0), ninja_pants)
apply_alpha(canvas_bot, bottoms_alpha).save(f"{OUT_DIR}/bottoms_ninja.png")

# -------------------------------------------------------------
# 8. 名誉武士甲冑 (Samurai)
# -------------------------------------------------------------
print("Processing 8. 名誉武士甲冑...")
samurai_src = Image.open("武士.png").convert("RGBA")
samurai_navy = (24, 34, 52, 255)
canvas_tops = Image.new("RGBA", (1024, 2048), samurai_navy)

samurai_torso = samurai_src.crop((320, 520, 760, 880)).resize((540, 560), Image.Resampling.LANCZOS)
samurai_f_feather = feather_image(samurai_torso, 16)
canvas_tops.paste(samurai_f_feather, (242, 260), samurai_f_feather)

samurai_back = samurai_src.crop((340, 520, 740, 860)).resize((540, 560), Image.Resampling.LANCZOS)
samurai_b_feather = feather_image(samurai_back, 16)
canvas_tops.paste(samurai_b_feather, (242, 1260), samurai_b_feather)

samurai_sleeve = samurai_src.crop((160, 520, 280, 720)).resize((180, 240), Image.Resampling.LANCZOS)
samurai_sl = feather_image(samurai_sleeve, 14)
samurai_sr = ImageOps.mirror(samurai_sl)
canvas_tops.paste(samurai_sl, (48, 195), samurai_sl)
canvas_tops.paste(samurai_sr, (796, 195), samurai_sr)
canvas_tops.paste(samurai_sl, (48, 1225), samurai_sl)
canvas_tops.paste(samurai_sr, (796, 1225), samurai_sr)

apply_alpha(canvas_tops, tops_alpha).save(f"{OUT_DIR}/tops_samurai.png")

samurai_pants = samurai_src.crop((290, 760, 790, 1260)).resize((1024, 617), Image.Resampling.LANCZOS)
canvas_bot = Image.new("RGBA", (1024, 1024), (22, 22, 26, 255))
canvas_bot.paste(samurai_pants, (0, 0), samurai_pants)
apply_alpha(canvas_bot, bottoms_alpha).save(f"{OUT_DIR}/bottoms_samurai.png")

print("All 8 textures rebuilt perfectly!")
