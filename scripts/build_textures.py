import os
from PIL import Image, ImageOps, ImageFilter, ImageEnhance

os.makedirs('assets/costumes', exist_ok=True)

# Load reference masks and base templates
base_tops = Image.open('dump_men_textures/12__12.png').convert('RGBA')
base_bottoms = Image.open('dump_men_textures/18__17.png').convert('RGBA')

tops_mask = base_tops.split()[3]
bottoms_mask = base_bottoms.split()[3]

TW, TH = base_tops.size       # 1024, 2048
BW, BH = base_bottoms.size    # 1024, 1024

# Save default textures
base_tops.save('assets/costumes/tops_default.png')
base_bottoms.save('assets/costumes/bottoms_default.png')
print('Saved default textures')

def apply_mask(img, mask):
    # Ensure alpha outside mask is 0, inside mask follows mask
    r, g, b, a = img.split()
    final_a = ImageOps.fit(mask, img.size)
    return Image.merge('RGBA', (r, g, b, final_a))

# ==========================================================
# 1. さかなパーカー (Fish Hoodie)
# ==========================================================
def build_hoodie():
    src = Image.open('さかなパーカー.png').convert('RGBA')
    # Background color: deep navy
    bg_color = (17, 24, 48, 255)
    
    # Crop front torso of hoodie (approx center body with "魚" and pocket)
    # src is 1500 x 1080
    torso_crop = src.crop((340, 200, 1160, 1050)) # w=820, h=850
    
    tops = Image.new('RGBA', (TW, TH), bg_color)
    
    # Fit torso_crop to front (TW=1024, TH/2=1024)
    # Front torso area is around x: 180 to 844, y: 150 to 900
    front_torso = torso_crop.resize((700, 750), Image.Resampling.LANCZOS)
    tops.paste(front_torso, (162, 160), front_torso)
    
    # For back (y: 1024 to 2048), paste a flipped/varied crop to give continuous fish kanji
    back_crop = torso_crop.crop((60, 100, 760, 780)).resize((680, 720), Image.Resampling.LANCZOS)
    tops.paste(back_crop, (172, 1024 + 160), back_crop)
    
    # Sleeves: crop left sleeve and right sleeve
    lsleeve = src.crop((60, 360, 480, 780)).resize((300, 320), Image.Resampling.LANCZOS)
    rsleeve = src.crop((1020, 360, 1440, 780)).resize((300, 320), Image.Resampling.LANCZOS)
    
    # Paste to front sleeves
    tops.paste(lsleeve, (30, 180), lsleeve)
    tops.paste(rsleeve, (694, 180), rsleeve)
    # Paste to back sleeves
    tops.paste(lsleeve, (30, 1024 + 180), lsleeve)
    tops.paste(rsleeve, (694, 1024 + 180), rsleeve)
    
    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_hoodie.png')
    
    # Bottoms: deep navy relaxed joggers
    bottoms = Image.new('RGBA', (BW, BH), (15, 20, 40, 255))
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_hoodie.png')
    print('Built hoodie')

build_hoodie()

# ==========================================================
# 2. 袴１ (Hakama 1 - Navy Kendo)
# ==========================================================
def build_hakama1():
    src = Image.open('袴１.png').convert('RGBA')
    # src is 1080 x 1500
    # Upper jacket: y: 112 to 620
    jacket_crop = src.crop((120, 112, 960, 640))
    # Pleated hakama: y: 640 to 1464
    hakama_crop = src.crop((160, 640, 920, 1464))
    
    # Tops
    tops = Image.new('RGBA', (TW, TH), (24, 38, 68, 255))
    j_front = jacket_crop.resize((760, 740), Image.Resampling.LANCZOS)
    tops.paste(j_front, (132, 150), j_front)
    
    # Back of jacket
    j_back = jacket_crop.crop((100, 100, 740, 520)).resize((720, 700), Image.Resampling.LANCZOS)
    tops.paste(j_back, (152, 1024 + 160), j_back)
    
    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_hakama1.png')
    
    # Bottoms (pleated hakama)
    bottoms = Image.new('RGBA', (BW, BH), (18, 28, 52, 255))
    h_fit = hakama_crop.resize((960, 620), Image.Resampling.LANCZOS)
    bottoms.paste(h_fit, (32, 0), h_fit)
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_hakama1.png')
    print('Built hakama1')

build_hakama1()

# ==========================================================
# 3. 袴２ (Hakama 2 - Charcoal Hakama)
# ==========================================================
def build_hakama2():
    src = Image.open('袴２.png').convert('RGBA')
    # Upper: y: 123 to 630
    jacket_crop = src.crop((70, 123, 1010, 630))
    # Hakama: y: 630 to 1470
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
    print('Built hakama2')

build_hakama2()

# ==========================================================
# 4. 黒Tシャツ (Black T-shirt)
# ==========================================================
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
    print('Built black_t')

build_black_t()

