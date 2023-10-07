# 과제
# users.txt 파일을 만드세요

# users_data.py 파일을 만들고 users.txt 파일을 쓸 수 있는 함수와 읽을 수 있는 함수를 만드세요
# users.txt 파일을 쓸 수 있는 함수 (user_file_writer) 는 파라미터로 읽고 싶은 파일의 이름과 쓰고 싶은 내용을 받고, 결과로 None을 리턴합니다 (None을 리턴하는 것은, 아무 결과도 리턴하지 않는 것과 같음)
# users.txt 파일을 읽을 수 있는 함수 (user_file_reader) 는 파라미터로 읽고 싶은 파일의 이름을 받고, 결과로 읽은 파일 내용을 배열로 리턴합니다

# 현재 파일에서 users_data.py의 함수들을 가져와서 사용하세요 (from, import를 사용하세요)
# 질문-사용하라고 해서 가져온다고는 했는데, none을 리턴하는 함수를 쓰면 자꾸 에러가 나서 쓸 수가 없었음. 어떻게 사용해야 되는지를 잘 모르겠음ㅠㅠ 그래서 그냥 새로 만들어서 썼음
# none을 리턴하는 함수를 잘 작성했는지도 모르겠음

from users_data import user_file_writer
from users_data import user_file_reader

# 현재 파일에서 아래의 유저들을 콘솔에서 입력해서 파일에 추가할 수 있도록 코드를 작성하세요
# 유저의 이름을 입력받을 때, exit를 입력하면 프로그램이 종료되도록 만들어주세요


#k랑 p라는 함수를 새로 만들었음. 뭔가 반복문을 사용해서 5명이 끝나면 그만 이름을 물어보는 코드를 짜고 싶었음. 근데 이름, 나이, 성별만 물어보고 입력하면
# 유저 1명이 추가 될 때마다 유저 목록 모두 출력하는 것 까지 ok, exit 입력하면 꺼지는것도 ok 근데 반복이 안됨.....


# k = open("users.txt", "a", encoding="utf-8")
# name = input("이름을 알려주세요: ")
# if name == "exit":
#         exit()
# age = input("나이를 알려주세요: ")
# gender = input("성별을 알려주세요: ")
# k.write(f"{name} {age} {gender}\n")
# k.close()
#
# # 유저 1명이 추가될 때마다, 현재 유저들의 목록을 전부 출력해주세요 (여기도 readline 이랑 readlines 써보려고 했는데 설명 까먹음 다시 설명 필요)
# p = open("users.txt", "r", encoding="utf-8")
# while True:
#     line = p.readline()
#     if line:
#         print(line, end="")
#     else:
#         break
# if input():
#     lines = p.readlines()
# p.close()
#
# # 하다가 잘 안되면 어떤 것이든 print를 해보고 눈으로 보면서 진행하세요 (....)
# # 추가할 유저 정보
# # 이름 | 성별 | 나이
# # 김세언 | 여성 | 21
# # 김우중 | 남성 | 24
# # 김가영 | 여성 | 23
# # 박진수 | 남성 | 26
# # 이다혜 | 여성 | 24

if __name__ == "__main__" :
    while True:
        name = input("유저의 이름을 알려주세요: ")
        if name == 'exit' :
            exit()
        gender = input("유저의 성을 알려주세요: ")
        age = input("유저의 나이를 알려주세요: ")
        user_file_writer('users.txt', f"{name} {gender} {age}")
        content = user_file_reader('users.txt')
        print("[현재 직원]")
        print(content)

#     i = 0
#     while True:
#         k()
#         if i == 5:
#             break
#         i += 1
