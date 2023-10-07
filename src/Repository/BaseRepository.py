import random
from src.Domain.product import Product
from src.Infrastructure.Database import Database


class BaseRepository(object):
    def __init__(self, file_name):
        self._db = Database()

    #다른 리포지토리에 상속하는 부모 리포지토리인 베이스 리포지토리를 만들었다
    def save(self, domain):
        self._db.update_data_in_csv_file('users.csv', domain.__dict__.values)


    #이 세이브함수는 도메인 객체를 받아 딕셔너리 형태로 변환한다
    #도메인 딕셔너리의 값만 불러오기 위해 domain.__dict__values()를 할 수 있다
    #배열로 바꾸는 작업이 필요하다면 list로 이를 감싼다.
