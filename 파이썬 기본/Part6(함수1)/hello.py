# 이름이 같은 함수가 두 개라면, 마지막으로 생성된 함수를 사용해서 변수들이 출력된다.
# 이름을 같게하지 않으면 둘 다 사용 가능

def say_hello_name(name,):                # 함수의 선언부
    print("안녕하세요, " + name)       # 함수의 구현부(정의부, 몸체)

def say_hello_name_msg(name, msg):                # 함수의 선언부
    print("안녕하세요, " + name, msg)       # 함수의 구현부(정의부, 몸체)

# 값을 반환하는 함수 예제
# start ~ end 까지의 누적합을 구하는 함수
def get_sum(start, end):
    hap = 0
    for i in range(start, end+1):
        hap += i
    return hap