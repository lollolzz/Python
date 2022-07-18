# 사용자로부터 문자열을 입력받아서 알파벳 문자의 개수, 숫자의 개수,
# 스페이스의 개수를 출력하는 프로그램을 작성하시오.

word = input("문자열을 입력하세요(영문자, 숫자, 공백) : ")
alp_cnt = 0
num_cnt = 0
sp_cnt = 0

for letter in word: # 입력받은 문자열을 letter에 넣어서 하나씩 가져오기
    if letter.isalpha():
        alp_cnt += 1
    elif letter.isdigit(): # 숫자라면...
        num_cnt += 1
    elif letter.isspace():
        sp_cnt += 1
    else:
        print("해당하는 문자는 알파벳, 수자, 공백이 아닙니다.")

print("문자열에서 영문자의 수 : ", alp_cnt)
print("문자열에서 숫자의 수 : ", num_cnt)
print("문자열에서 공백의 수 : ", sp_cnt)