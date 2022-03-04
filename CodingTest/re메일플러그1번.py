from string import ascii_lowercase


sentence = input()
sentence2 = sentence.lower()
alpha_list = list(ascii_lowercase)

for i in range(len(sentence)):
    if sentence2[i] in alpha_list:
        alpha_list.remove(sentence2[i])
if len(alpha_list) == 0:
    print("perfect")

print(alpha_list)
answer = "".join(alpha_list)
print(answer)
