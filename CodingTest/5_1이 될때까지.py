"""
날짜 : 21/08/27
이름 : 권능한
내용 : 1이 될 때까지
"""

# n,k를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    # n이 1이 면 k보다 작은 수이기 때문에 나눌 수 가 없다 그래서 반복문을 끝내는 것이다
    if n == 1:
        break
    # n을 k로 나눳을 경우 완벽하게 나누어져 0이 됐을 경우를 나타낸것
    if n % k == 0:
        n /= k
    # n을 k로 나눳을 경우 0이 아니고 나머지가 발생한 경우 n에서 -1씩 차감한다
    else:
        n -= 1

    result += 1

print(result)

# while True:
#     # N이 K로  나누어 떨어지는 수가 될때까지만 1씩 빼기
#     # 총 연산을 수행하는 (result) - target 은 1을 처리한 개수를 한번에 구한 것이다.
#     target = (n // k) * k
#     result += (n - target)
#     n = target
#     # N이 K보다 작을 떼 (더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     # k로 나누기
#     result += 1
#     # k를 나누는 연산을 수행하므로 1번 추가
#     # result는 총연산 횟수를 나타낸다
#     n //= k
#
# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n-1)
# print(result)