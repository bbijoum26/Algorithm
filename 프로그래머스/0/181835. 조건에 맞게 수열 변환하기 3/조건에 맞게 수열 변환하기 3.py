def solution(arr, k):
    answer = []
    if k % 2 == 0:
        for i in arr:
            i += k
            answer.append(i)
    else:
        for i in arr:
            i *= k
            answer.append(i)
    return answer