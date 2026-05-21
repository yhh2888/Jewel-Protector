import random

# 턴마다 훔치는 것 랜덤으로 지정하는 함수

def thiefSteal(DEV_MOD, jewelsLists, jewelAliveDict, stolenJewels, ThiefAlive):
    if ThiefAlive == True:

        
        stoleJewel = random.choice(jewelsLists)
        idx = jewelsLists.index(stoleJewel)
        targetJewel = jewelsLists[idx]
        stolenJewels.append(targetJewel)  
        
        # 개발자 모드용 출력
        if DEV_MOD == True:
            print(targetJewel)
            for keys in jewelsLists:
                print(keys)
                print(jewelAliveDict[keys], '\n')
            for i in stolenJewels:
                print(i)
        # 여기에 힌트를 넣으면 좋을듯
        
        print(f' 힌트: 이번에 훔쳐갈 보석은 삐리리리 뭐시기 ')
        while True:
            userAnswer = input('이번 턴에 도둑이 훔친 보석을 추리하시오: ')
            
            if (userAnswer == targetJewel) or (userAnswer in jewelsLists):
                break 
            else:
                print('목록에 없거나 오타입니다.\n')

    if userAnswer == str(targetJewel):
        ThiefAlive = False
        
    else:
            print('틀렸습니다! 도둑이 다음 보석을 노립니다.\n')
            jewelAliveDict[stoleJewel] = False 

    return jewelsLists, stolenJewels, ThiefAlive
