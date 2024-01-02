
print("2023년 12월 27일 ~ 2023년 12월 29일 학습내용 두번째")

"""
list 자료형
"""
exList = [0, 1, 2, 3, 4, 5] #리스트의 첫번째 항목의 위치는 0번째이다.

#인덱싱
print(exList[0]) #exList의 0번째 위치의 항목을 출력한다.
print(exList[5] == exList[-1]) #True

testList = ["다양한", 0, 1, 2, "타입의", True, exList, "하나의 리스트에"]
print(testList)

#업데이트
testList[-2] = "타입의 항목이" #-2위치의 항목인 exList가 
testListNew = testList + exList #리스트 이어붙이기

print(exList * 3) 
#리스트 반복 [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
print(testListNew)
print(testListNew[0][2]) #0번째의 3번째를 추출

#슬라이싱
print(exList[0:3]) #0번째 위치 이상, 3번째 위치 미만
print(exList[4:]) #4번째부터 전부
print(exList[:4]) #4번째 위치 미만까지
print(exList[:]) #전부
print(testListNew[1::2]) #1번째 위치부터 2번째 항목들을 출력

"""
tuple 자료형

list와 다르게 한 번 입력하면 수정할 수 없다.
list 같은 컬렉션으로써 크게 의미가 없다.

tuple을 사용하는 이유
1. list보다 가볍기 때문이다.
2. 문법적 편의성이 좋다.
"""

exTuple = (0, 1, 2, 3, 4, 5)
print(exList)
print(exTuple)

#exList[0] = 30 같은 인덱싱이 불가능하다.
del exList[-1]
print(exList)
#del exTuple[-1] 불가능

#tuple은 괄호를 생략할 수 있다.

exTuple2 = 0, 1, 2, 3, 4
print(exTuple2)
print(type(exTuple2))

"""
함수 split("*")
문자열을 "*"을 기준으로 리스트형태로 나누는 함수
"""
exSplit = "a, b, c, d".split(",")
print(exSplit) #['a', ' b', ' c', ' d']

coffeeMenuStr = "에스프레소, 아메리카노, 카페라떼, 카푸치노"

print(coffeeMenuStr.split(",")) 
#['에스프레소', ' 아메리카노', ' 카페라떼', ' 카푸치노']
print(coffeeMenuStr.split(" "))
#['에스프레소,', '아메리카노,', '카페라떼,', '카푸치노']
#","을 기준으로 나누면 '에스프레소'
#공백을 기준으로 나누면 '에스프레소,'

#split 응용
phoneNumer = "+82-10-1234-5678"
phoneNumerSplit = phoneNumer.split("-")
print(phoneNumer[0:3])
print(phoneNumerSplit[0])
#둘 다 +82가 출력됨

#부분 split
print(phoneNumer.split("-", maxsplit=2))
#"-"일 기준으로 나누고 그 중 2번째 위치의 항목까지만 리스트를 만든다

"""
함수 strip()
문자열의 지정한 선행문자와 후행문자를 제거하는 함수
"""
textStrip0 = "abcddcbaREAL TEXTbbbaaa"
print(textStrip0.strip("a")) #bcdabcdREALTEXTbbb
#선행문자에서 a 하나 지우고 b에 막혀서 나머지 a는 제거 실패함
print(textStrip0.strip("abcd")) #REALTEXT
#stip("")에서 ""에 제거할 문자를 입력하면 문자열에 실제로 적힌 순서와 무관하게 모두 제거됨

print(textStrip0.lstrip("abcd")) #선행문자만 제거
print(textStrip0.rstrip(" TEXTab")) #후행문자만 제거. 공백도 제거 가능

"""
함수 join()
문자열 연결

(문자열 + 문자열) 연산자와 다르게 list 안의 문자열을 연결시킬 수 있음 
"""
addressList = ["서울시", "서초구", "반포대로", "201(반포동)"]

print(" ".join(addressList)) #리스트 항목들을 연결하되 중간 중간 공백을 넣는다.
a = "//"
print(a.join(addressList)) #서울시//서초구//반포대로//201(반포동)

"""
함수 find()
문자열 내 찾고자 하는 문자의 시작 위치값을 반환함
만약 찾는 문자가 없는 -1을 반환한다.
"""
exStr = "Python is easy to learn. Python is great way to code. Python!!"

print(exStr.find("Python"))
print(exStr.find("great"))
print(exStr.find("Java"))

"""
함수 count()
찾고자 하는 문자열의 개수를 반환함.
만약 찾을 문자가 없으면 0을 반환한다.
"""
print(exStr.count("Python"))
print(exStr.count("Java"))

"""
함수 startswith(), endswith
함수 replace
"""

print(exStr.startswith("Python")) #True
print(exStr.endswith("Python!!"))
print(exStr.replace("Python", "Java"))

"""
list 관련 함수
append() : 새로운 요소를 리스트 마지막에 추가. 하나의 요소만 추가 가능
extend() : 새로운 요소들을 리스트 마지막에 추가. append와 비교 필요.
insert(i, element) : 인덱스 i에 element 추가
"""
exList2 = [0, 1, 2, 3, 4, 5]
exList2.append(6)
print(exList2)

#append와 extend 구분
exList2.append([7, 8, 9, 10]) 
print(exList2) #[0, 1, 2, 3, 4, 5, 6, [7, 8, 9, 10]]
del exList2[7]

exList2.extend([7, 8, 9, 10])
print(exList2)

exList3 = ["a", "b", "c", "d"]
exList3.insert(2, "알파벳입니다.")
print(exList3)

"""
insert 관련 메모
"""
# 음수 인덱스 삽입
exList3 = ["a", "b", "c", "d"]
exList3.insert(-1, "f")
exList3.insert(-2, "e")
print(exList3) 
# ['a', 'b', 'c', 'e', 'f', 'd'] 가 출력
# 음수 인덱스를 쓰면 맨 뒤에서부터 insert하지 않는다!

# 건너 뛰어서 인덱스 삽입
exList3 = [0, 1, 2, 3]
exList3.insert(5, 5) 
print(exList3) #[0, 1, 2, 3, 5]
# print(exList3[5]) -> IndexError: list index out of range
print(exList3[4])
# 인덱스 4를 건너뛰고 인덱스 5에 insert를 했으나 인덱스 4에 insert됨

#end