import numpy as np
from PIL import Image

tops = Image.open('assets/costumes/tops_hoodie.png')
arr = np.array(tops)

# In tops (1024x2048):
# Front torso is at x: 242..782, y: 260..820.
# The collar / neck area is around y: 240..310, x: 470..550.
# Let's check for any skin pixels:
# Skin is: R > 190, G > 140, B > 130, R > B + 20
skin_count = 0
for y in range(240, 320):
    for x in range(460, 560):
        p = arr[y, x]
        if int(p[0]) > 180 and int(p[1]) > 135 and int(p[2]) > 125 and int(p[0]) > int(p[2]) + 15:
            arr[y, x, :3] = [20, 30, 54]
            skin_count += 1

print(f'Replaced {skin_count} skin pixels with deep navy in collar')
Image.fromarray(arr).save('assets/costumes/tops_hoodie.png')
