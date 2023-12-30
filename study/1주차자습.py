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

"""논리연산자와 비교연산자

== : 같다
!= : 같지 않다

"""
print(type(True)) #<class 'bool'">

"""변수명 이름 짓기 규칙


"""