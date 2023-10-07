if __name__ == "__main__":
    while True:
        name = input("유저의 이름을 알려주세요: ")
        if name == 'exit':
            exit()
        gender = input("유저의 성을 알려주세요: ")
        age = input("유저의 나이를 알려주세요: ")
        user_file_writer('users.txt', f"{name} {gender} {age}")
        content = user_file_reader('users.txt')
        print("[현재 직원]")
        print(content)
