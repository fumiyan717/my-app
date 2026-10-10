import os
import gzip
import json
import urllib.request
import xml.etree.ElementTree as ET
import numpy as np
from svgpathtools import parse_path

WORKSPACE_DIR = '/workspaces/my-app'
SCRATCH_DIR = '/home/codespace/.gemini/antigravity-cli/brain/f63295f9-cf57-496e-868b-4b38220033a0/scratch'
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, 'data', 'kanjivg')

KANJIVG_URL = 'https://github.com/KanjiVG/kanjivg/releases/download/r20260714/kanjivg-20260714.xml.gz'
LOCAL_XML_GZ = os.path.join(SCRATCH_DIR, 'kanjivg.xml.gz')

def get_kanji_list():
    kanji_data_path = os.path.join(WORKSPACE_DIR, 'kanji-data.js')
    with open(kanji_data_path, 'r', encoding='utf-8') as f:
        text = f.read()
    start = text.find('{')
    end = text.rfind('}') + 1
    data = json.loads(text[start:end])
    return list(data.keys())

def download_kanjivg():
    os.makedirs(SCRATCH_DIR, exist_ok=True)
    if not os.path.exists(LOCAL_XML_GZ):
        print('Downloading KanjiVG XML database...')
        urllib.request.urlretrieve(KANJIVG_URL, LOCAL_XML_GZ)
        print('Download completed.')
    else:
        print('Using cached KanjiVG XML database.')

def convert_kanji_element(char, kanji_el):
    path_elems = [el for el in kanji_el.iter() if el.tag.endswith('path') and 'd' in el.attrib]
    total_strokes = len(path_elems)
    if total_strokes == 0:
        return None

    scale = 8.0
    x_center = 512.0
    y_center = 388.0

    # Adjust stroke thickness based on stroke count
    if total_strokes <= 5:
        hw = 25.0
    elif total_strokes <= 10:
        hw = 23.0
    elif total_strokes <= 15:
        hw = 21.0
    else:
        hw = 19.0

    def to_hw(x, y):
        hx = x_center + (x - 54.5) * scale
        hy = y_center - (y - 54.5) * scale
        return hx, hy

    strokes = []
    medians = []

    for el in path_elems:
        d = el.attrib['d']
        try:
            path = parse_path(d)
        except Exception as e:
            print(f'Error parsing path for {char}: {e}')
            continue

        length = path.length()
        if length <= 0.001:
            continue

        # Sampling points: about 1 sample per 1.2 units in KanjiVG coords
        num_samples = max(14, int(length / 1.1))
        ts = np.linspace(0, 1, num_samples)

        raw_pts = [path.point(t) for t in ts]
        hw_pts = [to_hw(pt.real, pt.imag) for pt in raw_pts]

        # Subsample for medians (5 to 12 points)
        num_median_pts = min(12, max(4, num_samples // 3))
        sub_indices = np.linspace(0, num_samples - 1, num_median_pts, dtype=int)
        median = [[round(hw_pts[idx][0]), round(hw_pts[idx][1])] for idx in sub_indices]

        # Deduplicate consecutive points
        clean_median = [median[0]]
        for pt in median[1:]:
            if pt != clean_median[-1]:
                clean_median.append(pt)
        medians.append(clean_median)

        # High resolution contour generation for strokes
        pts_hw = np.array(hw_pts)
        diffs = np.diff(pts_hw, axis=0)
        tangents = np.zeros_like(pts_hw)
        tangents[0] = diffs[0]
        tangents[-1] = diffs[-1]
        for k in range(1, len(pts_hw) - 1):
            tangents[k] = (diffs[k-1] + diffs[k]) / 2.0

        norms = np.linalg.norm(tangents, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        unit_tangents = tangents / norms
        unit_normals = np.stack([-unit_tangents[:, 1], unit_tangents[:, 0]], axis=1)

        left_pts = pts_hw + unit_normals * hw
        right_pts = pts_hw - unit_normals * hw

        # Start and end caps
        start_pt = pts_hw[0]
        start_tang = -unit_tangents[0]
        start_tip = start_pt + start_tang * hw

        end_pt = pts_hw[-1]
        end_tang = unit_tangents[-1]
        end_tip = end_pt + end_tang * hw

        # Assemble closed path string
        parts = [f'M {round(left_pts[0][0])},{round(left_pts[0][1])}']
        for k in range(1, len(left_pts)):
            parts.append(f'L {round(left_pts[k][0])},{round(left_pts[k][1])}')
        parts.append(f'Q {round(end_tip[0])},{round(end_tip[1])} {round(right_pts[-1][0])},{round(right_pts[-1][1])}')
        for k in range(len(right_pts) - 2, -1, -1):
            parts.append(f'L {round(right_pts[k][0])},{round(right_pts[k][1])}')
        parts.append(f'Q {round(start_tip[0])},{round(start_tip[1])} {round(left_pts[0][0])},{round(left_pts[0][1])}')
        parts.append('Z')

        strokes.append(' '.join(parts))

    return {'character': char, 'strokes': strokes, 'medians': medians}

def main():
    kanji_list = get_kanji_list()
    print(f'Total kanji to process: {len(kanji_list)}')
    
    download_kanjivg()
    
    print('Parsing KanjiVG XML database (streaming)...')
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Map kanji ID to character
    target_ids = {f'kvg:kanji_{ord(c):05x}': c for c in kanji_list}
    found_chars = {}
    
    with gzip.open(LOCAL_XML_GZ, 'rb') as gz:
        context = ET.iterparse(gz, events=('end',))
        for event, elem in context:
            if elem.tag == 'kanji':
                kanji_id = elem.attrib.get('id')
                if kanji_id in target_ids:
                    char = target_ids[kanji_id]
                    char_data = convert_kanji_element(char, elem)
                    if char_data:
                        found_chars[char] = char_data
                        
                        # Save by hex code and by char name
                        code = f'{ord(char):05x}'
                        json_str = json.dumps(char_data, ensure_ascii=False)
                        
                        with open(os.path.join(OUTPUT_DIR, f'{code}.json'), 'w', encoding='utf-8') as f:
                            f.write(json_str)
                        with open(os.path.join(OUTPUT_DIR, f'{char}.json'), 'w', encoding='utf-8') as f:
                            f.write(json_str)
                            
                elem.clear()

    print(f'Processed {len(found_chars)} / {len(kanji_list)} kanji.')
    missing = set(kanji_list) - set(found_chars.keys())
    if missing:
        print(f'Missing kanji ({len(missing)}): {missing}')
    else:
        print('All 1,026 elementary kanji successfully converted!')

    # Also build a single bundle kanjivg-data.js for fast initial lookup
    bundle_path = os.path.join(WORKSPACE_DIR, 'kanjivg-data.js')
    print(f'Writing bundled file to {bundle_path}...')
    with open(bundle_path, 'w', encoding='utf-8') as f:
        f.write('window.KANJIVG_DATA = ')
        json.dump(found_chars, f, ensure_ascii=False)
        f.write(';\n')
    print('Done!')

if __name__ == '__main__':
    main()
