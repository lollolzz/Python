# 임의의 숫자를 발생시켜 사용자로 부터 입력을 받아 숫자를 맞추는 게임을 만들어 보기
from random import *

cnt = 0
num = randint(1, 100)
print("1부터 100사이의 숫자를 맞추어 보세요")
print("기회는 단 10번 입니다.")

while cnt < 10:
    guess = int(input("숫자를 입력하세요 : "))
    cnt += 1
    if guess < num:
        print("입력한 수가 발생한 난수보다 낮습니다.")
    elif guess > num:
        print("입력한 수가 발생한 난수보다 높습니다.")
    elif guess == num:
        print("정답입니다. 시도횟수는 :", cnt)
        print("--------------------------")
        code = input("계속 하려면 y, 그만하시려면 n을 입력하세요 : ")
        # 중첩 if문이 들어가서 게임의 지속 여부를 확인하는 코드
        if code == 'n': # 게임 종료 코드
            print("게임을 종료합니다.")
            break
        else:
            print("------------------------")
            # 게임을 재시작을 하기 위해서 다시 난수발생과 cnt를 초기화를 해야한다.
            print("게임을 재시작합니다.")
            num = randint(1, 100)
            cnt = 0

print("기회 10번이 다 소진 되었습니다. 게임이 종료되었습니다.")


