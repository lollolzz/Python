# 사용자로부터 2개의 정수 값을 입력받고 첫 번째 입력 받은 값 부터
# 두 번째 입력 받은 값 까지 범위에서 3의 배수이고 4의 배수를 제외하고
# 출력하는 프로그램을 작성하시오.

n = int(input("첫 번째 수를 입력하세요 : "))
m = int(input("두 번째 수를 입력하세요 : "))

for i in range(n, m+1):
    # continue는 아래 문장을 실행하지 아니하고,
    # 다시 for문 첫 상단으로 돌아간다.
    # continue는 조건식이 참이면 아래 문장을 실행치 아니고 for문으로 이동하여 증가를 한다.
    if i % 3 == 0 and i % 4 == 0:
        continue
    print(i)






