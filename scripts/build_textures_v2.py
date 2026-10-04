import os
from PIL import Image, ImageOps, ImageFilter

os.makedirs('assets/costumes', exist_ok=True)

base_tops = Image.open('dump_men_textures/12__12.png').convert('RGBA')
base_bottoms = Image.open('dump_men_textures/18__17.png').convert('RGBA')
tops_mask = base_tops.split()[3]
bottoms_mask = base_bottoms.split()[3]
TW, TH = base_tops.size       # 1024, 2048
BW, BH = base_bottoms.size    # 1024, 1024

def apply_mask(img, mask):
    r, g, b, a = img.split()
    final_a = ImageOps.fit(mask, img.size)
    return Image.merge('RGBA', (r, g, b, final_a))

# 1. Hoodie (Fish Hoodie)
def build_hoodie():
    src = Image.open('さかなパーカー.png').convert('RGBA')
    bg_color = (17, 24, 48, 255)
    torso_crop = src.crop((340, 200, 1160, 1050))
    tops = Image.new('RGBA', (TW, TH), bg_color)
    front_torso = torso_crop.resize((700, 750), Image.Resampling.LANCZOS)
    tops.paste(front_torso, (162, 160), front_torso)
    back_crop = torso_crop.crop((60, 100, 760, 780)).resize((680, 720), Image.Resampling.LANCZOS)
    tops.paste(back_crop, (172, 1024 + 160), back_crop)
    lsleeve = src.crop((60, 360, 480, 780)).resize((300, 320), Image.Resampling.LANCZOS)
    rsleeve = src.crop((1020, 360, 1440, 780)).resize((300, 320), Image.Resampling.LANCZOS)
    tops.paste(lsleeve, (30, 180), lsleeve)
    tops.paste(rsleeve, (694, 180), rsleeve)
    tops.paste(lsleeve, (30, 1024 + 180), lsleeve)
    tops.paste(rsleeve, (694, 1024 + 180), rsleeve)
    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_hoodie.png')
    bottoms = Image.new('RGBA', (BW, BH), (15, 20, 40, 255))
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_hoodie.png')
    print('OK hoodie')

# 2. Hakama1 (Navy Kendo)
def build_hakama1():
    src = Image.open('袴１.png').convert('RGBA')
    jacket_crop = src.crop((120, 112, 960, 640))
    hakama_crop = src.crop((160, 640, 920, 1464))
    tops = Image.new('RGBA', (TW, TH), (24, 38, 68, 255))
    j_front = jacket_crop.resize((760, 740), Image.Resampling.LANCZOS)
    tops.paste(j_front, (132, 150), j_front)
    j_back = jacket_crop.crop((100, 100, 740, 520)).resize((720, 700), Image.Resampling.LANCZOS)
    tops.paste(j_back, (152, 1024 + 160), j_back)
    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_hakama1.png')
    bottoms = Image.new('RGBA', (BW, BH), (18, 28, 52, 255))
    h_fit = hakama_crop.resize((960, 620), Image.Resampling.LANCZOS)
    bottoms.paste(h_fit, (32, 0), h_fit)
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_hakama1.png')
    print('OK hakama1')

# 3. Hakama2 (Charcoal Modern)
def build_hakama2():
    src = Image.open('袴２.png').convert('RGBA')
    jacket_crop = src.crop((70, 123, 1010, 630))
    hakama_crop = src.crop((180, 630, 900, 1470))
    tops = Image.new('RGBA', (TW, TH), (45, 45, 50, 255))
    j_front = jacket_crop.resize((820, 740), Image.Resampling.LANCZOS)
    tops.paste(j_front, (102, 150), j_front)
    j_back = jacket_crop.crop((150, 80, 790, 500)).resize((720, 700), Image.Resampling.LANCZOS)
    tops.paste(j_back, (152, 1024 + 160), j_back)
    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_hakama2.png')
    bottoms = Image.new('RGBA', (BW, BH), (40, 40, 44, 255))
    h_fit = hakama_crop.resize((960, 620), Image.Resampling.LANCZOS)
    bottoms.paste(h_fit, (32, 0), h_fit)
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_hakama2.png')
    print('OK hakama2')

# 4. Black T-shirt
def build_black_t():
    src = Image.open('黒Tシャツ.png').convert('RGBA')
    t_crop = src.crop((34, 264, 1046, 1213))
    tops = Image.new('RGBA', (TW, TH), (20, 20, 22, 255))
    t_front = t_crop.resize((880, 780), Image.Resampling.LANCZOS)
    tops.paste(t_front, (72, 140), t_front)
    t_back = t_crop.crop((100, 150, 910, 940)).resize((780, 720), Image.Resampling.LANCZOS)
    tops.paste(t_back, (122, 1024 + 150), t_back)
    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_black_t.png')
    bottoms = Image.new('RGBA', (BW, BH), (16, 16, 18, 255))
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_black_t.png')
    print('OK black_t')

