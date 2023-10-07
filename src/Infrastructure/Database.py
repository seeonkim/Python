import csv
import os
import platform


class Database(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.root_dir = os.getcwd() + '/Data'

    def read_data_in_csv_file(self, file_name):
        content = []
        file_reader = open(f"{self.root_dir}/{file_name}", 'r', encoding="utf-8")
        csv_file_reader = csv.reader(file_reader)
        for row in csv_file_reader:
            if len(row) == 0:
                continue
            content.append(row)
        return content[1:]

    def add_data_in_csv_file(self, file_name, row):
        file_writer = open(f"{self.root_dir}/{file_name}", 'a', encoding="utf-8", newline="\n")
        csv_file_writer = csv.writer(file_writer)
        csv_file_writer.writerow(row)
        file_writer.close()

    def update_data_in_csv_file(self, file_name, row):
        all_rows = self.read_data_in_csv_file('users.csv')
        for i in range(len(all_rows)):
            findrow = all_rows[i]
            if row[0] == findrow[0]:
                all_rows[i] = row
        file_writer = open(f"{self.root_dir}/{file_name}", 'w', encoding="utf-8", newline="\n")
        csv_file_writer = csv.writer(file_writer)
        csv_file_writer.writerow(all_rows)
        file_writer.close()

if __name__ == "__main__":
    db = Database()
    db.update_data_in_csv_file('users.csv', ['asd@asd.com, asd, aaa, 3, seller'])


    #db의 update 함수를 보완하려고 함!
    #일단 이미 있는 걸 다 읽고, 이메일이 같은 줄을 발견하면 그 줄을 입력한 새 줄로 변경한다
    #새로운 모든 줄을 파일에 다시 작성한다
    #이때 기둥 (인스턴스변수들도 다 사라지기 때문에, row랑 그걸 합쳐야 한다..)
    #get_columns(self, file_name)-- 0번째 줄을 긁어와서 그걸 기둥이라 하자.
    #기둥+새로운 모든 줄을 통째로 writerow 해야 할듯
    #[columns] + [row]