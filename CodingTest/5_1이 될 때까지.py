"""
날짜 : 21/08/27
이름 : 권능한
내용 : 1이 될 때까지
"""

# n,k를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0


while True:

    if n == 1:
        break
    if n % k == 0:
        n /= k
    else:
        n -= 1

    result += 1


print(result)




# while True:
#     # N이 K로 나누어 떨어지는 수가 될때까지만 1씩 빼기
#     # 총 연산을 수행하는 횟수 (result) - target 은 1을 처리한 개수를 한번에 구한 것이다.
#     target = (n // k) * k
#     # 총 연산을 수행하는 횟수 (result) - target 은 1을 처리한 개수를 한번에 구한 것이다.
#     result += (n - target)
#     n = target
#     # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     # K로 나누기
#     result += 1   # # k를 나누는 연산을 수행하므로 1번 추가
#     n //= k
#
# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n - 1)
# print(result)



