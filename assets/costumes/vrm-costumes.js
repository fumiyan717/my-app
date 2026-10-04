/**
 * 👘 VRM 3D きせかえ・モデリングシステム (Kanji Jet Pilot Outfits)
 * 8大コスチューム（さかなパーカー, 袴１, 袴２, 黒Tシャツ, 書道, 仙人, 忍者, 武士）の
 * リアルタイムテクスチャ展開＆VRMボーン追従プロシージャル3Dアクセサリ
 */

// 🐱 ネコ用きせかえマスターデータ
export const CAT_COSTUMES_DATA = {
  outfit: [
    {
      id: 'default',
      name: '標準フライトスーツ',
      iconImg: 'assets/costumes/icon_default.png',
      icon: '🐱',
      desc: '清潔感のある白Tシャツと黒スラックスの標準パイロットスーツ',
      topsTex: 'assets/costumes/tops_default.png',
      bottomsTex: 'assets/costumes/bottoms_default.png'
    },
    {
      id: 'hoodie',
      name: 'さかなパーカー',
      iconImg: 'assets/costumes/icon_hoodie.png',
      icon: '🐟',
      desc: '「魚」字と海の漢字が躍るディープネイビーの3Dフード＆白コード付きパーカー',
      topsTex: 'assets/costumes/tops_hoodie.png',
      bottomsTex: 'assets/costumes/bottoms_hoodie.png'
    },
    {
      id: 'hakama1',
      name: '蒼藍の袴（袴１）',
      iconImg: 'assets/costumes/icon_hakama1.png',
      icon: '🥋',
      desc: '伝統の刺し子藍染道着と折り目美しい蒼藍の剣道袴＆3D前紐結び',
      topsTex: 'assets/costumes/tops_hakama1.png',
      bottomsTex: 'assets/costumes/bottoms_hakama1.png'
    },
    {
      id: 'hakama2',
      name: '墨炭の袴（袴２）',
      iconImg: 'assets/costumes/icon_hakama2.png',
      icon: '🥷',
      desc: 'シックな墨炭色の現代調クロス襟道着とプリーツ袴スタイル＆3D腰帯',
      topsTex: 'assets/costumes/tops_hakama2.png',
      bottomsTex: 'assets/costumes/bottoms_hakama2.png'
    },
    {
      id: 'black_t',
      name: 'シック黒Tシャツ',
      iconImg: 'assets/costumes/icon_black_t.png',
      icon: '👕',
      desc: '深みのあるマットブラックの高級コットンTシャツ＆スリムボトムス＆銀鎖',
      topsTex: 'assets/costumes/tops_black_t.png',
      bottomsTex: 'assets/costumes/bottoms_black_t.png'
    },
    {
      id: 'shodo',
      name: '書道師範（書道）',
      iconImg: 'assets/costumes/icon_shodo.png',
      icon: '🖌️',
      desc: '「書道」豪快揮毫の白道着・背負い大筆・「筆」字鉢巻き・墨壺＆木札装備',
      topsTex: 'assets/costumes/tops_shodo.png',
      bottomsTex: 'assets/costumes/bottoms_shodo.png'
    },
    {
      id: 'sennin',
      name: '仙人道服（仙人）',
      iconImg: 'assets/costumes/icon_sennin.png',
      icon: '☯️',
      desc: '富士山・鶴・松の豪華金糸刺繍をまとう仙術羽織＆「道・仙人」3D陰陽太極帯',
      topsTex: 'assets/costumes/tops_sennin.png',
      bottomsTex: 'assets/costumes/bottoms_sennin.png'
    },
    {
      id: 'ninja',
      name: '忍び装束（忍者）',
      iconImg: 'assets/costumes/icon_ninja.png',
      icon: '🥷',
      desc: '真紅の「忍」字胸当て・特製猫耳忍び頭巾覆面・背負い秘伝巻物・手裏剣苦無',
      topsTex: 'assets/costumes/tops_ninja.png',
      bottomsTex: 'assets/costumes/bottoms_ninja.png'
    },
    {
      id: 'samurai',
      name: '名誉武士甲冑（武士）',
      iconImg: 'assets/costumes/icon_samurai.png',
      icon: '⚔️',
      desc: '黄金鍬形兜・面頬・黒漆赤糸威胴・背負い大太刀＆腰刀・大袖・脛当の天下無双甲冑',
      topsTex: 'assets/costumes/tops_samurai.png',
      bottomsTex: 'assets/costumes/bottoms_samurai.png'
    }
  ],
  accessory: [
    { id: 'none', name: 'なし', icon: '✕', desc: 'アクセサリーなし' },
    { id: 'ribbon', name: 'プリティリボン', icon: '🎀', desc: '首元を飾る赤いキュートなリボン' },
    { id: 'bell', name: 'ゴールドベル', icon: '🔔', desc: 'チリンと鳴る黄金の鈴チョーカー' },
    { id: 'goggles', name: 'パイロットゴーグル', icon: '🥽', desc: '宇宙飛行用の耐熱耐圧ゴーグル' },
    { id: 'cap', name: 'キャプテンハット', icon: '🧢', desc: '機長専用のネイビーキャップ' }
  ],
  aura: [
    { id: 'none', name: 'なし', icon: '—', desc: 'オーラなし' },
    { id: 'stars', name: 'スターダスト', icon: '✨', desc: '星屑がきらめく宇宙の光彩' },
    { id: 'paw', name: 'にくきゅうオーラ', icon: '🐾', desc: '愛らしいピンクの足あとオーラ' },
    { id: 'neon', name: 'サイバーリング', icon: '⚡', desc: '青く発光するパルスリング' },
    { id: 'sakura', name: 'さくらふぶき', icon: '🌸', desc: '舞い散る雅な桜のエフェクト' }
  ]
};

