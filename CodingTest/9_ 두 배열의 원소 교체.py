"""
날짜 : 21.09.03
이름 : 권능한
내용 : 코딩테스트
"""


N, K = map(int, input().split())

# arrayA = int(input())
# arrayB = int(input())
# minA = min(arrayA)
# maxB = max(arrayB)
#
# for i in range(len(arrayA)):
#     for j in range(len(arrayB)):
#         for K range
#
# for i in range(len(arrayA)):
#
#     for j in range(len(arrayB)):
#
#         if arrayA[i] > arrayB[j]:
#             tmp = arrayA[i]
#             arrayA[i] = arrayB[j]
#             arrayB[j] = tmp
#
#             print(' %s :' % arrayA)
#

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(K):
    if a[i] < b[i]:
        a[i] = b[i]
    else:
        break
print(sum(a))
