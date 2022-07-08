# 사용자로부터 두 개의 정수를 입력받아서 둘 중에서 큰 수를 출력하는 프로그램 만들기

a = int(input(" 첫 번째 정수 : "))
b = int(input(" 두 번째 정수 : "))

Max = 0
if a > b:
    Max = a
    print("둘 중에 큰 수 : ", Max)
elif b > a:
    Max = b
    print("둘 중에 큰 수 : ", Max)
else:
    print(" a와 b는 같은 수 입니다.")


