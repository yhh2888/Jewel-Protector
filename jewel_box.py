import random  # 렌덤 무게를 쓰기 위해 꼭 필요해요!

def jewel_box():
    jewels = {
        "diamond": True, "ruby": True, "sapphire": True, "emerald": True,
        "amethyst": True, "topaz": True, "opal": True, "garnet": True,
        "aquamarine": True, "peridot": True, "tanzanite": True, "turquoise": True,
        "pearl": True, "amber": True, "jade": True, "spinel": True,
        "moonstone": True, "citrine": True, "lapis_lazuli": True, "black_onyx": True
    }
    return jewels


def choice(count):  
    original_jewels = jewel_box()
    jewel_names = list(original_jewels.keys())
    
    game_jewels = {}
    
    print("\n[ 지정된 보석 및 무게 정보 ]")
    print("-" * 35)

    while count > 0:
        name = jewel_names[random.randint(0, len(jewel_names)-1)]             
        weight = random.randint(1, 101)  
        if name not in game_jewels:
            game_jewels[name] = weight       
            print(f"💎 {name} | 무게: {weight}g")
            count -= 1
        
    print("-" * 35)
    
    return game_jewels
