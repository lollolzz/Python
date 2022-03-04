def solution(arr):
    answer = []
    dic_1 = {}
    # 딕셔너리 구조를 왜 쓴걸가 ? 키와 값으로 이루어졌다 시간복잡도를 줄이기 위하여 사용하였다.
    # 딕셔너리는 list사용 했을 경우 보다 효율성이 좋다 그래서 사용했다
    #
    for i in range(len(arr)):
        dic_1[arr[i]] = 0
        # arr 의 a는 처음은 2가 된다
        #   [arr[i]] key 이고 0은 value이다.
    for i in range(len(arr)):
        dic_1[arr[i]] += 1
        # 위에서 0으로(정수라서 0으로초기화) 리셋을 시켜주어야지 연산을 할 수 있는 것.

    for i in dic_1:
        if dic_1.get(i) == 1:
            # get(i)란 키값으로 벨류값을 찾는다 i에는 키가 들어간다
            # 벨류가 1인 것을 찾기 위하기 때문이다.
            answer.append(i)
            # append는 add이기 때문에 answer에 하나씩 추가 한다
    if len(answer)==0:
        return [-1]
        # len길이가 0경우 -1을 리턴한다.
    return sorted(answer)
        # 문제에서 보면 정렬을 하라고 되있어 sorted해서 값을 리턴
        # 오름차순정렬이다. 그냥 sort랑은 다른점은 answer가 저장이 안된다.
        # sorted는 변환값을 가져온다 sort는 true, flase를 가져온다.
        # sort sorted차이 알아오기