"""
날짜 : 21/08/13
이름 : 권능한
내용 : 코딩 테스트 - 큰 수의 법칙

"""
# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# n개의 숫자를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort(reverse=True) # 입력받은 수들 정렬
first = data[0] # 가장 큰 수
second = data[1] # 두 번째로 큰 수

result = 0

while True : # while 문이 true 가 아닌 false가 되면 while문 빠져나온다.
    for i in range(k): # 가장 큰 수를 k번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더 하기
    m -= 1 #더할 때마다 1씩 빼기

print(result)

"""
 while문을 보면 먼저 for문에서 가장 큰 수를 k번 더하고, 더할때마다 m의 값을 1씩 감소 시킨다. 후에 
 if문에서 두 번째로 큰 수를 1번 더한다.
 숫자를 몇 개 더 더 할 수 있는지 의미하는 m이 0인지 확인한 후에 result에 배열의 원소를 더한다 .
 ------------
 for문에서 first를 k번 더하고( k번 더하면서 m의 숫자는 -1 되는중) 
 k번 더한 후 거기에다가 second를 한 번 더한다 (이때 위에서 감소된 m에 -1을 해준다)
 아직 while문이 true이기 때문에 반복 한다 
 위의 과저을 반복하다 보면 m이 0이 되어 조건문을 빠져나가게 된다 .
 """