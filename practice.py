print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print('나비')
print("풍선")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

# boolean 자료형
# 참 / 거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))

# 변수
# 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4 #문자가 아니기때문에 "" 필요없음
hobby = "산책"
is_adult = age >=3

print("우리집 "+animal+ "의 이름은 "+name+"예요")
print(name+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
print(name+"는 어른일까요? "+str(is_adult))
# 위 처럼 미리 설정해준다면 바꾸고 싶을때 변수부분만 바꿔서 가능
# + 대신 ,를 사용 할 수도 있다
# 예시) print(name+"는 ",age,"살이며, ",hobby,"을 아주 좋아해요")
# ,를 사용 할 때는 str을 써주지 않는다

# 주석
# #으로 하는 주석도 있지만 어떠한 구간이라던가 전체를 주석처리
# 하고싶을땐 '''으로 한다

# Quiz 1
# 변수명 station
# 변수값 사당, 신도림, 인천공항 순서대로 입력
# 출력문장 XX행 열차가 들어오고 있습니다
station = "사당"
print(station,"행 열차가 들어오고 있습니다")

#연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(5//3) # 몫 1

print(10>3) # True

print(3==3) # 등호 앞뒤가 똑같은지 = True
print(4 == 2) #False
print(3+4==7) # True

print(1 != 3) # 등호 앞뒤가 같지않다 = True
print(not(1 != 3)) # 1은 3과 같지않다 의 반대
print((3>0) and (3<5)) # 앞뒤의 조건이 모두 충족해야함 = True
print((3<0) & (3<5)) # 위의 and 와 같은 말
print((3>0) or (3>5)) # 앞뒤의 조건 둘 중 하나만 맞으면 됨 = True
print((3>0) | (3>5)) # 위의 or과 같은말

number = 2 + 3 * 4 # 14
print(number) # 14
number = number + 2 # 16
print(number) # 16
number += 2 # number = number + 2와 완전히 같은말 18
print(number) # 18
number *= 2 # 36
print(number)
number %= 2 # 0
print(number)

#숫자처리함수
print(abs(-5)) # -5의 절대값 = 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 이 숫자들중 가장 큰 수 12
print(min(5, 12)) # 이 숫자들 중 가장 작은 수 5
print(round(3.14))  # 반올림 한 수 3
print(round(4.99)) # 5

from ipaddress import NetmaskValueError
from math import * # math 라이브러리 안에 있는 모든것을 이용하겠다
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

#랜덤함수(난수)
from random import *

print(random()) # 0.0 ~ 1.0 사이의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 사이의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 사이의 임의의 정수값만 생성
print(int(random() * 10) + 1) # 1~10 사이의 임의이 정수값 생성

print(int(random() * 45) + 1)
# 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46))
# 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45))
# 1~ 45 이하의 임의의 값 생성

# Quiz 2
# 월 4회, 3번 온라인, 1번 오프라인
# 조건1 : 랜덤으로 날짜 뽑기
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로
# 조건3 : 매월 1~3일은 제외
# 출력문 : 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 ",date, "일로 선정되었습니다")

#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
""" 
print(sentence3)

#슬라이싱 (원하는 구간의 값만 가져올 때)
jumin = "990129-1234567"

print("성별 : " + jumin[7]) # 7번째의 값만 가져옴 = 1
print("연 : " + jumin[0:2]) # 0부터 2 직전까지의 값을 다 가져옴 = 99
print("월 : " + jumin[2:4]) # 01
print("일 : " + jumin[4:6]) # 20
print("생년월일 : " + jumin[:6]) #처음부터 6 직전까지 값을 다 가져옴 = 990120
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지 = 1234567
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])
# 7번째부터 맨뒤까지를 뒤에서부터 세고싶을때 출력 = 7654321

#문자열 처리함수
python = "Python is Amazing"
print(python.lower()) # 전부 소문자로 출력
print(python.upper()) # 전부 대문자로 출력
print(python[0].isupper()) # 0번째 문자가 대문자가 맞는지 = True
print(len(python)) # 길이값을 구함
print(python.replace("Python", "Java")) # 특정 문자를 내가 원하는 문자로 바꿈

index = python.index("n") # n 이라는 문자가 몇번째인지 = 5
print(index)
index = python.index("n", index + 1) # 두번째 n의 위치 = 15
print(index)

print(python.find("Java"))
# index와 똑같이 특정 문자의 위치를 찾는건데 현재 변수안에 Jave라는 문자가 없다
# 그러면 값이 -1로 나오는데 만약 find가 아닌 index를 사용했다면
# 출력값이 그냥 오류로 출력. find는 틀리면 -1로 출력

print(python.count("n")) # 변수안에서 n이 몇번 등장하는가 = 2

#문자열 포맷
# 방법 1
print("나는 %d살입니다." % 20) # d는 정수
print("나는 %s을 좋아해요" %"파이쎤") # s는 문자열
print("Apple 은 %c로 시작해요." %"A") # c는 문자
# 하지만 전부 %s로 해도 된다
print("나는 %s살입니다." %20)
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# 0번째 1번째라는 순서이다. 그 순서에 맞는 값을 넣어줄 때 사용
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))
# {}안의 문자에 해당되는 변수를 뒤에 순서에 상관없이 출력한다

# 방법 4 (v3.6 이상~)
age=20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
# 저는 "나도코딩"입니다 를 출력하고 싶다면
print("저는 \"나도코딩\ 입니다.")

# \\ : 문장내에서 \ 한개로 출력
print("C:\\Users\\user\\OneDrive\\바탕 화면\\pythonwork space>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# 커서를 맨앞으로 이동시켜 R부터 Pine이 네글자이니 "Red "까지를 Pine으로 바꿈

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")
# Redd에서 백스페이스를 하면 d 하나가 사라진다

# \t : 탭
print("Red\tApple") # Red   Apple

# Quiz 3
# 비밀번호 생성

# 예) http://naver.com
# 규칙1 : http:// 는 제외
# 규칙2 : 처음 만나는 점(.) 이후 부분 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!' 로 구성
url="http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2
# my_str 변수의 처음부터 '.'의 위치 직전까지만 출력하고 싶기때문에 index로
# '.'의 위치 써줌. my_str[0:5]와 같은 말
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# len(my_str)과 my_str.count("e")는 str로 감싸준다
print("{0}의 비밀번호는 {1}입니다".format(url, password))

