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


def choice():  
    original_jewels = jewel_box()
    jewel_names = list(original_jewels.keys())
    
    count = int(input(f"보석의 수를 지정해주세요 (1~{len(jewel_names)}개): "))
    
    game_jewels = {}
    
    print("\n[ 지정된 보석 및 무게 정보 ]")
    print("-" * 35)

    for i in range(count):
        name = jewel_names[random.randint(0, len(jewel_names))]             
        weight = random.randint(1, 101)  
        
        game_jewels[name] = weight       
        print(f"💎 {name} | 무게: {weight}g")
        
    print("-" * 35)
    
    return game_jewels


final_jewels = choice()
    