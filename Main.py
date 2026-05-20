import jewel_box, hint, box_choice
import random

# 메인 루프


gameStory = "1. 스토리 배경 (Story Background) \n\
   세계 최고의 보석 박물관 \'루브르 파리\'에 괴도 루팡의 예고장이 날아들었습니다. \n\
   \'보석함에 보관된 N개의 전설적인 보석을 매일 밤 하나씩 훔쳐 가겠다.\' \n\
   당신은 박물관의 의뢰를 받은 명탐정이 되어, 매일 밤 루팡의 움직임을 예측하고 \n\
   그가 노리는 보석을 지켜내야 합니다! \n\
\n\n\
2. 등장인물 (Characters) \n\
   - 명탐정 (Player): 루팡의 심리를 예측하여 보석함 중 하나를 선택해 잠복합니다. \n\
   - 괴도 루팡 (AI): 매일 밤 남은 보석 중 하나를 무작위로 타겟팅하여 훔치려고 합니다. \n\
\n\n\
3. 시스템 규칙 (Game Rules) \n\
   - 박물관에는 총 N개의 진귀한 보석이 보석함(Dictionary)에 보관되어 있습니다. \n\
   - 매일 밤, 탐정은 지킬 보석의 영문 이름을 입력합니다. \n\
   - 같은 밤, 루팡도 남은 보석 중 하나를 훔치러 슬그머니 접근합니다. \n\
\n\n\
4. 승리 및 패배 조건 (Win/Lose Conditions) \n\
   - [승리] 탐정이 선택한 보석과 루팡이 노린 보석이 일치하면, 현장에서 루팡을 체포합니다. \n\
   - [패배] 루팡을 잡지 못해 박물관의 모든 보석(N개)을 도난당하면 탐정의 패배입니다. "

print(gameStory)
ThiefAlive = True
jewelNum = int(input("플레이할 게임의 보석 수를 입력하세요. "))

# jewelBoxDict = jewel_box.boxgenerator(jewelNum)

while ThiefAlive:
    # ThiefBoxNum = box_choice(jewelBoxDict)

    # 현재 게임 보석함 딕셔너리 공개하기
    # print(jewelbox.gonggae())

    # 힌트 공개하기
    # print(hint.hint(jewelBoxDict, ThiefBoxNum))

    # chosenBoxNum = int(input("감시할 보관함을 선택하세요"))
    # if chosenBoxNum == ThiefBoxNum:
    #    print("괴도 루팡을 잡았습니다!")
    #    ThiefAlive = False
    # else:
    #  print("보석을 지키지 못했습니다..")
    pass
