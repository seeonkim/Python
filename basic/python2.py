# 함수: y = x + 1

# 함수 정의하기 예시1
def add_one(x):
    x += 1
    return x


# 함수 사용하기 예시1
y = add_one(3)
print(y)

# 함수 정의하기 예시2
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
user3 = {
    "name": "김서연",
    "age": 24,
    "gender": "여성",
}
users = [user1, user2]


def get_job(user):
    if user.get("gender") == "여성":
        if user.get('age') <= 23:
            job = "학생"
        else:
            job = "백수"
    elif user.get("gender") == "남성":
        if user.get('age') <= 25:
            job = "학생"
        else:
            job = "백수"
    else:
        job = "알 수 없음"

    return job


# 함수 사용하기 예시2
print(get_job(users[0]))
