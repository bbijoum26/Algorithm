str = input()
answer = ''

for i in str:
    if i == i.upper():
        answer += i.lower()
    else:
        answer += i.upper()
print(answer)