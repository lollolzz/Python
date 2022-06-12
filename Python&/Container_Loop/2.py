# 우리의 주적은 중복 ~
input_id = input("아이디를 입력해주세요.\n")
members = ['egoing', 'k8805', 'smdgks']
for member in members:
    if member == input_id:
        print('Hello!, ' + member)
        import sys
        sys.exit() # 프로그램을 종료 시키는 함수 이다 ~

print('Who are you, what if smdgks?\n'
      'You should go out right now')
