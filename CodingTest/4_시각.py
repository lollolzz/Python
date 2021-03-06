"""
 날짜 : 21/08/20
 이름 : 권능한
 내용 : 코딩 테스트 - 시각
"""

# h값 입력 받기
h = int(input())
count = 0

# 3중 for문
# n시59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다
# 만약에 n이 5라면 6시까지의 '3'이 포함된 모든 경우의 수를 구한다
# 설정한 시간 h+1까지의 시간이 될때까지 '3'이 포함된 경우의 수를 구한다
for i in range(h+1):
    for j in range(60):
        for k in range(60):

           time = str(i) + str(j) + str(k)

           if '3' in time:
               count += 1
        # h가 5일 경우 count에 3이 포함된 경우가 11475가지가 존재한다

# 3포함에 대하여 찾을려면 문자열로 만들고 그담에 if문으로 찾으면 된다

print(count)