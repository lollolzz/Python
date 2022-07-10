# 중복(nested) if ~ else 구문
# 사용자로부터 아이디를 입력받아서 등록되어진 아이디인지를 검사하는 프로그램을
# 작성하는데, 등록된 아이디를 리스트(list)에 저장하도록 한다.
# 아이디가 등록되어 있다면, 패스워드를 물어보도록 한다.
# 단, 패스워드는 "1234"라고 가정하도록 한다.

user_id = input("아이디를 입력하세요 : ")
already_id = ["smdgks", "lollolzz1018", "park", "wow"]
totall_id = []
pw = "1234"

# if user_id in already_id: # 사용자가 입력한 id가 already_id에 있는지 확인하는 코드
#     password = input("패스워드를 입력하세요 : ")
#     if password == pw: # 중첩 if문
#         print(user_id + "님이 로그인 하셨습니다.")
#     else:
#         print("패스워드가 틀렸습니다.")
# else:
#     print("회원가입이 되질 않았습니다.")

if user_id == already_id:
    pw = int(input("패스워드를 입력하세요 : "))
    if pw == 1234:
        print("정상적으로 로그인 되었습니다.")
    else:
        print("비밀번호를 확인해 주세요.")
elif user_id != already_id:
    q_answer = input("가입이 필요한 ID입니다, 가입을 원하시나요 ?(가입을 원하시면 'y'를 입력하세요.) : ")
    if q_answer == 'y':
        print("등록이 완료 되었습니다, 초기 설정 pw은 1234입니다.")
        totall_id.append(user_id)
    elif q_answer != 'y':
        print("다음 기회에 보아요")

print("새롭게 가입된 ID : ", totall_id)
