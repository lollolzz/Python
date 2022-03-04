def solution(arr):
    answer = []
    dic_1 = {}
    print(answer)
    for i in range(len(arr)):
        dic_1[arr[i]] = 0
    for i in range(len(arr)):
        dic_1[arr[i]] += 1

    for i in dic_1:
        if dic_1.get(i) == 1:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    return sorted(answer)
