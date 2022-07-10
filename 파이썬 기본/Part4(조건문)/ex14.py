# 몸무게와 키를 입력받아 BMI가 20.0이상이고 25미만이면
# 표준입니다. 라고 출력하고 아니면 체중관리가 필요합니다라고
# 출력하는 프로그램 만들기
# 키를 입력받고 100.0으로 나누고 공식에 대입하도록 한다.
# BMI = 몸무게 / (키 * 키)


height = float(input("키를 입력하세요 : "))
weight = float(input("몸무게를 입력하세요 : "))

# 복합대입 연산자를 이용
height /= 100.0  # height =  height / 100.0와 좌측 코드가 동일
print(height)
BMI = weight / (height * height)
print("BMI 값 : ", BMI)

if BMI >= 20.0 and BMI < 25.0:
    print("정상 체중 입니다.")
else:
    print("체중관리가 필요합니다.")