if (typeof window !== 'undefined') {
  window.CAT_COSTUMES_DATA = CAT_COSTUMES_DATA;
}

/**
 * 👘 VRM コスチューム・3Dモデリング制御マネージャー
 */
export class VrmCostumeManager {
  constructor(THREE_INSTANCE) {
    this.THREE = THREE_INSTANCE;
    this.textureCache = {};
    this.textureLoader = new this.THREE.TextureLoader();
    this.currentAuraGroup = null;
    this.preloadAllTextures();
  }

  // テクスチャの事前読み込み
  preloadAllTextures() {
    const THREE = this.THREE;
    CAT_COSTUMES_DATA.outfit.forEach(item => {
      ['topsTex', 'bottomsTex'].forEach(prop => {
        const url = item[prop];
        if (url && !this.textureCache[url]) {
          this.textureLoader.load(url, (tex) => {
            tex.colorSpace = THREE.SRGBColorSpace;
            tex.flipY = false;
            this.textureCache[url] = tex;
          });
        }
      });
    });
  }

  getTexture(url, callback) {
    const THREE = this.THREE;
    if (this.textureCache[url]) {
      callback(this.textureCache[url]);
      return;
    }
    this.textureLoader.load(url, (tex) => {
      tex.colorSpace = THREE.SRGBColorSpace;
      tex.flipY = false;
      this.textureCache[url] = tex;
      callback(tex);
    });
  }

  // 👘 衣装（テクスチャ＆3Dアクセサリ）のVRMへの完全適用
  applyOutfit(vrm, outfitId = 'default') {
    if (!vrm || !vrm.scene) return;
    const outfit = CAT_COSTUMES_DATA.outfit.find(o => o.id === outfitId) || CAT_COSTUMES_DATA.outfit[0];

    // 1. テクスチャの適用
    this.applyOutfitTextures(vrm, outfit);

    // 2. 既存の衣装アクセサリをクリーンアップ
    this.removeCostumeItems(vrm);

    // 3. 3Dモデリングアクセサリの構築とVRMボーンへのリギング
    this.buildOutfit3DModels(vrm, outfitId);
  }

  applyOutfitTextures(vrm, outfit) {
    const isDefault = outfit.id === 'default';

    // Tops
    this.getTexture(outfit.topsTex, (topsTex) => {
      vrm.scene.traverse((obj) => {
        if (obj.isMesh && obj.material) {
          const mats = Array.isArray(obj.material) ? obj.material : [obj.material];
          mats.forEach((mat) => {
            if (mat.name && mat.name.includes('Tops') && mat.name.includes('CLOTH')) {
              if (!mat.userData.originalMap) {
                mat.userData.originalMap = mat.map;
                mat.userData.originalShade = mat.shadeMultiplyTexture;
              }
              if (isDefault) {
                mat.map = mat.userData.originalMap;
                if (mat.shadeMultiplyTexture) mat.shadeMultiplyTexture = mat.userData.originalShade;
              } else {
                mat.map = topsTex;
                if (mat.shadeMultiplyTexture) mat.shadeMultiplyTexture = topsTex;
              }
              mat.needsUpdate = true;
            }
          });
        }
      });
    });

    // Bottoms
    this.getTexture(outfit.bottomsTex, (bottomsTex) => {
      vrm.scene.traverse((obj) => {
        if (obj.isMesh && obj.material) {
          const mats = Array.isArray(obj.material) ? obj.material : [obj.material];
          mats.forEach((mat) => {
            if (mat.name && mat.name.includes('Bottoms') && mat.name.includes('CLOTH')) {
              if (!mat.userData.originalMap) {
                mat.userData.originalMap = mat.map;
                mat.userData.originalShade = mat.shadeMultiplyTexture;
              }
              if (isDefault) {
                mat.map = mat.userData.originalMap;
                if (mat.shadeMultiplyTexture) mat.shadeMultiplyTexture = mat.userData.originalShade;
              } else {
                mat.map = bottomsTex;
                if (mat.shadeMultiplyTexture) mat.shadeMultiplyTexture = bottomsTex;
              }
              mat.needsUpdate = true;
            }
          });
        }
      });
    });
  }

  // 既存のコスチュームアイテムを完全に削除・解放
  removeCostumeItems(vrm) {
    if (!vrm || !vrm.scene) return;
    const toRemove = [];
    vrm.scene.traverse((obj) => {
      if (obj.userData && obj.userData.isCostumeItem) {
        toRemove.push(obj);
      }
    });
    toRemove.forEach((obj) => {
      if (obj.geometry) obj.geometry.dispose();
      if (obj.material) {
        if (Array.isArray(obj.material)) obj.material.forEach(m => m.dispose());
        else obj.material.dispose();
      }
      if (obj.parent) obj.parent.remove(obj);
    });
  }

