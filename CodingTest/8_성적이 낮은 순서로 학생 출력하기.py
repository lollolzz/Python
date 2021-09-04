"""
날짜 : 21.09.03
이름 : 권능한
내용 : 코딩테스트
"""

N = int(input())

array = []

for i in range(N):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')

# key lambda를 모를경우
# dataset = []
# for i in range(N):
#     a, b = input().split()
#
#     student = [a, int(b)]
#     dataset.append(student)
# # print(dataset)
# scores = []
# for i in range(len(dataset)):
#     score = dataset[i][1]
#     scores.append(score)
#
# scores.sort()
#
# names = []
# for score in scores:
#     for i, data in enumerate(dataset):
#         if score == data[1]:
#             names.append(data[0])
#             dataset.pop(i)
#
# print(names)