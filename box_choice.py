
# # 턴마다 훔치는 것 랜덤으로 지정하는 함수

import random
from hint import *


def thiefSteal(DEV_MOD, jewelsDict, jewelAliveDict, stolenJewels, ThiefAlive):
    if ThiefAlive == True:

        jewelsLists = list(jewelsDict.keys())

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
        
        print("-"*45)
        weightHint(jewelsDict[targetJewel], 50)
        randLetterHint(stoleJewel)
        print("-"*45)

        while True:
            userAnswer = input('이번 턴에 도둑이 훔친 보석을 추리하시오: ')
            if (userAnswer == targetJewel) or (userAnswer in jewelsLists):
                break 
            else:
                print('목록에 없거나 오타입니다.\n')

        if userAnswer == str(targetJewel):
            ThiefAlive = False
        else:
            print("\n"+"-"*45)
            print('틀렸습니다! 도둑이 다음 보석을 노립니다.\n')
            print("-"*45)
            jewelAliveDict[stoleJewel] = False

    return jewelsLists, stolenJewels, ThiefAlive


