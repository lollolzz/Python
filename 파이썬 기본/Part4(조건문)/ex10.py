'''
쇼핑몰에서 물건을 구매할 때, 구입액이 5만원 이상이면,
5%의 할인을 해준다고 하자. 사용자에게 구입 금액을 입력받고,
최종적으로 할인금액 과 지불금액을 출력하는 프로그램을 만들기
'''

user_pay = int(input("구입금액 : "))


if user_pay >= 50000:
    dc = user_pay * 0.05 # 할인 금액
    sa = user_pay - dc # 지불 금액
    print("구입 금액 : ", user_pay, "원")
    print("할인 금액 : ", dc, "원")
    print("최종 금액 :", sa, "원입니다.")
else:
    print("할인 금액 대상이 되질 않습니다.",user_pay ,"원을 결재해주세요.")


