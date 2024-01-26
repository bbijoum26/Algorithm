def solution(a, d, included):
    answer = 0
    current_term = a

    for i in range(len(included)):
        if included[i]:
            answer += current_term
        current_term += d

    return answer