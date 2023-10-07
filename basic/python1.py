# 1. 기본 데이터와 변수
# 기본 데이터: 숫자, 문자, 참거짓
# 기본 데이터는 서로 연산을 할 수 있다


# 2. 변수라는 상자에 데이터를 담아서 사용한다
# 변수를 쓰는 방법은 3가지가 있다
# 변수 이름은 아무거나 지어도 된다
# my_name / myName / MyName
# 파이썬은 my_name 방식을 선호한다


# 변수와 데이터 예시
name1 = "김세언"
age1 = 21
gender1 = "여성"
name2 = "김서연"
age2 = 24
gender2 = "여성"
#money = True : money 라는 변수에 True라는 값을 담음

# 3. 주의할 연산자
# 오른쪽의 값을 왼쪽의 변수에 대입: =
# 같다: ==
# 다르다: !=
# 작거나 같다: <=
# 크거나 같다: >=
x = 1
x = x + 1
x += 1

# 4. 문자열 포맷팅 - 문자열 중간 부분에 원하는 값 (변수) 을 집어넣고 (삽입) 싶을 때!
print(f"{name1}은 {age1}살이고 {gender1}이고 직업은 학생입니다")
print(f"{name2}은 {age2}살이고 {gender2}이고 직업은 백수입니다")

# 5. 연관성 있는 데이터끼리는 딕셔너리에 잘 응집시켜서 관리하자
# {키: 값}
# 조회, 추가, 변경, 삭제
user1 = {
    "name": "김세언",
    "age": 21,
    "gender": "여성",
}
user2 = {
    "name": "김서연",
    "age": 24,
    "gender": "여성",
}
print(f"{user1.get('name')}은 {user1.get('age')}살이고 {user1.get('gender')}이고 직업은 학생입니다")
print(f"{user2.get('name')}은 {user2.get('age')}살이고 {user2.get('gender')}이고 직업은 백수입니다")

# 6. 데이터가 많아지면 배열에 담아서 관리하자
# []
# 인덱싱, 추가, 변경, 삭제! 여기서의 배열은 users = []
# 배열에서의 첫번째, 두번째, 세번째는 각각 0,1,2임!

users = [user1, user2]
print(f"{users[0].get('name')}은 {users[0].get('age')}살이고 {users[0].get('gender')}이고 직업은 학생입니다")
print(f"{users[1].get('name')}은 {users[1].get('age')}살이고 {users[1].get('gender')}이고 직업은 백수입니다")

user3 = {
    "name": "김도담",
    "age": 29,
    "gender": "수컷",
}
# ex) 추가하기 : 배열.append(추가할 데이터)
users.append(user3)
print(f"{users[2].get('name')}은 {users[2].get('age')}살이고 {users[2].get('gender')}이고 직업은 백수입니다")

# 7. 데이터를 활용해서 논리적인 글을 작성하자

# 7-1. if문 - 조건을 판단하여 해당 조건에 맞는 상황을 수행
# if 조건문 : (조건문은 참과 거짓을 판단하는 문장이다. 이 뒤에는 항상 : 이 붙으니 주의!)
#   수행할 문장
# 주의점 : 들여쓰기 한 부분을 실행한다!
# if elif elif (..) else

# 만약에 user1의 age가 23살 이하이면 => 학생
# 그게 아니면 => 백수
if users[0].get("age") <= 23:
    print("학생")
else:
    print("백수")

# 7-2. 반복문
# 반복문1
# while문 : 조건문이 참인 동안 들여쓰기 한 부분을 반복해서 실행한다.

# 1부터 10까지 출력하라
i = 1
while i <= 10:
    print(i)
    i += 1

# 반복문2
# while 문을 무한 반복하고 싶다면? while True : 수행할 문장
# 특정 상황이 주어졌을 때 반복문을 탈출하고 싶다면? if 특정 상황 : break
# 특정 상황이 주어졌을 때 반복문의 맨 처음으로 돌아가고 싶다면? if 특정 상황 : continue (그 다음 줄은 실행 되지 않는다.)
# 1부터 10까지 출력하라
i = 1
while True:
    print(i)
    # 만약에 i가 10이면 => 반복문을 종료한다
    if i == 10:
        break
    i += 1

# 반복문3: 1부터 10까지 출력하라
# for 변수(구성요소) in 리스트/문자열 : 리스트의 요소가 순서대로 변수에 대입된다
for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(number)

# 숫자 리스트를 자동으로 만들어주는 range 함수 range(a,b) : a 이상 b 미만의 숫자 리스트
# for 변수 in range (a,b) : a 이상 b 미만 의 수가 순서대로 변수에 대입된다
for number in range(1, 11):
    print(number)
