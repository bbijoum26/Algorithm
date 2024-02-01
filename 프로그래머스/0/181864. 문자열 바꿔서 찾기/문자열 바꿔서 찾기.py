def solution(myString, pat):
    answer = 0
    temp = ''
    for i in myString:
        if i == "A":
            temp += i.replace("A", "B")
        else:
            temp += i.replace("B", "A")
    if temp.startswith(pat,temp.find(pat)):
        answer = 1
    else:
        answer = 0
    
    return answer