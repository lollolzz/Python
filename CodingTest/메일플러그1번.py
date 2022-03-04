# 소문자를 return 해야 한다
# 소문자로 만들어주어야 한다.
# ascii_lowercase 소문자 알파벳 리스트 들이 다 나오는 것
from string import ascii_lowercase

def solution(sentence):

    sentence2 = sentence.lower()
    print(ascii_lowercase)
    # string으로 반환된다
    alpha_list = list(ascii_lowercase)
    # list(ascii_lowercase) 이것만 쓰면 알파벳으로 된 리스트가 출력 / 리스트가 안붙으면 STRING형태로 반환된다.
    # 알파벳을 일일이 안적고 모듈을 사용 하였구나 (ascii_lowercase 이걸 사용했다는 거군 이 지원자가 ascii_lowercase  알고 있구나)
    for i in range(len(sentence)):
        # range는 for i in range는 범위이다 len(sentence)이것은 0부터 len(sentence)길이 까지 반복하라는 뜻
        # len 사용한 이유가 문장사용성에 있어 확장성이 있다.
        # len을 사용하지 않아도 되지만 가용성이 좋아서 이렇게 썻다.
        if sentence2[i] in alpha_list:
            print(sentence2[i])
            # 알파리스트라는 배열을 하나식 출력해보는 것
            alpha_list.remove(sentence2[i])
            # 이미 들어 있는 것을 지우고 출력한다
            # a가 여러번 있다면 이미 a를 한번 지웠기 때문에 a가 다시 나오지 않는다
    if len(alpha_list) == 0:
        # ascii_lowercase이 대입되어있는 alpha_list에 안사용한 소문자 알파벳이 없다면이라는 뜻
        return "perfect"
    print(alpha_list)
    answer = "".join(alpha_list)
    # 리스트가 아닌 스트링으로 답을 제출해야 하기 때문에 이렇게 사용
    # "".join(alpha_list) 스트링으로 바꾸는 함수
    return answer