"""
로또번호 생성기
조건
1. 숫자는 6개
2. 1부터 45까지
3. 순서는 오름차순
"""

import numpy as np

#방법 1

lottoNum1 = np.random.choice(range(1, 46), 6, replace = False)
lottoNum1.sort()

print(lottoNum1)
print(type(lottoNum1))

#방법 2

lottoNum2 = [] #빈 리스트를 생성
rndNum = np.random.randint(1, 46) #랜덤으로 숫자 하나 뽑기

for i in range(6):#6번 i를 반복함
    while rndNum in lottoNum2:#rndNum이 true이면 아래의 다시 뽑기를 실행. false이면 넘어가고 append 실행
        rndNum = np.random.randint(1, 46) # 다시 뽑기
    lottoNum2.append(rndNum) #리스트의 끝 rndNum을 추가
    
lottoNum2.sort() #i를 6번 거치고 완성된 리스트를 정리해줌

print(lottoNum2)
print(type(lottoNum2))

#방법 2 응용

count = int(input("로또번호를 몇개 생성할까요? ")) #count에 int값을 input함.

def makeLotto(count):
    for i in range(count): #count 만큼 lottoNum3를 생성함
        lottoNum3 = []
        
        for j in range(6):
            rndNum = np.random.randint(1, 46) #rndNum 변수에 리스트 부여
            
            while rndNum in lottoNum3:
                rndNum = np.random.randint(1, 46)
            lottoNum3.append(rndNum)
            
        lottoNum3.sort()

        print("{}. 로또번호: {}".format(i+1, lottoNum3))
        #print(f"{i+1}. 로또번호: {lottoNum3}")

makeLotto(count)