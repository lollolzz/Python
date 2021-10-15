"""
날찌 : 2021/10/15
이름 : 권능한
내용 : 코딩테스트 - 다이나믹 프로그래밍 피보나치 수열
"""

import time

# 프로그램 실행 시간 시작
start_time = time.time()

# 피보나치 함수
def fibo(n):
    if n <= 1:
        return n

    return fibo(n-1) + fibo(n-2)

for i in range(40):
    print(fibo(i))

# 프로그램 실생 시간 종료
end_time = time.time()

# 전체 수행시간
total_time = end_time - start_time
print('프로그램 수행시간 :', total_time)