# ==========================================================
# 5. 書道 (Calligraphy Master)
# ==========================================================
def build_shodo():
    src = Image.open('書道.png').convert('RGBA')
    # Shirt with '書道' and ink splatters: y: 150 to 520, x: 20 to 1000
    shirt_crop = src.crop((20, 150, 980, 520))
    # Hakama with ink splatters: y: 450 to 860, x: 210 to 730
    hakama_crop = src.crop((210, 450, 730, 860))
    
    tops = Image.new('RGBA', (TW, TH), (245, 245, 248, 255))
    s_front = shirt_crop.resize((920, 740), Image.Resampling.LANCZOS)
    tops.paste(s_front, (52, 140), s_front)
    
    # Back with big calligraphy aesthetic
    s_back = shirt_crop.resize((880, 720), Image.Resampling.LANCZOS)
    tops.paste(s_back, (72, 1024 + 150), s_back)
    
    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_shodo.png')
    
    bottoms = Image.new('RGBA', (BW, BH), (38, 55, 85, 255))
    h_fit = hakama_crop.resize((940, 620), Image.Resampling.LANCZOS)
    bottoms.paste(h_fit, (42, 0), h_fit)
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_shodo.png')
    print('Built shodo')

build_shodo()

# ==========================================================
# 6. 仙人 (Taoist Sage)
# ==========================================================
def build_sennin():
    src = Image.open('仙人.png').convert('RGBA')
    # Upper landscape robe: y: 383 to 850
    upper_crop = src.crop((8, 383, 1040, 850))
    # Lower landscape skirt: y: 700 to 1264
    lower_crop = src.crop((260, 700, 710, 1264))
    
    tops = Image.new('RGBA', (TW, TH), (30, 50, 80, 255))
    u_front = upper_crop.resize((960, 760), Image.Resampling.LANCZOS)
    tops.paste(u_front, (32, 130), u_front)
    
    u_back = upper_crop.resize((920, 730), Image.Resampling.LANCZOS)
    tops.paste(u_back, (52, 1024 + 150), u_back)
    
    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_sennin.png')
    
    bottoms = Image.new('RGBA', (BW, BH), (25, 42, 70, 255))
    l_fit = lower_crop.resize((900, 620), Image.Resampling.LANCZOS)
    bottoms.paste(l_fit, (62, 0), l_fit)
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_sennin.png')
    print('Built sennin')

build_sennin()

# ==========================================================
# 7. 忍者 (Ninja)
# ==========================================================
def build_ninja():
    src = Image.open('忍者.png').convert('RGBA')
    # Shinobi dogi with '忍' crest: y: 180 to 650, x: 160 to 920
    jacket_crop = src.crop((160, 180, 920, 650))
    # Shinobi pants: y: 550 to 1100, x: 260 to 740
    pants_crop = src.crop((260, 550, 740, 1100))
    
    tops = Image.new('RGBA', (TW, TH), (28, 42, 65, 255))
    j_front = jacket_crop.resize((860, 750), Image.Resampling.LANCZOS)
    tops.paste(j_front, (82, 140), j_front)
    
    j_back = jacket_crop.resize((820, 720), Image.Resampling.LANCZOS)
    tops.paste(j_back, (102, 1024 + 150), j_back)
    
    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_ninja.png')
    
    bottoms = Image.new('RGBA', (BW, BH), (24, 36, 56, 255))
    p_fit = pants_crop.resize((920, 620), Image.Resampling.LANCZOS)
    bottoms.paste(p_fit, (52, 0), p_fit)
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_ninja.png')
    print('Built ninja')

build_ninja()

# ==========================================================
# 8. 武士 (Samurai)
# ==========================================================
def build_samurai():
    src = Image.open('武士.png').convert('RGBA')
    # Torso armor (Dou) with red cords: y: 310 to 690, x: 210 to 820
    dou_crop = src.crop((210, 310, 820, 690))
    # Thigh plates (Haidate / Kusazuri): y: 650 to 1100, x: 280 to 760
    haidate_crop = src.crop((280, 650, 760, 1100))
    
    tops = Image.new('RGBA', (TW, TH), (25, 25, 30, 255))
    d_front = dou_crop.resize((800, 740), Image.Resampling.LANCZOS)
    tops.paste(d_front, (112, 140), d_front)
    
    d_back = dou_crop.resize((760, 710), Image.Resampling.LANCZOS)
    tops.paste(d_back, (132, 1024 + 150), d_back)
    
    tops = apply_mask(tops, tops_mask)
    tops.save('assets/costumes/tops_samurai.png')
    
    bottoms = Image.new('RGBA', (BW, BH), (22, 22, 26, 255))
    h_fit = haidate_crop.resize((920, 620), Image.Resampling.LANCZOS)
    bottoms.paste(h_fit, (52, 0), h_fit)
    bottoms = apply_mask(bottoms, bottoms_mask)
    bottoms.save('assets/costumes/bottoms_samurai.png')
    print('Built samurai')

build_samurai()
