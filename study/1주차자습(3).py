"""
함수의 구조

def 함수명([인자1, 인자2, 인자3, ..., 인자 n]):
    코드 블록
    return 반환
"""
#예시 1
def mySum(a, b):
    c = a + b
    return print(c)

x = 1
y = 2
result = mySum(x, y)

#예시 2
def mySubtract1(a, b=0): #b = None
    c = b - a
    return print(c)

result = mySubtract1(3) 
#함수 자체에 b의 초깃값을 설정하였기 때문에 인수의 개수를 적게 넣어도 오류가 생기지 않는다