  // 🔨 各衣装の3Dプロシージャルモデリング
  buildOutfit3DModels(vrm, outfitId) {
    if (!vrm || !vrm.humanoid) return;
    const humanoid = vrm.humanoid;
    const headNode = humanoid.getNormalizedBoneNode('head');
    const chestNode = humanoid.getNormalizedBoneNode('upperChest') || humanoid.getNormalizedBoneNode('chest');
    const hipsNode = humanoid.getNormalizedBoneNode('hips');
    const leftArmNode = humanoid.getNormalizedBoneNode('leftUpperArm');
    const rightArmNode = humanoid.getNormalizedBoneNode('rightUpperArm');
    const leftShinNode = humanoid.getNormalizedBoneNode('leftLowerLeg');
    const rightShinNode = humanoid.getNormalizedBoneNode('rightLowerLeg');

    switch (outfitId) {
      case 'samurai':
        this.buildSamurai3D(headNode, chestNode, hipsNode, leftArmNode, rightArmNode, leftShinNode, rightShinNode);
        break;
      case 'shodo':
        this.buildShodo3D(headNode, chestNode, hipsNode);
        break;
      case 'ninja':
        this.buildNinja3D(headNode, chestNode, hipsNode);
        break;
      case 'sennin':
        this.buildSennin3D(hipsNode, chestNode);
        break;
      case 'hoodie':
        this.buildHoodie3D(chestNode);
        break;
      case 'hakama1':
        this.buildHakama3D(hipsNode, 0x182848);
        break;
      case 'hakama2':
        this.buildHakama3D(hipsNode, 0x323236);
        break;
      case 'black_t':
        this.buildBlackT3D(chestNode);
        break;
    }
  }

  // ⚔️ 1. 武士 (Samurai Armor 3D)
  buildSamurai3D(head, chest, hips, lArm, rArm, lShin, rShin) {
    const THREE = this.THREE;
    const ironMat = new THREE.MeshStandardMaterial({ color: 0x18181c, metalness: 0.85, roughness: 0.3 });
    const goldMat = new THREE.MeshStandardMaterial({ color: 0xffd700, metalness: 0.95, roughness: 0.15 });
    const redMat = new THREE.MeshStandardMaterial({ color: 0xb51c1c, roughness: 0.5 });

    // === 兜冠・黄金鍬形の前立 (Samurai Kuwagata Crest Crown on Head) ===
    // ※ ネコ本来の愛らしい耳や表情を隠さない、マスコット専用の英雄甲冑冠
    if (head) {
      const crownGroup = new THREE.Group();
      crownGroup.userData.isCostumeItem = true;

      // 額の黒漆鉢巻き・前板 (Black Lacquer Forehead Band)
      const band = new THREE.Mesh(
        new THREE.CylinderGeometry(0.125, 0.13, 0.024, 24, 1, true, Math.PI * 0.22, Math.PI * 0.56),
        ironMat
      );
      band.position.set(0, 0.07, 0.02);
      band.rotation.x = -0.15;
      crownGroup.add(band);

      // 前立て座 (Maedate Base - 黄金菊座)
      const crestBase = new THREE.Mesh(new THREE.CylinderGeometry(0.022, 0.022, 0.008, 16), goldMat);
      crestBase.rotation.x = Math.PI / 2;
      crestBase.position.set(0, 0.09, 0.135);
      crownGroup.add(crestBase);

      // 黄金の大鍬形・左角 (Golden Kuwagata Horn - Left)
      const lHorn = new THREE.Mesh(new THREE.ConeGeometry(0.012, 0.17, 8), goldMat);
      lHorn.position.set(-0.055, 0.17, 0.13);
      lHorn.rotation.z = -0.52;
      lHorn.rotation.x = -0.18;
      crownGroup.add(lHorn);

      // 黄金の大鍬形・右角 (Golden Kuwagata Horn - Right)
      const rHorn = new THREE.Mesh(new THREE.ConeGeometry(0.012, 0.17, 8), goldMat);
      rHorn.position.set(0.055, 0.17, 0.13);
      rHorn.rotation.z = 0.52;
      rHorn.rotation.x = -0.18;
      crownGroup.add(rHorn);

      // 中央の武将金紋 (Center Gold Crest Emblem)
      const emblem = new THREE.Mesh(new THREE.BoxGeometry(0.018, 0.075, 0.006), goldMat);
      emblem.position.set(0, 0.145, 0.135);
      crownGroup.add(emblem);

      // 後ろ結び目の朱色紐 (Crimson Tie Ribbons at Back)
      const tie1 = new THREE.Mesh(new THREE.BoxGeometry(0.014, 0.11, 0.004), redMat);
      tie1.position.set(-0.02, 0.01, -0.125);
      tie1.rotation.z = 0.25;
      crownGroup.add(tie1);

      const tie2 = new THREE.Mesh(new THREE.BoxGeometry(0.014, 0.11, 0.004), redMat);
      tie2.position.set(0.02, 0.01, -0.125);
      tie2.rotation.z = -0.25;
      crownGroup.add(tie2);

      head.add(crownGroup);
    }

    // === 背負い名刀・大太刀 (Great Katana on Chest) ===
    if (chest) {
      const katanaGroup = new THREE.Group();
      katanaGroup.userData.isCostumeItem = true;

      // 鞘 (Saya)
      const saya = new THREE.Mesh(new THREE.CylinderGeometry(0.015, 0.013, 0.90, 12), ironMat);
      katanaGroup.add(saya);

      // 鐺 (Kojiri) 金具
      const kojiri = new THREE.Mesh(new THREE.CylinderGeometry(0.016, 0.014, 0.045, 12), goldMat);
      kojiri.position.y = -0.43;
      katanaGroup.add(kojiri);

      // 鍔 (Tsuba)
      const tsuba = new THREE.Mesh(new THREE.CylinderGeometry(0.042, 0.042, 0.008, 16), goldMat);
      tsuba.position.y = 0.45;
      katanaGroup.add(tsuba);

      // 柄 (Tsuka)
      const tsuka = new THREE.Mesh(
        new THREE.CylinderGeometry(0.013, 0.013, 0.22, 10),
        new THREE.MeshStandardMaterial({ color: 0x111115, roughness: 0.7 })
      );
      tsuka.position.y = 0.57;
      katanaGroup.add(tsuka);

      // 頭 (Kashira) 金具
      const kashira = new THREE.Mesh(new THREE.SphereGeometry(0.015, 10, 10), goldMat);
      kashira.position.y = 0.68;
      katanaGroup.add(kashira);

      katanaGroup.position.set(-0.10, 0.12, -0.16);
      katanaGroup.rotation.set(0.16, 0.10, 0.62);
      chest.add(katanaGroup);
    }

    // === 腰刀・脇差 (Waist Katana on Hips) ===
    if (hips) {
      const waistKatana = new THREE.Group();
      waistKatana.userData.isCostumeItem = true;

      const wSaya = new THREE.Mesh(new THREE.CylinderGeometry(0.012, 0.010, 0.48, 10), ironMat);
      waistKatana.add(wSaya);

      const wTsuba = new THREE.Mesh(new THREE.CylinderGeometry(0.032, 0.032, 0.006, 12), goldMat);
      wTsuba.position.y = 0.24;
      waistKatana.add(wTsuba);

      const wTsuka = new THREE.Mesh(
        new THREE.CylinderGeometry(0.011, 0.011, 0.15, 10),
        new THREE.MeshStandardMaterial({ color: 0x181820, roughness: 0.7 })
      );
      wTsuka.position.y = 0.32;
      waistKatana.add(wTsuka);

      waistKatana.position.set(-0.16, 0.05, 0.03);
      waistKatana.rotation.set(0.12, 0.18, -0.22);
      hips.add(waistKatana);
    }

    // === 大袖 (Sode Shoulder Armor on Arms - 自然なスケール) ===
    [ { arm: lArm, sign: 1 }, { arm: rArm, sign: -1 } ].forEach(({ arm, sign }) => {
      if (arm) {
        const sodeGroup = new THREE.Group();
        sodeGroup.userData.isCostumeItem = true;
        [0, 1].forEach(i => {
          const plate = new THREE.Mesh(
            new THREE.BoxGeometry(0.09, 0.024, 0.08),
            i === 0 ? ironMat : redMat
          );
          plate.position.set(0, -i * 0.022, 0);
          sodeGroup.add(plate);
        });
        sodeGroup.position.set(sign * 0.055, 0.01, 0);
        arm.add(sodeGroup);
      }
    });

    // === 脛当 (Suneate Shin Armor on Legs) ===
    [ lShin, rShin ].forEach(shin => {
      if (shin) {
        const suneate = new THREE.Mesh(
          new THREE.CylinderGeometry(0.065, 0.055, 0.22, 12, 1, false, Math.PI * 0.2, Math.PI * 0.6),
          ironMat
        );
        suneate.userData.isCostumeItem = true;
        suneate.position.set(0, -0.12, 0.04);
        shin.add(suneate);
      }
    });
  }

