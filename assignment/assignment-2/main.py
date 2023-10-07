#문제 복습하기~~~~~~~~~~~~~~~~~~~~~~~응용연습을하자~(1,2,3)
import random
from users_data import write_csv_file, read_csv_file

users = [{
    "name": "김세언",
    "age": 21,
    "gender": "여성"
}, {
    "name": "이바람",
    "age": 22,
    "gender": "남성"
}, {
    "name": "신네모",
    "age": 23,
    "gender": "남성"
}, {
    "name": "김동그라미",
    "age": 24,
    "gender": "여성"
}, {
    "name": "민수빈",
    "age": 25,
    "gender": "여성"
}, {
    "name": "김수빈",
    "age": 25,
    "gender": "여성"
}, {
    "name": "채수빈",
    "age": 25,
    "gender": "여성"
}, {
    "name": "문가람",
    "age": 25,
    "gender": "여성"
}]


# 유저중에서 랜덤으로 3명의 여성을 뽑아주세요
# 질문-중복으로 뽑히는데 어떡하죠..? 들여쓰기 문제..?
# 출력은 돠는데 줄바꾸기 엔터도 같이 출력됨....
def pick_random_three_users(users):
    users_list = []
    while True:
        random_index = random.randint(0, 7)
        find_same_name = False
        for user in users_list:
            if user.get('name') == users[random_index].get('name'):
                find_same_name = True
        if find_same_name == True:
            continue
        users_list.append(users[random_index])
        if len(users_list) == 3:
            break
    return users_list


def convert_dictionary_to_list(dictionary):
    return list(dictionary.values())


if __name__ == "__main__":
    users_list = pick_random_three_users(users)
    print(users_list)
    for user in users_list:
        row = convert_dictionary_to_list(user)
        write_csv_file('random_users.csv', row)