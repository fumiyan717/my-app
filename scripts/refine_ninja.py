from PIL import Image, ImageOps

base_tops = Image.open('dump_men_textures/12__12.png').convert('RGBA')
tops_mask = base_tops.split()[3]
TW, TH = base_tops.size

src = Image.open('忍者.png').convert('RGBA')
# Arm guards: x: 50 to 240, y: 460 to 600
arm_guard = src.crop((50, 460, 240, 600)).resize((260, 300), Image.Resampling.LANCZOS)

# Dogi with "忍": y: 340 to 860, x: 230 to 850
dogi_crop = src.crop((230, 340, 850, 860)).resize((720, 740), Image.Resampling.LANCZOS)

tops = Image.new('RGBA', (TW, TH), (28, 42, 65, 255))
# Front
tops.paste(arm_guard, (40, 180), arm_guard)
tops.paste(arm_guard.transpose(Image.FLIP_LEFT_RIGHT), (724, 180), arm_guard)
tops.paste(dogi_crop, (152, 140), dogi_crop)

# Back
tops.paste(arm_guard, (40, 1024 + 180), arm_guard)
tops.paste(arm_guard.transpose(Image.FLIP_LEFT_RIGHT), (724, 1024 + 180), arm_guard)
tops.paste(dogi_crop, (152, 1024 + 140), dogi_crop)

r, g, b, a = tops.split()
final_a = ImageOps.fit(tops_mask, tops.size)
tops = Image.merge('RGBA', (r, g, b, final_a))
tops.save('assets/costumes/tops_ninja.png')
print('Refined ninja tops')