  // 🖌️ 2. 書道師範 (Calligraphy Master 3D)
  buildShodo3D(head, chest, hips) {
    const THREE = this.THREE;

    // === 「筆」字 鉢巻き on Head ===
    if (head) {
      const headGroup = new THREE.Group();
      headGroup.userData.isCostumeItem = true;

      // 鉢巻き本体リング
      const band = new THREE.Mesh(
        new THREE.TorusGeometry(0.125, 0.014, 8, 32),
        new THREE.MeshStandardMaterial({ color: 0x18181c, roughness: 0.8 })
      );
      band.rotation.x = Math.PI / 2;
      band.position.set(0, 0.08, 0.02);
      headGroup.add(band);

      // 「筆」字の額布キャンバステクスチャ
      const canvas = document.createElement('canvas');
      canvas.width = 128;
      canvas.height = 128;
      const ctx = canvas.getContext('2d');
      ctx.fillStyle = '#f8f8fa';
      ctx.beginPath();
      ctx.roundRect(8, 20, 112, 88, 12);
      ctx.fill();
      ctx.strokeStyle = '#c02020';
      ctx.lineWidth = 4;
      ctx.stroke();
      ctx.fillStyle = '#c02020';
      ctx.font = 'bold 64px serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('筆', 64, 64);

      const fudeTex = new THREE.CanvasTexture(canvas);
      fudeTex.colorSpace = THREE.SRGBColorSpace;
      const fudeBadge = new THREE.Mesh(
        new THREE.PlaneGeometry(0.055, 0.045),
        new THREE.MeshBasicMaterial({ map: fudeTex, transparent: true, side: THREE.DoubleSide })
      );
      fudeBadge.position.set(0, 0.08, 0.145);
      headGroup.add(fudeBadge);

      // 後ろ結び目のリボン
      const ribbon1 = new THREE.Mesh(
        new THREE.BoxGeometry(0.02, 0.14, 0.004),
        new THREE.MeshStandardMaterial({ color: 0x18181c, roughness: 0.8 })
      );
      ribbon1.position.set(-0.02, 0.01, -0.13);
      ribbon1.rotation.z = 0.2;
      headGroup.add(ribbon1);

      const ribbon2 = new THREE.Mesh(
        new THREE.BoxGeometry(0.02, 0.14, 0.004),
        new THREE.MeshStandardMaterial({ color: 0x18181c, roughness: 0.8 })
      );
      ribbon2.position.set(0.02, 0.01, -0.13);
      ribbon2.rotation.z = -0.2;
      headGroup.add(ribbon2);

      head.add(headGroup);
    }

    // === 背負い大筆 (Giant Calligraphy Brush on Chest) ===
    if (chest) {
      const brushGroup = new THREE.Group();
      brushGroup.userData.isCostumeItem = true;

      // 竹軸 (Bamboo Shaft)
      const shaft = new THREE.Mesh(
        new THREE.CylinderGeometry(0.022, 0.024, 0.96, 16),
        new THREE.MeshStandardMaterial({ color: 0x9b6b3e, roughness: 0.45 })
      );
      brushGroup.add(shaft);

      // 金具リング (Brass Ferrules)
      const goldMat = new THREE.MeshStandardMaterial({ color: 0xd4af37, metalness: 0.85, roughness: 0.25 });
      [-0.40, 0.1, 0.42].forEach(y => {
        const ring = new THREE.Mesh(new THREE.CylinderGeometry(0.025, 0.025, 0.02, 16), goldMat);
        ring.position.y = y;
        brushGroup.add(ring);
      });

      // 筆尻の吊り紐金具
      const topCap = new THREE.Mesh(new THREE.SphereGeometry(0.026, 12, 12), goldMat);
      topCap.position.y = 0.48;
      brushGroup.add(topCap);

      // 筆毛 (Brush Bristle Head)
      // 根元の馬毛 (天然の白毛)
      const hairBase = new THREE.Mesh(
        new THREE.ConeGeometry(0.058, 0.24, 20),
        new THREE.MeshStandardMaterial({ color: 0xe5dec9, roughness: 0.6 })
      );
      hairBase.position.y = -0.58;
      hairBase.rotation.x = Math.PI;
      brushGroup.add(hairBase);

      // 穂先 (瑞々しい純黒の墨滴)
      const inkTip = new THREE.Mesh(
        new THREE.ConeGeometry(0.038, 0.16, 20),
        new THREE.MeshStandardMaterial({ color: 0x0a0a0f, roughness: 0.08 })
      );
      inkTip.position.y = -0.70;
      inkTip.rotation.x = Math.PI;
      brushGroup.add(inkTip);

      brushGroup.position.set(-0.09, 0.16, -0.17);
      brushGroup.rotation.set(0.15, -0.12, -0.62);
      chest.add(brushGroup);
    }

    // === 腰の墨壺＆木札 (Ink Jars & Cedar Tag on Hips) ===
    if (hips) {
      const hipsGroup = new THREE.Group();
      hipsGroup.userData.isCostumeItem = true;

      // ガラスの墨瓶
      const jar = new THREE.Mesh(
        new THREE.CylinderGeometry(0.022, 0.024, 0.055, 12),
        new THREE.MeshStandardMaterial({ color: 0x111116, roughness: 0.15, metalness: 0.1 })
      );
      jar.position.set(0.15, 0.04, 0.12);
      hipsGroup.add(jar);

      // コルク栓
      const cork = new THREE.Mesh(
        new THREE.CylinderGeometry(0.014, 0.016, 0.015, 10),
        new THREE.MeshStandardMaterial({ color: 0xb58850, roughness: 0.8 })
      );
      cork.position.set(0.15, 0.075, 0.12);
      hipsGroup.add(cork);

      // 檜の木札「墨雲」
      const tagCanvas = document.createElement('canvas');
      tagCanvas.width = 64;
      tagCanvas.height = 128;
      const tctx = tagCanvas.getContext('2d');
      tctx.fillStyle = '#c8a065';
      tctx.fillRect(0, 0, 64, 128);
      tctx.strokeStyle = '#5a3d1c';
      tctx.lineWidth = 4;
      tctx.strokeRect(2, 2, 60, 124);
      tctx.fillStyle = '#111';
      tctx.font = 'bold 36px serif';
      tctx.textAlign = 'center';
      tctx.fillText('墨', 32, 45);
      tctx.fillText('雲', 32, 90);
      const tagTex = new THREE.CanvasTexture(tagCanvas);
      tagTex.colorSpace = THREE.SRGBColorSpace;
      const tagMesh = new THREE.Mesh(
        new THREE.PlaneGeometry(0.035, 0.07),
        new THREE.MeshBasicMaterial({ map: tagTex, side: THREE.DoubleSide })
      );
      tagMesh.position.set(0.17, -0.02, 0.13);
      hipsGroup.add(tagMesh);

      hips.add(hipsGroup);
    }
  }

