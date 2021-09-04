"""
날짜 : 21.09.03
이름 : 권능한
내용 : 코딩테스트
"""


array = []
n = int(input())

for i in range(n):
    num = int(input())
    array.append(num)
array.sort(reverse=True)
for i in array:
    print(i, end=' ')

