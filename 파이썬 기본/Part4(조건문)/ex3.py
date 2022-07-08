# 사용자로부터 성별을 입력받아서 해당하는 성별을 출력하는 프로그램만들기
gender = input("성별을 입력하세요 : ")

if gender == 'man':
    print("남자입니다.")
elif gender == 'woman':
    print("여성입니다.")
else:
    print("잘못입력하셨습니다.")