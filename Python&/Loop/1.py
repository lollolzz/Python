# 반복문 귀한줄 알아야 한다.
# print("Hello world 0")
# print("Hello world 9")
# print("Hello world 18")
# print("Hello world 27")
# print("Hello world 36")
# print("Hello world 45")
# print("Hello world 54")
# print("Hello world 63")
# print("Hello world 72")
# print("Hello world 81")

# 반복문은 쉽다. 반복은 무한이거나 무한이 아니거나
# while False:
#     print('Hello world')
# print('After while')

# i의 값이 4가 되면 while문이 False가 되어서 더 이상 출력 되어지지 않는다.
# i = 0
# while i < 3:
#     print('Hello world')
#     i = i + 1

# while을 이용한 반복문
# i = 0
# while i < 10:
#     print('Hello world '+str(i*9)+'')
#     i = i + 1

# 반복 + 조건 합체
# 유지 보수의 편의성이 높아졌다
i = 0
while i < 10:
    # if i!= 4: # i가 4가 아닐 때 참이 되는 코드
    if i == 4:
        print(i)
    i = i + 1

j = 0
while j < 10:
    if j == 4:
        break # j가 4일 때 이 반복문은 끝이 난다. / 그리고 4 전까지의 숫자는 출력 된다.
    print(j)
    j = j + 1
print('Well Done')



