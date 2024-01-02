"""
시퀀스 자료형

정의: 
값이 연속적으로 이어진 자료형
list, tuple, range, 문자열(string), byte, bytearray가 있다.

시퀀스 자료형으로 만든 객체는 시퀀스 객체라고 하며 시퀀스 객체에 들어있는 각 값은 요소, element라고 부른다.
"""

#시퀀스 객체 안에 특정 값이 있는지 확인하기
exList0 = [0, 10, 20, 30, 40, 50]
a = 30 in exList0 #True
b = 100 in exList0 #False
print(a)
print(b)

#tuple, range, string에도 똑같이 적용됨
print(10 in range(10)) #False

#시퀀스 객체 연결하기
exList1 = ["아메리카노", "카페라떼", "카푸치노"]
print(exList0 + exList1)

#range는 + 연산자를 활용해서 연결이 불가능하다.
#그러므로 list나 tuple로 만들어서 연결하면 된다.

print(tuple(range(10)) + tuple(range(10,20))) 
#(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

#문자열 객체 연결하기
#문자열과 문자열도 연결이 가능하다. 정수, 실수와 연결할려면 숫자를 string으로 바꾸고 연결해야 한다.

exStr = "내년은 " + str(2024) + "년입니다."
print(exStr) #내년은 2024년입니다.

#시퀀스 객체 반복하기
#range는 자체적으로 반복이 불가능하므로 + 연산자처럼 list나 tuple로 바꾸고 변환해줘야 한다.

print(list(range(5)) * 3)

"""
len()함수
list, tuple: 요소 개수
range: 숫자 생성 개수
string: 문자열의 길이, 문자의개수, 문자열의 길이에는 공백까지 포함된다.
"""
print(len(exList1)) #3
print(len(range(10))) #10
print(len(exStr)) #13

"""
인덱스 사용하기
시퀀스 객체 안의 요소에 접근하는 방법.
list[], tuple[], range[], string[] 으로 [] 안의 인덱스를 출력한다.
이때 인덱스는 range와 마찬가지로 1이 아닌 0부터 시작한다.
즉 tuple 객체의 첫번째 요소를 가져올려면 tuple[1]이 아닌 tuple[0]을 해야 한다.
"""
print(exList1[0]) #아메리카노
print(range(10)[2]) #2
print(exStr[4]) #2. 문자열의 공백까지 포함해서 인덱스 위치를 따짐

#음수 인덱스를 사용하면 뒤에서부터 요소를 접근한다.
print(exList1[-1]) #카푸치노

#len()을 활용해서 인덱스의 마지막 요소에 접근하기
#len()함수의 출력값은 문자열의 길이이다. 
#그러나 인덱스는 1이 아닌 0부터 시작하므로 마지막 요소의 인데스 위치는 len()-1 값이다.

#print(exList1[len(exList1)-1]) -> IndexError: list index out of range
print(exList1[len(exList1)-1]) #카푸치노

"""
시퀀스에 값을 할당, 업데이트하기
list의 경우 원하는 인덱스 위치에 새로운 값을 업데이트할 수 있다.
tuple, range, 문자열은 읽기 전용이라 안 된다.
"""
exList2 = [0, 0, 0, 0]
exList2[0] = 1
exList2[1] = "two"
exList2[2] = True
exList2[3] = 4
print(exList2) #[1, 'two', True, 4]

"""
del로 요소 삭제하기
list의 경우 원하는 인덱스 위치의 요소를 삭제할 수 있다.
tuple, range, 문자열은 읽기 전용이라 안 된다.
"""
del exList2[0]
print(exList2) #['two', True, 4]
print(exList2[0]) #two가 출력. 새로운 0번째 요소가 됨

"""
슬라이스를 이용하여 시퀀스 객체의 일부를 잘라내 새로운 시퀀스를 만들 수 있다.
list[0, 10] -> 0번재 인덱스 요소부터 9번째 인덱스 요소를 잘라서 새 리스트를 생성. 10번째 인덱스는 포함하지 않는다.
"""
exList3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exTuple3 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
exRange3 = range(11)
exStr3 = "Hello World!"

print(exList3[2:5]) #[2, 3, 4]. 2번째 인덱스 이상, 5번째 인덱스 미만.
print(exList3[:11]) #list 전체를 가져올려면 존재하지 않는 11번째 인덱스까지 슬라이스해야 한다.
print(exList3[4:-3]) #[4, 5, 6, 7]. 4번째에서 -4번째(-3-1번째)요소를 슬라이스함
print(exList3[4:-8]) #[]. 4번째에서 -9번째 요소를 가져오면 아무것도 가져오지 못 한다.

print(exTuple3[:11]) #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(exRange3[4:-3]) #range(4,8)이 출력
print(exStr3[0:7]) #Hello W

"""
인덱스 증가폭 설정하기
시퀀스[시작할 인덱스:끝 낼 인덱스+1:증가폭]
"""
print(exList3[2:11:3]) #인덱스 2부터 3씩 증가하여 인덱스 10(11-1)까지 슬라이스
#[2, 5, 8]가 출력됨. 2, 2+3, 2+3+3
print(exList3[2::3])#[2, 5, 8] 출력. 시작과 끝 인덱스는 생략할 수 있다.

print(exTuple3[2:11:2]) #(2, 4, 6, 8, 10)
print(exRange3[2:11:2]) #range(2, 11, 2)
print(exStr3[2:len(exStr3):2])#loWrd. len(exStr3)을 끝 인덱스로 잡아서 문자열 전체를 범위로 함

"""
슬라이스에 새로운 값을 할당하고 del을 이용해 삭제 가능하다.
그러나 range, tuple, 문자열은 슬라이스는 가능해도 값 할당과 del은 불가능하다.
"""
exList3[2:5] = ["아메리카노", "카페라떼", "카푸치노"]
print(exList3) #[0, 1, '아메리카노, 카페라떼', '카푸치노', 5, 6, 7, 8, 9, 10]

exList3[2:5] = [2, 3]  #업데이트할 요소가 범위보다 작으면 리스트의 요소 개수가 줄면서 업데이트된다.
print(exList3) #[0, 1, 2, 3, 6, 7, 8, 9, 10]

exList3[2:5] = ["new2", "new3", "new4", "new5", "new6"] #업데이트할 요소가 범위보다 크면 리스트의 요소 개수가 늘면서 업데이트된다.
print(exList3) #[0, 1, 'new2', 'new3', 'new4', 'new5', 'new6', 7, 8, 9, 10]

exList3[2:11:3] = ["아메리카노", "카페라떼", "카푸치노"]
print(exList3) #[0, 1, '아메리카노', 'new3', 'new4', '카페라떼', 'new6', 6, '카푸치노', 8, 9, 10]
#이때 슬라이스 범위의 요소 개수와 할당할 요소 개수가 정확히 일치해야 한다.
#일치하지 않으면 다음과 같은 에러 메세지가 뜬다. (예시)
#ValueError: attempt to assign sequence of size 2 to extended slice of size 3

del exList3[2:11:3]
print(exList3) #[0, 1, 'new3', 'new4', 'new6', 6, 8, 9, 10]