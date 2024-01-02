print("2023년 12월 27일 ~ 2023년 12월 29일 학습내용 첫번째")

"""
사친연산
덧셈, 뺄셈, 곱셈은 정수(Int)로 처리하나다.
그러나 나눗셈은 실수(float)로 처리한다.
"""

a = 30
b = 2
print(a * b) #결과: 60
print(a / b) #결과: 15.0
print(type(a * b)) #<class "int">
print(type(a / b)) #<class 'float'>

print(2 ** 5) #2의 5승. 32
print(32 % 5) #32 나누기 5의 나머지. 2
print(32 // 5) #32 나누기 5의 몫. 6

"""Scientific Notation"""
a =  3 * 10 ** 8 #300,000,000
b =  3e8
print( a == b) #True
print(1e-4) #0.0001

"""
논리연산자와 비교연산자

== : 같다
!= : 같지 않다

"""
print(type(True)) #<class 'bool'">

"""
변수명 이름 짓기 규칙

snake_style : 모든 문자를 소문자로 쓴다. 띄어쓰기는 언더바
camelStyle: 첫문자는 소문자로 시작. 그후 단어마다 대문자. 낙타혹처럼 생김
주의할 것: 변수의 첫 문자는 숫자가 오면 안 됨

"""
"""

변수의 type에 따른 연산 결과 차이와 type 변환방법

"""

num1 = input("숫자를 입력해주세요!! ") #100울 입력
num2 = input("숫자를 입력해주세요!! ") #200을 입력

print(num1, num2)
print(num1 + num2) #300이 아니라 100200 이 출력됨
print(num1 * 3) #300이 아니라 100100100 이 출력됨
print(int(num1)+int(num2)) #int()을 통해서 정수로 변경함
print(int(num1) * 3) #300

#end