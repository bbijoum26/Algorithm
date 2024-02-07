def solution(number):
    num = 0
    answer = 0
    for i in number:
        num += int(i)

    answer = num % 9
    return answer