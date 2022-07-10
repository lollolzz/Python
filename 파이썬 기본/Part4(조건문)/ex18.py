# 주사위 눈을 랜덤으로 발생시켜서 해당하는 숫자를 출력하는 프로그램 만들기
# randint() 함수를 검색하여, 사용법을 익힌 후 프로그램을 작성하시오.

from random import *
# randint(a, b) 함수는 a 부터 b 까지의 사이에 있는 정수를 반환해주는 함수
num = randint(1, 6)
print("주사위 눈 : ", num)

# # random() 함수는 0.0부터 1.0미만의 임의의 값을 float 형태로 반환해주는 함수
# num = random()
# print("num : ", num)
# # randrange(start, stop, step) 함수는 start에서 step의 값에 따라서
# # 임의의 수를 반환을 해주는 함수이다
# num = randrange(1, 101, 2)
# print("num : ", num)
#
# # 범위안의 숫자 안 숫자-1 숫자 중에 랜덤으로 나온다
# num = randrange(10)
# print("num : ", num)
