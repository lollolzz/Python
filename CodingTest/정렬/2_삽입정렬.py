"""
날짜 : 21/09/03
이름 : 권능한
내용 : 코딩테스트 - 삽입정렬

"""

array = [4, 2, 1, 5, 3]

for i in range(1,len(array)):
    for j in range(i, 0, -1):

        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

    print('%d -round : %s' % (i, array))

print('최종결과 :', array)