  // 🥷 3. 忍び装束 (Ninja Shinobi 3D)
  buildNinja3D(head, chest, hips) {
    const THREE = this.THREE;
    const navyMat = new THREE.MeshStandardMaterial({ color: 0x162238, roughness: 0.7 });
    const steelMat = new THREE.MeshStandardMaterial({ color: 0x889098, metalness: 0.9, roughness: 0.25 });

    // === 忍び額当て (Shinobi Hitai-ate Forehead Protector on Head) ===
    // ※ ネコ本来の愛らしい顔・口元を覆わず、額に凛々しく装着
    if (head) {
      const ninjaHead = new THREE.Group();
      ninjaHead.userData.isCostumeItem = true;

      // 額当て紺布バンド (Navy Cloth Headband)
      const cowlBand = new THREE.Mesh(
        new THREE.CylinderGeometry(0.124, 0.128, 0.022, 24, 1, true, Math.PI * 0.22, Math.PI * 0.56),
        navyMat
      );
      cowlBand.position.set(0, 0.07, 0.02);
      cowlBand.rotation.x = -0.15;
      ninjaHead.add(cowlBand);

      // 忍び金属プレート (Steel Hitai-ate Plate)
      const plate = new THREE.Mesh(new THREE.BoxGeometry(0.065, 0.032, 0.006), steelMat);
      plate.position.set(0, 0.075, 0.136);
      ninjaHead.add(plate);

      // 「忍」字 キャンバステクスチャ紋
      const nCanvas = document.createElement('canvas');
      nCanvas.width = 128;
      nCanvas.height = 128;
      const nCtx = nCanvas.getContext('2d');
      nCtx.fillStyle = '#889098';
      nCtx.fillRect(0, 0, 128, 128);
      nCtx.fillStyle = '#c02020';
      nCtx.font = 'bold 88px sans-serif';
      nCtx.textAlign = 'center';
      nCtx.textBaseline = 'middle';
      nCtx.fillText('忍', 64, 64);

      const nTex = new THREE.CanvasTexture(nCanvas);
      nTex.colorSpace = THREE.SRGBColorSpace;
      const nBadge = new THREE.Mesh(
        new THREE.PlaneGeometry(0.045, 0.026),
        new THREE.MeshBasicMaterial({ map: nTex, side: THREE.DoubleSide })
      );
      nBadge.position.set(0, 0.075, 0.140);
      ninjaHead.add(nBadge);

      // 後ろに結ばれた忍びリボン (Trailing Tie Ribbons)
      const nRibbon1 = new THREE.Mesh(new THREE.BoxGeometry(0.016, 0.14, 0.004), navyMat);
      nRibbon1.position.set(-0.02, 0.01, -0.125);
      nRibbon1.rotation.z = 0.22;
      ninjaHead.add(nRibbon1);

      const nRibbon2 = new THREE.Mesh(new THREE.BoxGeometry(0.016, 0.14, 0.004), navyMat);
      nRibbon2.position.set(0.02, 0.01, -0.125);
      nRibbon2.rotation.z = -0.22;
      ninjaHead.add(nRibbon2);

      head.add(ninjaHead);
    }

    // === 秘伝忍術巻物 (Secret Ninjutsu Scroll on Chest) ===
    if (chest) {
      const scrollGroup = new THREE.Group();
      scrollGroup.userData.isCostumeItem = true;

      // 巻物紙面
      const parchment = new THREE.Mesh(
        new THREE.CylinderGeometry(0.032, 0.032, 0.38, 16),
        new THREE.MeshStandardMaterial({ color: 0xded4b8, roughness: 0.55 })
      );
      parchment.rotation.z = Math.PI / 2;
      scrollGroup.add(parchment);

      // 両端の木製軸棒
      const woodMat = new THREE.MeshStandardMaterial({ color: 0x3d2212, roughness: 0.4 });
      [-0.20, 0.20].forEach(x => {
        const spool = new THREE.Mesh(new THREE.CylinderGeometry(0.038, 0.038, 0.025, 16), woodMat);
        spool.rotation.z = Math.PI / 2;
        spool.position.x = x;
        scrollGroup.add(spool);
      });

      scrollGroup.position.set(0, 0.12, -0.16);
      scrollGroup.rotation.set(0, 0, 0.32);
      chest.add(scrollGroup);
    }

    // === 手裏剣＆苦無ホルスター on Hips ===
    if (hips) {
      const hipGroup = new THREE.Group();
      hipGroup.userData.isCostumeItem = true;

      // 四方手裏剣 (Quad Shuriken)
      const shuriken = new THREE.Group();
      [0, Math.PI / 2].forEach(rot => {
        const blade = new THREE.Mesh(new THREE.BoxGeometry(0.065, 0.015, 0.003), steelMat);
        blade.rotation.z = rot;
        shuriken.add(blade);
      });
      shuriken.position.set(0.12, 0.06, 0.13);
      shuriken.rotation.y = 0.2;
      hipGroup.add(shuriken);

      // 苦無 (Kunai)
      const kunai = new THREE.Mesh(new THREE.ConeGeometry(0.02, 0.12, 4), steelMat);
      kunai.position.set(-0.14, 0.04, 0.12);
      kunai.rotation.x = Math.PI;
      hipGroup.add(kunai);

      hips.add(hipGroup);
    }
  }