# 5. Shodo (Calligraphy Master)
def build_shodo():
    src = Image.open('書道.png').convert('RGBA')
    # Extract only the dogi shirt: y: 160 to 455, x: 20 to 980
    shirt_crop = src.crop((20, 160, 980, 455))
    # Extract calligraphy "書道" kanji specifically: y: 200 to 410, x: 380 to 570
    shodo_kanji = src.crop((380, 200, 570, 410))
    # Hakama with ink splatters: y: 450 to 860, x: 210 to 730
    hakama_crop = src.crop((210, 450, 730, 860))

    tops = Image.new('RGBA', (TW, TH), (248, 248, 250, 255))
    s_front = shirt_crop.resize((920, 700), Image.Resampling.LANCZOS)
    tops.paste(s_front, (52, 170), s_front)
    
    # Extra crisp "書道" kanji in center chest
    k_front = shodo_kanji.resize((240, 290), Image.Resampling.LANCZOS)
    tops.paste(k_front, (TW // 2 - 120, 310), k_front)
    
    # Back with ink splatters and large calligraphy
    s_back = shirt_crop.resize((880, 680), Image.Resampling.LANCZOS)
    tops.paste(s_back, (72, 1024 + 170), s_back)
    tops.paste(k_front, (TW // 2 - 120, 1024 + 310), k_front)

    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_shodo.png')

    bottoms = Image.new('RGBA', (BW, BH), (38, 55, 85, 255))
    h_fit = hakama_crop.resize((940, 620), Image.Resampling.LANCZOS)
    bottoms.paste(h_fit, (42, 0), h_fit)
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_shodo.png')
    print('OK shodo')

# 6. Sennin (Taoist Sage)
def build_sennin():
    src = Image.open('仙人.png').convert('RGBA')
    # Upper robe with Mount Fuji, cranes, pines: y: 260 to 650, x: 20 to 1060
    robe_crop = src.crop((20, 260, 1060, 650))
    # Belt with "道" Yin-Yang "仙人": y: 640 to 860, x: 180 to 900
    belt_crop = src.crop((180, 640, 900, 860))
    # Lower landscape: y: 860 to 1264, x: 260 to 710
    lower_crop = src.crop((260, 860, 710, 1264))

    tops = Image.new('RGBA', (TW, TH), (30, 50, 80, 255))
    r_front = robe_crop.resize((960, 720), Image.Resampling.LANCZOS)
    tops.paste(r_front, (32, 140), r_front)
    
    # Add the obi sash along bottom of tops
    b_front = belt_crop.resize((760, 220), Image.Resampling.LANCZOS)
    tops.paste(b_front, (TW // 2 - 380, 640), b_front)

    # Back
    r_back = robe_crop.resize((920, 700), Image.Resampling.LANCZOS)
    tops.paste(r_back, (52, 1024 + 140), r_back)
    tops.paste(b_front, (TW // 2 - 380, 1024 + 640), b_front)

    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_sennin.png')

    bottoms = Image.new('RGBA', (BW, BH), (25, 42, 70, 255))
    l_fit = lower_crop.resize((900, 620), Image.Resampling.LANCZOS)
    bottoms.paste(l_fit, (62, 0), l_fit)
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_sennin.png')
    print('OK sennin')

# 7. Ninja (Shinobi)
def build_ninja():
    src = Image.open('忍者.png').convert('RGBA')
    # Dogi with "忍": y: 350 to 850, x: 160 to 920
    dogi_crop = src.crop((160, 350, 920, 850))
    # Pants: y: 850 to 1400, x: 260 to 740
    pants_crop = src.crop((260, 850, 740, 1400))

    tops = Image.new('RGBA', (TW, TH), (28, 42, 65, 255))
    d_front = dogi_crop.resize((860, 750), Image.Resampling.LANCZOS)
    tops.paste(d_front, (82, 140), d_front)

    d_back = dogi_crop.resize((820, 720), Image.Resampling.LANCZOS)
    tops.paste(d_back, (102, 1024 + 150), d_back)

    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_ninja.png')

    bottoms = Image.new('RGBA', (BW, BH), (24, 36, 56, 255))
    p_fit = pants_crop.resize((920, 620), Image.Resampling.LANCZOS)
    bottoms.paste(p_fit, (52, 0), p_fit)
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_ninja.png')
    print('OK ninja')

# 8. Samurai
def build_samurai():
    src = Image.open('武士.png').convert('RGBA')
    # Body armor: y: 440 to 880, x: 200 to 880
    body_crop = src.crop((200, 440, 880, 880))
    # Leg armor: y: 800 to 1300, x: 250 to 830
    legs_crop = src.crop((250, 800, 830, 1300))

    tops = Image.new('RGBA', (TW, TH), (25, 25, 30, 255))
    b_front = body_crop.resize((820, 740), Image.Resampling.LANCZOS)
    tops.paste(b_front, (102, 140), b_front)

    b_back = body_crop.resize((780, 710), Image.Resampling.LANCZOS)
    tops.paste(b_back, (122, 1024 + 150), b_back)

    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_samurai.png')

    bottoms = Image.new('RGBA', (BW, BH), (22, 22, 26, 255))
    h_fit = legs_crop.resize((920, 620), Image.Resampling.LANCZOS)
    bottoms.paste(h_fit, (52, 0), h_fit)
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_samurai.png')
    print('OK samurai')

build_hoodie()
build_hakama1()
build_hakama2()
build_black_t()
build_shodo()
build_sennin()
build_ninja()
build_samurai()
