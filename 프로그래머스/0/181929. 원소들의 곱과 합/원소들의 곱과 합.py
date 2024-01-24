def solution(num_list):
    answer = 0
    product = 1
    square = 0

    for i in num_list:
        product *= i
        square += i
    
    if product < (square ** 2):
        answer = 1
    else:
        answer = 0
    
    return answer