def solution(arr, n):
    answer = []
    if len(arr) % 2 != 0:       # 0, 2, 4 + n  
        for i, num in enumerate(arr):
            if i % 2 == 0:
                num += n
                answer.append(num)
            else:
                answer.append(num)
    else:
        for j, num in enumerate(arr):
            if j % 2 != 0:
                num += n
                answer.append(num)
            else:
                answer.append(num)
    return answer