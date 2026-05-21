import jewel_box
import random

# jewel_box에서 받은 딕셔너리로 힌트를 만듭니다.

def weightHint(weight : float) :
    if int(game_jewels[stoleJewel]) < weight:
        print(f'{stoleJewel}는 {weight}g 미만입니다.')
    else :
        print(f'{stoleJewel}는 {weight}g이상입니다.')

def randLetterHint(name):
    hint = random.choice(name)
    print(f'글자힌트: {hint}')