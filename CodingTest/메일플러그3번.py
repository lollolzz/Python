# 좌표 큰 사각형 구하기
# 길이로 문제를 구해야 겟다고 말하자

def solution(n, m, x_axis, y_axis):
    x_list=[]
    y_list=[]
    x_length = 0;

    for i in range(len(x_axis)):
        if i == 0:
            x_list.append(x_axis[i])
            # 길이값이 들어간다 즉 문제의 표에서 1을 넣는다는 말
        elif i > 0 :
            x_length = x_axis[i]-x_axis[i-1]
            #x_length i-1로 해줌 위에서 잘라준것을 새롭게 가정해서 길이를 담은 배열
            x_list.append(x_length)
    x_list.append(n-x_axis[-1])
    # 마지막으로 새롭게 생긴 수들을 배열에 넣기 위한 것
    # 맨 마지막 수를 총길이에서 빼준다
    
    for j in range(len(y_axis)):
        if j == 0:
            y_list.append(y_axis[j])
        elif j > 0 :
            y_length=y_axis[j]-y_axis[j-1]
            y_list.append(y_length)
    y_list.append(m-y_axis[-1])
    print(x_list,y_list)
    max_1 = 0
    num = 0
    print(x_list,y_list)

    for i2 in range(len(x_list)):
        # 위의 for문들롤 list가 만들어 짐
        # 2중 for문 사용 이유 i, j가 반복 되야한고 두 가지를 곱해야 한다.
        for j2 in range(len(y_list)):
            print(x_list[i2]*y_list[j2])
            if x_list[i2]*y_list[j2] > max_1:
                max_1 = x_list[i2]*y_list[j2]
    answer = max_1
    return answer
