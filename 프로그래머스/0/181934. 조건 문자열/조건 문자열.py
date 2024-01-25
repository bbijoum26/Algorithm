def solution(ineq, eq, n, m):
    answer = 0
    if (ineq in ">") and (eq in "="):
        if n >= m:
            answer = 1
        else:
            answer = 0
    elif (ineq in "<") and (eq in "="):
        if n <= m:
            answer = 1
        else:
            answer = 0
    elif (ineq in ">") and (eq in "!"):
        if n > m:
            answer = 1
        else:
            answer = 0
    elif (ineq in "<") and (eq in "!"):
        if n < m:
            answer = 1
        else:
            answer = 0
            
    return answer