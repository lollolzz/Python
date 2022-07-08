# 사용자에게 명령어를 입력받아서 tutle그래픽을 제어를 해보자.
# 즉 사용자가 "left"를 입력을 하면 왼쪽으로 회전하게 되고 사용자가 "right"를 입력햇다면 오른쪽으로 회전하게 하는
# 프로그램 만들기

import turtle

# 펜의 기능을 t라는 변수에 저장함.

t = turtle.Pen()
# 반복문을 무한루프를 돌려서 if 구문을 이용하여 방향을 제어하는 코드
# while문은 통상 무한루프일 때 사용
# 무한루프를 프로그래밍을 했다면, 반드시 루프를 탈출하는 코드가 반드시 있어야 된다.(중요)
while True:
    direction = input("왼쪽 = left, 오른쪽=right, 종료=quit 입력 : ")
    # break는 무한루프를 빠져나가라는 keyword이다.
    # 무한루프에서 반드시 필요한 부분
    if direction == "quit":
        print("종료되었습니다.")
        break
    #########################

    # 사용자가 left를 입력했을 때
    if direction == "left":
        print("left를 입력하셨습니다.")
        t.left(60)
        t.forward(50)

    # 사용자가 right를 입력했을 때
    elif direction == "right":
        print("right를 입력하셨습니다.")
        t.right(60)
        t.forward(50)

    else:
        print("다시 입력하세요")

# 터틀 그래픽 창이 클릭이 되어야 화면에서 사라지게 하는 코드다.
turtle.exitonclick()
