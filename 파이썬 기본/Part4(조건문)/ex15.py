# if ! elif ~ else(옵션) 대한 실습
# esle에는 조건을 쓰지않는다
# 다중 조건 중 하나만 만족하면 그 이후의 조건은 검사하지 않는다

score = int(input("성적을 입력하세요(0~100) : "))

if score >= 90:
    print("학점 A")
elif score >= 80:
    print("학점 B")
elif score >= 70:
    print("학점 C")
elif score >= 60:
    print("학점 D")
else: # else 구무은 옵션이지만 다중 조건을 설정 할 때는 절대 조건을 명시하면 안된다.
    print("학점 F")


