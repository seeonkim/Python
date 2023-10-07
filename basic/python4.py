if __name__ == "__main__":
    # 예외처리 : 파이썬에서 오류를 처리하는 방법
    # 오류에는 어떤 것들이 있나? FileNotFoundError ZeroDivisionError IndexError
    # try-except문 : try 블록 수행 중 오류가 발생하면 ?=> except 블록 수행
    # try:
    #   ...
    # except [발생오류 [as 오류변수]]:
    #   ...
    # else :
    #   ... 오류가 없을 경우에만 수행)


    # (1) try-except만 쓰는 방법
    try:
        x = int(input("나눌 숫자를 입력하세요: "))
        y = 10 / x
        print(y)
    except:
        print("예외가 발생함")

    # (2) 발생 오류만 포함한 except 문

    try:
        numbers = input("숫자와, 나눌 숫자를 입력해주세요: ")
        string_number_list = numbers.split(" ")

        #string은 문자열, int는 정수

        int_number_list = []
        for string_number in string_number_list:
            #stringnumberlist의 문자열이 stringnumber라는 변수에 차례대로 대입된다
            int_number_list.append(int(string_number))
            #stringnumber를 정수화해서 정수 리스트에 추가한다
        print(int_number_list[0] / int_number_list[1])
    except ZeroDivisionError:
        print("숫자를 0으로 나눌 수 없습니다.")
    except IndexError:
        print("인덱스 접근이 잘못되었습니다.")

    # (3) 발생 오류와 오류 변수까지 포함한 except 문 - 두번째 경우에서 오류의 내용까지 알고 싶을 때

    try:
        numbers = input("숫자와, 나눌 숫자를 입력해주세요: ")
        string_number_list = numbers.split(" ")

        int_number_list = []
        for string_number in string_number_list:
            int_number_list.append(int(string_number))

        print(int_number_list[0] / int_number_list[1])
    except ZeroDivisionError as e:
        print("숫자를 0으로 나눌 수 없습니다.", e)
    except IndexError as e:
        print("잘못된 인덱스입니다.", e)

    # 나머지 죄다 묶어서 처리하기

    try:
        numbers = input("숫자와, 나눌 숫자를 입력해주세요: ")
        string_number_list = numbers.split(" ")

        int_number_list = []
        for string_number in string_number_list:
            int_number_list.append(int(string_number))

        print(int_number_list[0] / int_number_list[1])
    except ZeroDivisionError as e:
        print("숫자를 0으로 나눌 수 없습니다.", e)
    except Exception as e:
        print("알 수 없는 에러: ", e)

 # raise 명령어 : 파이썬에 정의되어 있지 않은 오류를 정의해 일부러 오류를 발생시키기 위함
 # a % b : a를 b로 나눈 나머지
    try:
        x = int(input("3의 배수를 입력하세요: "))
        if x % 3 != 0:
            raise Exception("3의 배수가 아닙니다.")
        print(x)
    except Exception as e:
        print("예외가 발생했습니다.", e)
