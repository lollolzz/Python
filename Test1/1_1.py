"""
날짜 : 2021/08/12
이름 : 권능한
내용 : 파이썬 기본 입출력
"""

# 이름, 나이, 생년월일 출력
name = input("이름을 입력하시오 : ")
age = input("나이를 입력하시오 : ")

year = 2021 - int(age)

print(name+'님은 ' +age+'세이고 '+str(year)+'년도에 태어났습니다.')

# 평균 계산 출력
n1 = int(input("첫 번재 숫자 입력 : "))
n2 = int(input("첫 번재 숫자 입력 : "))
n3 = int(input("첫 번재 숫자 입력 : "))

avg = (n1 + n2 + n3) / 3

print(n1, n2, n3, "의 평균은", avg, "입니다.")