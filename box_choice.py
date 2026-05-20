
# # 턴마다 훔치는 것 랜덤으로 지정하는 함수


import random

ThiefAlive = True

jewels = {
        "diamond": True,       # 다이아몬드
        "ruby": True,          # 루비
        "sapphire": True,      # 사파이어
        "emerald": True,       # 에메랄드
        "amethyst": True,      # 자수정
        "topaz": True,         # 토파즈
        "opal": True,          # 오팔
        "garnet": True,        # 가넷
        "aquamarine": True,    # 아쿠아마린
        "peridot": True,       # 페리도트
        "tanzanite": True,     # 탄자나이트
        "turquoise": True,     # 터키석
        "pearl": True,         # 진주
        "amber": True,         # 호박
        "jade": True,          # 제이드(옥)
        "spinel": True,        # 스피넬
        "moonstone": True,     # 문스톤
        "citrine": True,       # 시트린
        "lapis_lazuli": True,  # 라피스라줄리 
        "black_onyx": True     # 블랙오닉스 
}

turn = 1
chosenJewel = str
jewelsLists = list(jewels.keys())
stolenJewels = []

while True:
        if True not in jewels.values():
            print('도둑이 승리하였습니다. 모든 보석이 털렸습니다.')    
            break  

        if ThiefAlive == True:
            stoleJewel = random.choice(jewelsLists)
            jewels[stoleJewel] = False 
            print(f' [{turn}]째 턴에 도둑이 보석 하나를 훔쳐갔습니다.') 

            idx = jewelsLists.index(stoleJewel)
            targetJewel = jewelsLists.pop(idx)
            stolenJewels.append(targetJewel)  

            # 여기에 힌트를 넣으면 좋을듯
            
            print(f' 힌트: 이번에 훔쳐간 보석은 삐리리리 뭐시기 ')

            while True:
                userAnswer = input('이번 턴에 도둑이 훔친 보석을 추리하시오: ')
                
                if (userAnswer == targetJewel) or (userAnswer in jewelsLists):
                    break 
                else:
                    print('목록에 없거나 오타입니다.')
                break

            if userAnswer == str(targetJewel):
                 ThiefAlive = False
                 print('체포 성공! 도둑이 잡혔습니다.')
                 break
            else:
                 print('틀렸습니다! 도둑이 다음 보석을 노립니다.')

            print(f'턴 수: {turn}턴')
            print(f'훔친 보석 목록: {sorted(stolenJewels)}')

        turn += 1



# ThiefAlive = True

# jewels = {
#         "diamond": True,       # 다이아몬드
#         "ruby": True,          # 루비
#         "sapphire": True,      # 사파이어
#         "emerald": True,       # 에메랄드
#         "amethyst": True,      # 자수정
#         "topaz": True,         # 토파즈
#         "opal": True,          # 오팔
#         "garnet": True,        # 가넷
#         "aquamarine": True,    # 아쿠아마린
#         "peridot": True,       # 페리도트
#         "tanzanite": True,     # 탄자나이트
#         "turquoise": True,     # 터키석
#         "pearl": True,         # 진주
#         "amber": True,         # 호박
#         "jade": True,          # 제이드(옥)
#         "spinel": True,        # 스피넬
#         "moonstone": True,     # 문스톤
#         "citrine": True,       # 시트린
#         "lapis_lazuli": True,  # 라피스라줄리 (공백 대신 언더바 사용)
#         "black_onyx": True     # 블랙오닉스 (공백 대신 언더바 사용)
# }

# import random

# turn = 1

# chosenJewel = str

# jewelsLists = list(jewels.keys())

# stolenJewels = []

# while True:

#         if True not in jewels.values():
#             print('도둑이 승리하였습니다.')    
#             break  

#         if ThiefAlive == True:
             
#             stoleGem = random.choice(jewelsLists)
#             jewels[stoleGem] = False 
#             print(f" 도둑이 보석 중 하나를 훔쳐갔습니다.") 

#             idx = jewelsLists.index(stoleGem)
#             targetJewel= jewelsLists.pop(idx)
#             stolenJewels.append(targetJewel)  

#              # 여기에 힌트를 넣으면 좋을듯  
   
#             userAnswer = str(input('이번 턴에 도둑이 훔친 보석을 추리하시오.'))

#         elif userAnswer == str(targetJewel):
#              ThiefAlive = False
#              print('도둑이 사망하였습니다.')
#              break
        

#         turn += 1 
# print(turn)
# print(f'지금까지 훔친 보석과 그 순서 {sorted(stolenJewels,reverse = True)}') 

# 정답 : targetJewel 

# (box_choice.py)






# import random


# def thiefSteal(jeweLists, jewelsdict, thiefBag):
#     stoleGem = random.choice(jeweLists)
    
#     jewelsdict[stoleGem] = False 

#     print(f'도둑이 보석 중 하나를 훔쳐갔습니다.') 

#     idx = jeweLists.index(stoleGem)
#     targetJewel = jeweLists.pop(idx)
    
#     thiefBag.append(targetJewel)  
    
#     return targetJewel


# ThiefAlive = True

# jewels = {
#         "diamond": True,       # 다이아몬드
#         "ruby": True,          # 루비
#         "sapphire": True,      # 사파이어
#         "emerald": True,       # 에메랄드
#         "amethyst": True,      # 자수정
#         "topaz": True,         # 토파즈
#         "opal": True,          # 오팔
#         "garnet": True,        # 가넷
#         "aquamarine": True,    # 아쿠아마린
#         "peridot": True,       # 페리도트
#         "tanzanite": True,     # 탄자나이트
#         "turquoise": True,     # 터키석
#         "pearl": True,         # 진주
#         "amber": True,         # 호박
#         "jade": True,          # 제이드(옥)
#         "spinel": True,        # 스피넬
#         "moonstone": True,     # 문스톤
#         "citrine": True,       # 시트린
#         "lapis_lazuli": True,  # 라피스라줄리 (공백 대신 언더바 사용)
#         "black_onyx": True     # 블랙오닉스 (공백 대신 언더바 사용)
# }

# turn = 1
# jewelsLists = list(jewels.keys())
# stolenJewels = [] 

# while True:
#     if True not in jewels.values():
#         print('도둑이 승리하였습니다! 모든 보석이 털렸습니다.')    
#         break  

#     if ThiefAlive == True:
        
#         # 여기에 힌트를 넣으면 좋을듯    

#         targetJewel = thiefSteal(jewelsLists, jewels, stolenJewels)
    
#         userAnswer = input('이번 턴에 도둑이 훔친 보석을 추리하시오. ')

#         if userAnswer == str(targetJewel):
#             ThiefAlive = False
#             print('체포 성공! 도둑이 잡혔습니다.')
#             break
#         else:
#             print('틀렸습니다! 도둑이 도망갔습니다.')

#     turn += 1 

# print(f'턴 수: {turn}턴')
# print(f'훔친 보석과 순서: {sorted(stolenJewels, reverse=True)}')

# ----------------------------------------------------------------------------------------------------

