# 한 사람이 돈이 5000원이 있는데, 사탕의 가격이 120원이라면, 최대로 살수 있는 사탕의 수는
# 몇 개인지 알아보는 프로그램을 만들어 보자

myMoney = int(input("가진 돈 : "))
candyPrice = int(input("사탕 가격 : "))
# 최대로 살 수 잇는 사탕의 개수
# / -> 몫(실수) , // -> 몫(정수)
numCandies = myMoney // candyPrice
print("최대로 살 수 있는 사탕의 개수 : ", numCandies)

# 최대로 살 수 있는 사탕을 구입하고 남은 돈
change = myMoney % candyPrice
print("최대로 사고 남은 돈 : ", change)