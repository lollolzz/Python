# while문 실습
# while 문은 조건을 정해놓고 반복을 하는 구조이다.


i = 0
while i < 5:
    print("반값습니다.")
    i += 1
    # i += 1 -> 이 조건을 빼면, 무한 루프에 빠지게 된다.
    # while문은 무한 루프를 돌것이다.
print("반복이 종료되었습니다.")

# 숫자 0 ~ 9 까지 줄바꿈을 하지 아니하고 출력해보기(while 문 사용)

# i = 0
# while i < 10:
#     print(i, end=" ")
#     i += 1

# 1~10까지의 누계합을 구하는 예제
i = 1
hap = 0
while i <= 10:
    hap += i
    i += 1
print("1~10까지의 누계합 : ", hap)

# 펙토리얼 구하기
# !5

i = 1
fa = 1

while i <= 5:
    fa *= i
    i += 1
print("5!의 값은 %d 입니다." % fa)


# while문을 사용하여 3단을 출력하는 예제

i = 1

while i <=9:
    print("3 * %d = %d" %(i, 3*i))
    i += 1

# 정수 안의 각 자리수의 합을 계산하는 예제
# 예를 들면 1234라면 (1+2+3+4)를 계산하는 것이다.

num =1234
hap = 0
while num > 0:
    digit = num % 10 # 해당하는 자릿수의 값을 구하는 코드
    hap += digit
    num = num // 10 # 10으로 나누어 줌으로써 몫으로만 num에 저잗되는 코드
print("1234정수의 자리수의 합은 %d" % hap)