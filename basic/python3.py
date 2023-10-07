import csv

# 정의 코드를 여기에 적어주세요

if __name__ == "__main__":
    # 실행 코드를 여기에 적어주세요

    # 1. csv 파일 쓰기, input
    user_file_writer = open('buyer.csv', 'w', encoding="utf-8", newline="\n")
    user_csv_file_writer = csv.writer(user_file_writer)
    while True:
        name = input("이름을 알려주세요: ")
        if name == "exit":
            user_file_writer.close()
            break
        age = input("나이를 알려주세요: ")
        gender = input("성별을 알려주세요: ")
        user_csv_file_writer.writerow([name, age, gender])

    # 2. csv 파일 읽기
    user_file_reader = open('buyer.csv', 'r', encoding="utf-8")
    user_csv_file_reader = csv.reader(user_file_reader)
    for line in user_csv_file_reader:
        print(line)
    user_file_reader.close()
