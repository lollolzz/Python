# 모듈을 다른 파일로 만들고 import하면 불러 올 수 있다.
import auth

input_id = input('아이디를 입력해주세요\n')

if auth.login(input_id):
    print('Hello, '+input_id)
else:
    print('Who are you?')
