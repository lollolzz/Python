# 제곱을 구하는 함수
# 함수를 선언 및 구현
def square(num):
    temp = num * num
    # 반환값 처리
    return temp


# 두 수중 큰 값을 반환하는 함수
# 두 개의 정수를 입력 받아서 두 수 중에서 더 큰 수를 찾아서 큰 수를 리턴하는
# 함수를 만들어보자.

def get_max(x, y):
    # return문은 최소화하는게 좋은 코드이다.
    temp = 0
    if x > y:
        temp = x
    else:
        temp = y
    return temp

# 두 수중 작은 값을 반환하는 함수
# 두 개의 정수를 입력받아서 두 수 중에서 더 작은 수를 찾아서 작은 수를 리턴하는
# 함수를 만들어보자.

def get_min(x, y):
    temp = 0
    if x > y:
        temp = y
    else:
        temp = x
    return temp


# 거듭제곱 구하는 함수
def get_gudeap(x, y):
    result = 1
    for i in range(y):
        result *= x
    # result = x ** y 해도 나옴

    return result