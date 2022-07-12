# 사용자로부터 출력하고 싶은 구구단을 출력하는 프로그램을 만들기

n = int(input("출력하고 싶은 구구단 단 수 : "))
print(n,"의 구구단 시작")

for i in range(1, 10):
    if n < 2 or n > 9:
        print("단을 잘못 입력하셨습니다.")
        break
    print(n,'*',i, '=', n*i)