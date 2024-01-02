"""
클래스 선언과 객체 생성

함수와 클래스 비유적 비교
    함수: 각각 덧셈, 뺄셈, 곱셈 등
    클래스: 사칙연산 클래스
    라이브러리: 클래스의 묶음
     예시)수학 라이브러리 = 사칙연산 클래스 + 미분 클래스 + 적분 클래스 (...)
"""

class Calculator:
    def __init__(self): #result값을 초기화하는 메소드
        self.result = 0
     #init이란?
    #객체, 인스턴스 생성할 때 데이터를 초기화하는 메소드
    #__init__()은 반드시 첫 번째 인수로 self를 지정해야 한다.
    
    def add(self, num):
        self.result =  self.result + num
        return self.result
        #init의 초기값, 0을 받고 num을 더함. 그리고 다시 init의 self.result로 결과를 반환한다.


cal1 = Calculator() #인스턴스화
cal2 = Calculator()
cal3 = Calculator()

print(cal1.add(3)) #0+3
print(cal1.add(5)) #3+5
print(cal2.add(10)) #0+10
print(cal3.add(1)) #0+1
print(cal3.add(100)) #1+100

class Bicycle():
    
    def __init__(self, wheelSize, color):
        self.wheelSize = wheelSize #정보 기재
        self.color = color
    
    def stop(self):
        print("자전거({0}, {1}) : 정지".format(self.wheelSize, self.color))

bicycle1 = Bicycle(26, "black") #초기값 세팅
bicycle2 = Bicycle(30, "pink")

bicycle1.stop() #Bicycle 클래스의 stop 메서드를 실행함
bicycle2.stop()

"""
클래스 상속

대분류 > 중분류 > 소분류의 개념

대분류: 동물
    운동성이 있다.
중분류: 포유류
    (운동성이 있다.) 젖을 먹여 새끼를 키운다
중분류: 파충류
    (운동성이 있다.) 비늘로 덮여있다.
"""

class Animal:
    name = "" #Attribute, 클래스 함수 정의

    def move(self):
        print("동물은 운동성이 있다.")

class Mammal(Animal): #클래스 상속, Animal에서 Mammal로 기본기능을 제공함.(name과 move가 상속됨)
    def feed(self):
        print(f"{self.name}은 새끼에게 젖을 먹인다.")

a = Mammal()
a.name = "고양이" #name 메소드에 할당
a.move()
a.feed()

b = Animal
b.name = "이구아나"
b.move()