  // ☯️ 4. 仙人道服 (Taoist Sage 3D)
  buildSennin3D(hips, chest) {
    const THREE = this.THREE;

    // === 陰陽太極帯 (Grand Yin-Yang Belt on Hips) ===
    if (hips) {
      const beltGroup = new THREE.Group();
      beltGroup.userData.isCostumeItem = true;

      // 青銅外輪
      const disk = new THREE.Mesh(
        new THREE.CylinderGeometry(0.075, 0.075, 0.014, 24),
        new THREE.MeshStandardMaterial({ color: 0x3d5a52, metalness: 0.8, roughness: 0.35 })
      );
      disk.rotation.x = Math.PI / 2;
      disk.position.set(0, 0.04, 0.145);
      beltGroup.add(disk);

      // 陰陽太極図 (Taijitu Canvas Texture)
      const canvas = document.createElement('canvas');
      canvas.width = 128;
      canvas.height = 128;
      const ctx = canvas.getContext('2d');
      // 円形枠
      ctx.fillStyle = '#d4af37';
      ctx.beginPath();
      ctx.arc(64, 64, 60, 0, Math.PI * 2);
      ctx.fill();
      // 陰（深碧）
      ctx.fillStyle = '#1c3a32';
      ctx.beginPath();
      ctx.arc(64, 64, 56, -Math.PI / 2, Math.PI / 2);
      ctx.arc(64, 92, 28, Math.PI / 2, -Math.PI / 2, true);
      ctx.arc(64, 36, 28, Math.PI / 2, -Math.PI / 2);
      ctx.fill();
      // 陽（金）
      ctx.fillStyle = '#ffd700';
      ctx.beginPath();
      ctx.arc(64, 36, 8, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#1c3a32';
      ctx.beginPath();
      ctx.arc(64, 92, 8, 0, Math.PI * 2);
      ctx.fill();

      const taijituTex = new THREE.CanvasTexture(canvas);
      taijituTex.colorSpace = THREE.SRGBColorSpace;
      const taijitu = new THREE.Mesh(
        new THREE.PlaneGeometry(0.12, 0.12),
        new THREE.MeshBasicMaterial({ map: taijituTex, transparent: true, side: THREE.DoubleSide })
      );
      taijitu.position.set(0, 0.04, 0.154);
      beltGroup.add(taijitu);

      // 左右の「道」「仙人」金文字木札
      const goldMat = new THREE.MeshStandardMaterial({ color: 0xd4af37, metalness: 0.9, roughness: 0.2 });
      const badgeL = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.035, 0.008), goldMat);
      badgeL.position.set(-0.09, 0.04, 0.14);
      beltGroup.add(badgeL);

      const badgeR = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.035, 0.008), goldMat);
      badgeR.position.set(0.09, 0.04, 0.14);
      beltGroup.add(badgeR);

      hips.add(beltGroup);
    }

    // === 仙術光輪 (Celestial Taoist Halo on Chest) ===
    if (chest) {
      const haloGroup = new THREE.Group();
      haloGroup.userData.isCostumeItem = true;

      const haloRing = new THREE.Mesh(
        new THREE.TorusGeometry(0.35, 0.012, 12, 36),
        new THREE.MeshStandardMaterial({ color: 0xffd700, metalness: 0.9, roughness: 0.15 })
      );
      haloGroup.add(haloRing);

      const haloLight = new THREE.PointLight(0xffd700, 1.2, 2.5);
      haloGroup.add(haloLight);

      haloGroup.position.set(0, 0.20, -0.22);
      chest.add(haloGroup);
    }
  }

  // 🐟 5. さかなパーカー (Fish Hoodie 3D - 自然なドレープ＆コード)
  buildHoodie3D(chest) {
    const THREE = this.THREE;
    if (!chest) return;

    const hoodieGroup = new THREE.Group();
    hoodieGroup.userData.isCostumeItem = true;

    // 背中に自然に落ちた3Dフード (Natural Dropped Hoodie Hood)
    const hoodMat = new THREE.MeshStandardMaterial({ color: 0x141f36, roughness: 0.8 });
    const hood = new THREE.Mesh(
      new THREE.SphereGeometry(0.095, 16, 12, 0, Math.PI * 2, 0, Math.PI * 0.45),
      hoodMat
    );
    hood.rotation.x = Math.PI * 0.95;
    hood.position.set(0, 0.11, -0.115);
    hood.scale.set(1.05, 0.65, 0.85);
    hoodieGroup.add(hood);

    // 胸元から垂れる白コード紐 (Natural Drawstrings)
    const cordMat = new THREE.MeshStandardMaterial({ color: 0xf5f5fa, roughness: 0.4 });
    const agletMat = new THREE.MeshStandardMaterial({ color: 0xdcdce2, metalness: 0.9, roughness: 0.15 });

    [-0.032, 0.032].forEach(x => {
      // 紐本体
      const cord = new THREE.Mesh(new THREE.CylinderGeometry(0.004, 0.004, 0.20, 8), cordMat);
      cord.position.set(x, 0.03, 0.138);
      hoodieGroup.add(cord);

      // 金属アグレット先端
      const aglet = new THREE.Mesh(new THREE.CylinderGeometry(0.005, 0.005, 0.022, 8), agletMat);
      aglet.position.set(x, -0.075, 0.138);
      hoodieGroup.add(aglet);
    });

    chest.add(hoodieGroup);
  }

  // 🥋 6 & 7. 袴スタイル (Hakama 3D Waist Knot)
  buildHakama3D(hips, colorHex = 0x182848) {
    const THREE = this.THREE;
    if (!hips) return;

    const hakamaGroup = new THREE.Group();
    hakamaGroup.userData.isCostumeItem = true;
    const hakamaMat = new THREE.MeshStandardMaterial({ color: colorHex, roughness: 0.65 });

    // 前紐の結び目 (Front Knot)
    const knot = new THREE.Mesh(new THREE.BoxGeometry(0.055, 0.030, 0.018), hakamaMat);
    knot.position.set(0, 0.055, 0.142);
    hakamaGroup.add(knot);

    // 垂れる紐端 (Ribbon Tails)
    const tailL = new THREE.Mesh(new THREE.BoxGeometry(0.022, 0.19, 0.006), hakamaMat);
    tailL.position.set(-0.022, -0.045, 0.145);
    tailL.rotation.z = 0.07;
    hakamaGroup.add(tailL);

    const tailR = new THREE.Mesh(new THREE.BoxGeometry(0.022, 0.17, 0.006), hakamaMat);
    tailR.position.set(0.022, -0.035, 0.145);
    tailR.rotation.z = -0.07;
    hakamaGroup.add(tailR);

    hips.add(hakamaGroup);
  }

  // 👕 8. 黒Tシャツ (Black T-shirt 3D Chain & Pendant)
  buildBlackT3D(chest) {
    const THREE = this.THREE;
    if (!chest) return;

    const chainGroup = new THREE.Group();
    chainGroup.userData.isCostumeItem = true;

    // 首元のシルバージュエリーチェーン (Silver Curb Chain)
    const chainMat = new THREE.MeshStandardMaterial({ color: 0xeeeeee, metalness: 0.95, roughness: 0.12 });
    const chain = new THREE.Mesh(new THREE.TorusGeometry(0.078, 0.004, 8, 24), chainMat);
    chain.rotation.x = Math.PI * 0.44;
    chain.position.set(0, 0.11, 0.092);
    chainGroup.add(chain);

    // 魚モチーフのシルバーチャームペンダント (Fish Charm Pendant)
    const pendant = new THREE.Mesh(new THREE.BoxGeometry(0.016, 0.024, 0.004), chainMat);
    pendant.position.set(0, 0.036, 0.118);
    chainGroup.add(pendant);

    chest.add(chainGroup);
  }

  // 🎀 装飾アクセサリ（リボン, ベル, ゴーグル, キャップ）
  applyAccessory(vrm, accId = 'none') {
    if (!vrm || !vrm.humanoid) return;
    const THREE = this.THREE;
    const humanoid = vrm.humanoid;
    const head = humanoid.getNormalizedBoneNode('head');
    const neck = humanoid.getNormalizedBoneNode('neck') || humanoid.getNormalizedBoneNode('chest');

    // 既存アクセサリの削除
    const toRemove = [];
    vrm.scene.traverse((obj) => {
      if (obj.userData && obj.userData.isHeadAccessory) toRemove.push(obj);
    });
    toRemove.forEach(obj => obj.parent && obj.parent.remove(obj));

    if (accId === 'none') return;

    if (accId === 'ribbon' && neck) {
      const ribbonGroup = new THREE.Group();
      ribbonGroup.userData.isHeadAccessory = true;
      const redMat = new THREE.MeshStandardMaterial({ color: 0xff2255, roughness: 0.5 });
      const bow = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.035, 0.02), redMat);
      bow.position.set(0, 0.02, 0.12);
      ribbonGroup.add(bow);
      neck.add(ribbonGroup);
    } else if (accId === 'bell' && neck) {
      const bellGroup = new THREE.Group();
      bellGroup.userData.isHeadAccessory = true;
      const goldMat = new THREE.MeshStandardMaterial({ color: 0xffd700, metalness: 0.9, roughness: 0.2 });
      const bell = new THREE.Mesh(new THREE.SphereGeometry(0.025, 12, 12), goldMat);
      bell.position.set(0, 0.02, 0.13);
      bellGroup.add(bell);
      neck.add(bellGroup);
    } else if (accId === 'goggles' && head) {
      const gGroup = new THREE.Group();
      gGroup.userData.isHeadAccessory = true;
      const gMat = new THREE.MeshStandardMaterial({ color: 0x222225, roughness: 0.4 });
      const lensMat = new THREE.MeshStandardMaterial({ color: 0x00e5ff, metalness: 0.8, roughness: 0.1 });
      [-0.045, 0.045].forEach(x => {
        const frame = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 0.015, 16), gMat);
        frame.rotation.x = Math.PI / 2;
        frame.position.set(x, 0.09, 0.135);
        gGroup.add(frame);
        const lens = new THREE.Mesh(new THREE.CylinderGeometry(0.024, 0.024, 0.016, 16), lensMat);
        lens.rotation.x = Math.PI / 2;
        lens.position.set(x, 0.09, 0.136);
        gGroup.add(lens);
      });
      head.add(gGroup);
    } else if (accId === 'cap' && head) {
      const capGroup = new THREE.Group();
      capGroup.userData.isHeadAccessory = true;
      const capMat = new THREE.MeshStandardMaterial({ color: 0x142038, roughness: 0.6 });
      const goldMat = new THREE.MeshStandardMaterial({ color: 0xffd700, metalness: 0.9 });
      const dome = new THREE.Mesh(new THREE.SphereGeometry(0.125, 16, 12, 0, Math.PI * 2, 0, Math.PI * 0.5), capMat);
      dome.position.set(0, 0.10, -0.01);
      capGroup.add(dome);
      const brim = new THREE.Mesh(new THREE.CylinderGeometry(0.135, 0.14, 0.012, 16, 1, false, Math.PI * 0.25, Math.PI * 0.5), capMat);
      brim.position.set(0, 0.09, 0.04);
      brim.rotation.x = -0.15;
      capGroup.add(brim);
      head.add(capGroup);
    }
  }

  // 🌟 オーラ（光彩）エフェクト
  applyAura(scene, vrm, auraId = 'none') {
    const THREE = this.THREE;
    if (this.currentAuraGroup) {
      if (this.currentAuraGroup.parent) {
        this.currentAuraGroup.parent.remove(this.currentAuraGroup);
      }
      this.currentAuraGroup = null;
    }
    if (auraId === 'none' || !scene) return;

    const auraGroup = new THREE.Group();
    auraGroup.name = 'VrmAuraGroup';

    if (auraId === 'neon') {
      const ring = new THREE.Mesh(
        new THREE.TorusGeometry(0.55, 0.018, 12, 40),
        new THREE.MeshBasicMaterial({ color: 0x00e5ff })
      );
      ring.rotation.x = Math.PI / 2;
      ring.position.y = 0.85;
      auraGroup.add(ring);
    } else if (auraId === 'sakura' || auraId === 'stars') {
      const color = (auraId === 'sakura') ? 0xff77aa : 0xffdd44;
      const count = 24;
      const pGeo = new THREE.BufferGeometry();
      const positions = new Float32Array(count * 3);
      for (let i = 0; i < count; i++) {
        const angle = (i / count) * Math.PI * 2;
        const rad = 0.45 + Math.random() * 0.35;
        positions[i * 3] = Math.cos(angle) * rad;
        positions[i * 3 + 1] = 0.2 + Math.random() * 1.4;
        positions[i * 3 + 2] = Math.sin(angle) * rad;
      }
      pGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
      const pMat = new THREE.PointsMaterial({ color, size: 0.05, transparent: true, opacity: 0.8 });
      const pts = new THREE.Points(pGeo, pMat);
      auraGroup.add(pts);
    }

    scene.add(auraGroup);
    this.currentAuraGroup = auraGroup;
  }
}
