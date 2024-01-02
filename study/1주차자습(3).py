"""
함수의 구조

def 함수명([인자1, 인자2, 인자3, ..., 인자 n]):
    코드 블록
    return 반환
"""
#예시 1
def mySum1(a, b):
    c = a + b
    return print(c)

x = 1
y = 2
result = mySum1(x, y)

#예시 1 - 1
def mySum1(a, b):
    c = a + b
    print(c) #print로 함수를 끝낼거면 return을 할 필요없음

x = 1
y = 2
result = mySum1(x, y)

#예시 2
def mySubtract1(a, b=0): #b = None
    c = b - a
    return print(c)

result = mySubtract1(3) 
#함수 자체에 b의 초깃값을 설정하였기 때문에 인수의 개수를 적게 넣어도 오류가 생기지 않는다
result = mySubtract1(10, 100) #b가 100으로 새로 정의됨


#return이 필요한 메서드와 필요없는 메서드

def myFunc():
    print("My first fuction")
    print("This is new fuction")
myFunc() #return이 없지만 결과가 출력이 됨

def mySum2(a, b):
    c = a + b
    print(f"{c}이/가 출력 되어야 함")

x = 1
y = 2
result = mySum2(x, y)
print(result) #None이 출력됨. 왜냐하면 반환값이 없기 때문이다.

"""
myFunc는 문장을 출력하는 기능이 전부이다. 그래서 특별히 무언가를 반환할 필요는 없다.
mySum2는 c 를 계산하는 기능이다. 그런데 특별히 c를 반환하여 메서드 결과를 확정시켜주지 않으면 향후 메서드 결과를 출력할 수 없다. 
"""
#올바른 형태
def mySum2New(a, b):
    c = a + b
    print(f"{c}이/가 출력 되어야 함")
    return c

x = 1
y = 2
result = mySum2New(x, y)
print(result)

"""
변수의 유효범위

지역 변수(Local Variable)과 전역 변수(Global Variable)
"""
a = 5 #global

def func1():
    a = 1 #local
    print(f"func1() 지역 변수 a = {a}")

func1()
print(f"전역 변수 a = {a}")
print(a + 1)

#출력결과물
#func() 지역 변수 a = 1
#전역 변수 a = 5
#6

"""
해설
지역 변수 "a"는 밖으로 나오지 않고 함수 내부에서만 영향을 미친다.
전역 변수 a는 func를 패스하고 코드 전체에 영향을 미친다.
"""

a = 5 #global

def func2():
    print(f"func2() 지역 변수 a = {a}")

func2()
print(f"func1() 전역 변수 a = {a}")
"""
해설
함수 내부에서 a를 정의하지 않아서 전역 변수가 함수 내부까지 영향을 미치고 있다.
"""

a = 5 #global

def func1():
    a = 1 #local
    print(f"func1() 지역 변수 a = {a}")

def func2():
    a = 2 #local
    print(f"func2() 지역 변수 a = {a}")

def func3(): #함수 내부에서 전역 변수 지정
    print(f"func2() 전역 변수 a = {a}")

def func4():
    global a
    a = 100 #함수 내부에서 전역 변수를 변경함
    print(f"func2() 새로운 전역 변수 a = {a}")

func1()
func2()
func3()
print(f"전역 변수 a = {a}")
func4()
print(f"전역 변수 a = {a}")
func3() #func4()를 실행하고 func3()를 실행하면 이제 a = 100이 나온다.

"""
lambda 함수
def 함수는 복잡한 함수 로직을 만들 때 주로 사용함
lambbda 함수는 단순 기능을 수행할 때만 사용함
함수를 1줄로 처리 가능
(lambda 매개변수 : 매개변수를 활용한 코드)(원하는 매개변수 입력)
"""

lambdaResult = (lambda x : x ** 2)(3)

def myPower(x):
    y = x ** 2
    return y
defResult = myPower(3)

print(lambdaResult == defResult)

mySquare = lambda x : x ** 2
print(mySquare(4))

#end