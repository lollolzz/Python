# 사용자로부터 태어난 연도를 입력받아서 초등학생, 중학생, 고등학생, 대학생 분류 중
# 에서 어디에 해당하는지를  출력하는 프로그램을 작성해보세요. (현재 나이)
# 나이 : 8 ~ 13(초등학생), 14 ~ 16(중학생), 17 ~ 19(고등학생), 이 외의
# 나이라면 일반인으로 분류를 하도록 한다. (일반적인 기준으로 나이를 산정하였다.)

year = int(input("태어난 연도 : "))
# 나이 계산
age_year = (2022 - year) + 1
print(age_year)

if age_year >= 20:
    print("일반인입니다.")
elif age_year >= 17:
    print("고등학생입니다.")
elif age_year >= 14:
    print("중학생입니다.")
elif age_year >= 8:
    print("초등학생입니다.")
else:
    print("아주 어린아이 입니다.")

