# 학점을 세부적으로 나누는 프로그램을 작성하기 - 중첩 if문 사용
# 조건
# 1. 사용자로부터 점수를 입력받는다.
# 2. 점수가 95점이상 100이하라면 A+ 을 출력한다
# 3. 점수가 90점이상 94이하라면 A0 을 출력한다
# 다른 B, C, D 학점도 위와 같이 출력한다.
# 단, F는 그냥 출력하도록 하자.

grade = int(input("점수를 입력하세요 : "))
print("입력한 점수 : ", grade)

if grade >= 90 and grade <= 100:
    if grade >= 95:
        print('A+')
    elif grade >= 90:
        print('A0')
elif grade >= 80 and grade < 90:
    if grade >= 85:
        print('B+')
    elif grade >= 80:
        print('B0')
elif grade >= 70 and grade < 80:
    if grade >= 75:
        print('C+')
    elif grade >= 70:
        print('C0')
elif grade >= 60 and grade < 70:
    if grade >= 65:
        print('D+')
    elif grade >= 60:
        print('D0')
else:
    print('당신의 학점은 F입니다.')