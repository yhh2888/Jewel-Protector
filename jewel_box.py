import random  # 렌덤 무게를 쓰기 위해 꼭 필요해요!

def jewel_box():
    jewels = {
        
        "diamond": True, "ruby": True, "sapphire": True, "emerald": True,
        "amethyst": True, "topaz": True, "opal": True, "garnet": True,
        "aquamarine": True, "peridot": True, "tanzanite": True, "turquoise": True,
        "pearl": True, "amber": True, "jade": True, "spinel": True,
        "moonstone": True, "citrine": True, "lapis_lazuli": True, "black_onyx": True,
        "alexandrite": True, "tourmaline": True, "zircon": True, "morganite": True,
        "kunzite": True, "sunstone": True, "bloodstone": True, "carnelian": True,
        "malachite": True, "obsidian": True, "tiger_eye": True, "rose_quartz": True,
        "smoky_quartz": True, "adularia": True, "agate": True, "jasper": True,
        "hematite": True, "pyrite": True, "rhochrosite": True, "larimar": True,
        "charoite": True, "sugilite": True, "chrysoberyl": True, "iolite": True,
        "apatite": True, "fluorite": True, "labradorite": True, "amazonite": True,
        "rhodonite": True, "aventurine": True
    }
    return jewels


def choice(count):  
    original_jewels = jewel_box()
    jewel_names = list(original_jewels.keys())
    
    game_jewels = {}
    
    while count > 0:
        name = jewel_names[random.randint(0, len(jewel_names)-1)]             
        weight = random.randint(1, 101)  
        if name not in game_jewels:
            game_jewels[name] = weight
            count -= 1
    
    print("\n[ 지정된 보석 및 무게 정보 ]")
    print("-" * 45)
    listjewel = list(game_jewels.keys())
    listjewel.sort()
    for name in listjewel:
        print(f"{name}: {game_jewels[name]}g")
    print("-" * 45)
    
    
    return game_jewels
