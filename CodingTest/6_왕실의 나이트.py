"""
날짜 : 21.08.27
이름 : 권능한
내용 : 코딩테스트 - 왕실과 나이트
"""

# 현재 나이트의 위치 입력받기
input_date = input()
row = int(input_date[1])
column = int(ord(input_date[0])) - int(ord('a')) + 1
# ord 아스키코드 변환값 나타내는 것 column번호 abcd...이것을 숫자로 변환하여 준다

result = 0

# 오른쪽 2칸, 위쪽 1칸
next_row = row - 1
next_column = column + 2

if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
# 문제의 그림상 체스판안에 위쪽에 짠 코드를 집어 넣어야하기 때문에
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



# cnt = 0
# dx = [2,2,-2,-2,-1,1,-1,1]
# dy = [1,1,-1,-1,-2,2,-2,-2]
#
# for num in range(8):
#     temp_row = row
#     temp_column = column
#     temp_row += dy[num]
#     temp_column += dx[num]
#     if temp_row >= 1 and temp_column >= 1:
#         cnt += 1
#     print(cnt)
