import jewel_box, hint, box_choice
import random
import time

DEV_MOD = False

MAX_TURNS = 6
MAX_JEWELS = 50

def gameStorySetter(jewelNum):
   gameRule = ["1. 게임규칙 (Game Rules) \n",
   f"- 박물관에는 총 {jewelNum}개의 진귀한 보석이 보석함(Dictionary)에 보관되어 있습니다. \n",
   "- 매 턴마다, 탐정은 \033[1m\033[32m보석의 이름을 입력해\033[0m\033[0m 수사를 진행합니다. \n",
   "- 수사 전, 도둑이 훔칠 보석의 \033[1m\033[33m무게 / 이름 내의 랜덤 글자\033[0m를 힌트로 제공받습니다.\n",
   "- \033[1m\033[31m그 후, 도둑은 보석을 훔치러 슬그머니 접근합니다.\033[0m\033[0m \n",
   "- 탐정이 선택한 보석과 도둑이 노린 보석이 \033[1m\033[32m일치하면, 현장에서 도둑을 체포합니다.\033[0m\033[0m \n",
   "- 도둑을 잡지 못하면 \033[1m\033[31m보석은 사라지고,\033[0m\033[0m 다음 턴으로 넘어가 다시 다른 보석을 훔치러 옵니다. \n",
   f"- 도둑을 잡지 못해 박물관의 보석 {MAX_TURNS-1}개를 도난당하면 탐정의 패배입니다. \n",
   "\n"]
   while True:
       skipYesOrNo = input("게임규칙 설명을 스킵하시겠습니까? (Y/N): ")
       if skipYesOrNo == 'Y' or skipYesOrNo == 'y':
           break
       elif skipYesOrNo == 'N' or skipYesOrNo == 'n':
           for sentence in gameRule:
               print(sentence)
               time.sleep(3)
           break

while True:
    jewelNum = int(input(f"플레이할 게임의 보석 수를 입력하세요. ({MAX_TURNS-1}~{MAX_JEWELS}개): "))
    if (jewelNum < MAX_TURNS) or (jewelNum > 50):
        print(f"보석의 수는 {MAX_TURNS-1}~{MAX_JEWELS}개여야 합니다. 다시 입력하세요.")
    else:
        print('\n')
        break

gameStorySetter(jewelNum)

jewelBoxDict = jewel_box.choice(jewelNum)
jewelAliveDict = {}
for keys in jewelBoxDict.keys():
    jewelAliveDict[keys] = True

stolenJewels = []
turns = 1

ThiefAlive = True

while ThiefAlive:
    print('\n'+'-'*45)
    print(f'턴 수: {turns}턴')
    print(f'사라진 보석 목록: {stolenJewels}')
    jewelsLists, stolenJewels, ThiefAlive = box_choice.thiefSteal(DEV_MOD, jewelBoxDict, jewelAliveDict, stolenJewels, ThiefAlive)
    turns += 1
    if ThiefAlive == False:
        print('체포 성공! 도둑이 잡혔습니다.\n')
    elif turns >= MAX_TURNS:
        print(f'도둑이 승리하였습니다. 보석이 {turns-1}회 털렸습니다.\n')
        ThiefAlive = False
