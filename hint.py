import jewel_box
import random

# jewel_box에서 받은 딕셔너리로 힌트를 만듭니다.

def setCriminal():

 targetJewel = random.choice(jewel_box)
 return targetJewel

targetJewel = setCriminal()

count = 0

def detectiveGuess():


 if '유저가 말하는값' == jewel_box:
   print(f'탐정이 승리 하였습니다.')
 else:
   global count
   count += 1
   print(f'현재 {count}번 틀렸습니다.')

   if count >= 5:
     print(f'탐정이 패배 하엿습니다.')
     print(f'도둑이 {targetJewel}를 훔쳐 달아났습니다.!.')
     
playerGuess = detectiveGuess()

