# for문을 이용하여, 펙토리얼(Factorial)을 계산하는 프로그램을 작성해보자.
# 펙토리얼 n!은 1부터 n 까지의 정수의 모두 곱한 것을 의미하는 것이다.
# f(1) = 1이다.

fact = 1.0

n = int(input("펙토리얼 값을 정수를 입력하세요 : "))

for i in range(n, 0, -1):
    fact *= i
    # fact = fact * i를 복합대입연산자를 사용한 코드이다.

print(n, "!은", fact, "입니다.")
