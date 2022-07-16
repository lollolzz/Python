# 플래그 변수를 사용한 무한 루프 문제
# flag 변수 이용한 무한루프
# flag 참 거짓으로 while문 만들고 if elif등으로 조건 넣기
# 1-증속, 2-감속, 3-중지를 출력하고 사용자의 입력을
# 1, 2, 3 받아서
# 증속을 하면 속도를 10 씩 증가하고 출력 해 준다.
# 감속을 하면 속도를 10 씩 감속하고 출력 해 준다.
# 중지를 하면 Flag변수를 이용하여 무한루프를 빠져나간다.

run = True
print(type(run))
speed = 0
keyCode = 0

while run:
    print("---------------------")
    print("1.증속   |  2.감속   | 3.중지")
    print("---------------------")
    keyCode = int(input("선택 : "))

    # 증속일 경우
    if keyCode == 1:
        speed += 10
        print("현재 속도 : ", speed)
    # 감속일 경우
    elif keyCode == 2:
        speed -= 10
        if speed < 0:
            print("속도를 더 줄일 수 없습니다.")
            speed = 0
        else:
            print("현재 속도 : ", speed)
    # 중지일 경우 플래그 변수를 False로 설정해주므로서, 무한 루프를 탈출한다.
    elif keyCode == 3:
        run = False

    # 사용자가 잘못 입력 햇을 경우
    else:
        print("잘못된 입력 값입니다.")

print("프로그램 종료")