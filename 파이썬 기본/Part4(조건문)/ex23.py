# 사용자로부터 연도를 입력받고 윤년인지 아닌지를 판단하는 프로그램을 만들기
# 윤년의 조건
# 1. 연도가 4로 나누어 떨어지면 윤년이다.
# 2. 100으로 나누어 떨어지는 연도는 제외한다.
# 3. 400으로 나누어 떨어지는 연도는 윤년이다.

user_year = int(input("연도를 입력하세요 : "))

if (user_year % 4 == 0 and user_year % 100 != 0) or user_year % 400 == 0:
    print(user_year,"의 연도는 윤년이다.")
else:
    print("윤년이 아니다.")