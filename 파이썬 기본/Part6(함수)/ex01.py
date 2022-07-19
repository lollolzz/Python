# 함수(function)에 대한 실습
# 1. 함수는 프로그램 안에서 중복된 코드를 제거한다.
# 2. 복잡한 프로그래밍 작업을 더 간단한 작업들로 분해할 수 있다.
# 3. 함수는 한 번 만들어두면 재사용이 얼마든지 가능하다.
# 4. 함수를 사용하면 가독성이 증대되고, 유지관리도 쉬워진다.

# 모듈 형태로 되어 있는 함수들의 집합

# 간단한 함수
# def 키워드 함수이름(매개변수)
# hello 파일의 내용을 전부 다 가져오기 때문에, 파일이름.함수명으로 접근할 필요가 없고
# 함수명만 호출하면 된다.

from hello import *     # hello.py를 import하여 ex01페이지를 run한다.
# import hello              # 파일명.함수명으로 접근해야 한다.

say_hello_name("엄복동")
say_hello_name("홍길동")

# 위와 같이 함수를 정의만 했다면 출력값은 없다. 출력값이 나오게 할려면
# 호출(call)을 해야한다.
# 함수 호출(function call)

# 함수가 호출되어 10을 출력을 하긴 하지만, 가독성이 좋지 않다.
# why? 함수의 매개변수명이 name이기 때문에, 매개변수명과 유사한 값을 입력해야한다
# say_hello(10)
# python에서는 오버로딩의 개념이 적용되지 않는다.
# 같은 함수의 이름이라면, 마지막에 정의되어진 함수를
# 기준으로 함수만 인식하게 된다. 하여, 함수명은 유니크한 값으로 함수명을 짓도록 한다.

# 생성한 함수에 있는 매개변수를 가진 것들로 기반으로 하여 변수들을 선언하여야 한다.
say_hello_name_msg("엄복동", "반값습니다.")
say_hello_name_msg("홍길동", "그렇군요.")

# get_sum()를 이용하여 범위값의 누적합을 구하는 코드
result = get_sum(1, 10)
print(type(result))
print("1~10 누접 합 : ", result)

result = get_sum(1, 30)
print(type(result))
print("1~10 누접 합 : ", result)

result = get_sum(1, 100)
print(type(result))
print("1~10 누접 합 : ", result)