from PIL import Image, ImageOps

base_tops = Image.open('dump_men_textures/12__12.png').convert('RGBA')
tops_mask = base_tops.split()[3]
TW, TH = base_tops.size

src = Image.open('仙人.png').convert('RGBA')
# Left sleeve of kimono (cranes & clouds): x: 8 to 320, y: 380 to 720
lsleeve_crop = src.crop((8, 380, 320, 720)).resize((300, 320), Image.Resampling.LANCZOS)
# Right sleeve (Fuji & pines): x: 740 to 1040, y: 380 to 720
rsleeve_crop = src.crop((740, 380, 1040, 720)).resize((300, 320), Image.Resampling.LANCZOS)

# Torso with collar and belt
# Collar starts around y: 260
torso_crop = src.crop((240, 260, 840, 860)).resize((720, 740), Image.Resampling.LANCZOS)

tops = Image.new('RGBA', (TW, TH), (30, 50, 80, 255))
# Front
tops.paste(lsleeve_crop, (30, 180), lsleeve_crop)
tops.paste(rsleeve_crop, (694, 180), rsleeve_crop)
tops.paste(torso_crop, (152, 140), torso_crop)

# Back
tops.paste(lsleeve_crop, (30, 1024 + 180), lsleeve_crop)
tops.paste(rsleeve_crop, (694, 1024 + 180), rsleeve_crop)
tops.paste(torso_crop, (152, 1024 + 140), torso_crop)

r, g, b, a = tops.split()
final_a = ImageOps.fit(tops_mask, tops.size)
tops = Image.merge('RGBA', (r, g, b, final_a))
tops.save('assets/costumes/tops_sennin.png')
print('Refined sennin tops')
