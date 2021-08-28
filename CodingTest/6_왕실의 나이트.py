"""
날짜 : 21/08/27
이름 : 권능한
내용 : 코딩테스트 - 왕실과 나이트
"""

# 현재 나이트의 위치 입력 받기
input_date = input()
row = int(input_date[1])
column = int(ord(input_date[0])) - int(ord('a')) + 1
# ord는 아스키코드 변환값을 나타내는 것 column번호 abcd...이것을 숫자로 변환하여 준다

result = 0

# 나이트의 시작 위치에 따라 움직일 수 있는 모든 경우의 수를 적어보자
# 매우 직관적이라 다른 방법보다 초보가 알아 보기 쉽다
# if조건에 해당하는 경우에만 result의 횟수가 상승한다

# 오른쪽 2칸, 위쪽 1칸 (왼,오는 열의 움직임,,,, 위,아래는 횡의 움직음)
next_row = row - 1
next_column = column + 2

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
# 문제의 그림상 체스판안에 위쪽에 짠 코드를 집어넣어야하기 때문에 가로새로 8칸씩이 필요한다
    result += 1
# 오른쪽 2칸, 아래쪽 1칸
next_row = row + 1
next_column = column + 2

if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
# 문제의 그림상 체스판안에 위쪽에 짠 코드를 집어 넣어야하기 때문에
    result += 1

# 왼쪽 2칸, 위쪽 1칸
next_row = row - 1
next_column = column - 2

if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
# 문제의 그림상 체스판안에 위쪽에 짠 코드를 집어 넣어야하기 때문에
    result += 1

# 왼쪽 2칸, 아래쪽 1칸
next_row = row + 1
next_column = column - 2

if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
# 문제의 그림상 체스판안에 위쪽에 짠 코드를 집어 넣어야하기 때문에
    result += 1

# 위쪽 2칸, 오른쪽 1칸
next_row = row - 2
next_column = column + 1

if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
# 문제의 그림상 체스판안에 위쪽에 짠 코드를 집어 넣어야하기 때문에
    result += 1

# 위쪽 2칸, 왼쪽 1칸
next_row = row - 2
next_column = column - 1

if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
# 문제의 그림상 체스판안에 위쪽에 짠 코드를 집어 넣어야하기 때문에
    result += 1

# 아래쪽 2칸, 오른쪽 1칸
next_row = row + 2
next_column = column + 1

if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
# 문제의 그림상 체스판안에 위쪽에 짠 코드를 집어 넣어야하기 때문에
    result += 1

# 아래쪽 2칸, 왼쪽 1칸
next_row = row + 2
next_column = column - 1

if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
# 문제의 그림상 체스판안에 위쪽에 짠 코드를 집어 넣어야하기 때문에
    result += 1

print(result)
