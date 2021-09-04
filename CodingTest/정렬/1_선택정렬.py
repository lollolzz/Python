"""
날짜 : 21/09/03
이름 : 권능한
내용 : 코딩테스트 - 선택정렬

"""
array = [4, 2, 1, 5, 3]

for i in range(len(array)):
    for j in range(i+1, len(array)):

        if array[i] > array[j]:
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp

    print('%d - round : %s' % (i+1, array))

print('최종결과 :', array)