import jewel_box, hint, box_choice
import random
import time

# 메인 루프
 
DEV_MOD = False

MAX_TURNS = 6

def gameStorySetter(jewelNum):
    gameStory = f"1. 스토리  \n\
세계 최고의 보석 박물관 \'루브르 파리\'에 도둑의 예고장이 날아들었습니다. \n\
\'보석함에 보관된 {jewelNum}개의 보석들을 매일 밤 하나씩 훔쳐 가겠다.\' \n\
당신은 박물관의 의뢰를 받은 명탐정이 되어, 매일 밤 도둑의 움직임을 예측하고 \n\
그가 노리는 보석을 지켜내야 합니다! \n\
    \n\n\
2. 시스템 규칙 (Game Rules) \n\
- 박물관에는 총 {jewelNum}개의 진귀한 보석이 보석함(Dictionary)에 보관되어 있습니다. \n\
- 매일 밤, 탐정은 지킬 보석의 영문 이름을 입력하여 잠복수사를 진행합니다. \n\
- 탐정은 수사 전에 보석의 무게와 이니셜레터를 힌트로 제공받습니다.\n\
- 같은 밤, 도둑도 남은 보석 중 하나를 훔치러 슬그머니 접근합니다. \n\
    \n\n\
3. 승리 및 패배 조건 (Win/Lose Conditions) \n\
- [승리] 탐정이 선택한 보석과 도둑이 노린 보석이 일치하면, 현장에서 도둑을 체포합니다. \n\
- [패배] 루팡을 잡지 못해 박물관의 보석 {MAX_TURNS}개를 도난당하면 탐정의 패배입니다. \n\
   \n\n"
   
    print(gameStory)
    time.sleep(1)

ThiefAlive = True
while True:
    jewelNum = int(input(f"플레이할 게임의 보석 수를 입력하세요. ({MAX_TURNS-1}~50개): "))
    if (jewelNum < MAX_TURNS) or (jewelNum > 50):
        print(f"보석의 수는 {MAX_TURNS-1}~20개여야 합니다. 다시 입력하세요.")
    else:
        break

gameStorySetter(jewelNum)

jewelBoxDict = jewel_box.choice(jewelNum)
jewelAliveDict = {}
for keys in jewelBoxDict.keys():
    jewelAliveDict[keys] = True

stolenJewels = []
turns = 1

while ThiefAlive:
    print(f'턴 수: {turns}턴')
    print(f'훔쳐진 보석 목록: {stolenJewels}')
    jewelsLists, stolenJewels, ThiefAlive = box_choice.thiefSteal(DEV_MOD, jewelBoxDict, jewelAliveDict, stolenJewels, ThiefAlive)
    turns += 1
    if ThiefAlive == False:
        print('체포 성공! 도둑이 잡혔습니다.\n')
    elif turns >= MAX_TURNS:
        print(f'도둑이 승리하였습니다. 보석이 {turns-1}회 털렸습니다.\n')
        ThiefAlive = False
