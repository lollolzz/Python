# 입력받은 문자열을 거꾸로 출력하는 프로그램을 작성하시오.

statements = input("문자열을 입력하세요 : ")
s_reverse = ""

# for문을 활용한 방법
for ch in statements:
    # a -> b a -> c b a
    # 처음 들어온 a가 b가 들어오면 제일 마지막이 되고, c가 들어오면 b, a가 뒤로 밀려서 저장된다.
    s_reverse = ch + s_reverse

print("입력한 문자열 : " + statements)
print("역순으로 출력한 문자열 : " + s_reverse)
print("---------------------------------------")

# python 내장함수를 이용한 뒤집기

# list를 이용한 reverse()이다. - 이것은 list 타입만을 역순으로 바꿔주는 역할 
# list() 함수는 문자열을 리스트 타입으로 바꾸는 함수이다.
# list타입으로 바꾸어 주어야한다
s_list = list(statements)
# print(type(s_list))
# reverse() 는 리스트 타입을 역순으로 바꿔주는 함수이다.
s_list.reverse()
# join() 함수는 역순으로 된 문자열을 연결해서 출력을 하고 있는 코드
print("".join(s_list))

print("---------------------------------------")     
# reversed()는 문자열을 역순으로 하는 함수
# reversed()는 문자열에만 역순으로 출력하는 함수
s1 = statements
print("".join(reversed(s1)))

# python에서는 [::-1]를 사용하여 문자열을 역순으로 출력 할 수 있다.
print("---------------------------------------")
print(statements[::-1])

print("----------------------------------------")
# 문자열 3번째 인덱스부터 역순으로 출력하는 방법이다.
print(statements[3::-1])

