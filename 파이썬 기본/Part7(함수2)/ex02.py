# 문자열 전달에 대한 실습
# 문자열에 대한 내용도 앞서 살펴본 숫자형의 객체와 동일한 변경될 수 없는
# immutable object 형태이다.
# 파이썬의 경우는 타 언어의 call by value의 개념과는 조금은 다르다.
# 그 이유는 파이선은 모든 것을 "객체"로 판단하기 때문이다.
# 파이썬의 이런 특성이 존재하므로, call by objective라고도 칭한다.

# 함수에서 연산을 하면 새로운 객체가 생성 되므로, 주소 값이 달라지고
# 함수에서 연산을 거치지 않은 값들은 모두 같은 값을 가진다
# 기존의 주소값이 stack에 쌓여 있는데, 함수가 호출되면 이 함수가 stack에 쌓이게 되고
# 그래서 두 가지는 다른 주소값을 가지게 된다는 느낌의 내용
def change(string):
    print("change()내의 연산전의 string 값 : ", string)
    print("change()내의 연산전의 string 주소(id) : ", id(string))
    string += "공부합니다."
    print("change()내의 연산후의 string 값 : ", string)
    print("change()내의 연산후의 string 주소(id) : ", id(string))

msg = "안녕하세요 저는 파이썬을 "
print("호출 전 msg 값 : " + msg)
print("호출 전 msg 주소 값 : ", id(msg))
change(msg)
print("호출 후 msg 값 : " + msg)
print("호출 후 msg 주소 값 : ", id(msg))