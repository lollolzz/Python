"""
날짜 : 21/09/03
이름 : 권능한
내용 : 코딩테스트 - 퀵정렬

"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sork(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:

        while left <= end and array[pivot] >= array[left]:
            # 피봇보다 큰 데이터를 찾을 때까지 왼쪽 포인터를 +1
            left += 1

        while right > start and array[pivot] <= array[right]:
            # 피봇보다 작은 데이터를 찾을 때까지 왼쪽 포인터를 +1
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    # 파티션으로 나눈 후 왼쪽, 오른쪽 각각 다시 퀵정렬 수행
    quick_sork(array, start, right-1)
    quick_sork(array, right+1, end)

quick_sork(array, 0, len(array)-1)
print(array)