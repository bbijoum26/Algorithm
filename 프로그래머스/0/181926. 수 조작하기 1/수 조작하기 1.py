def solution(n, control):
    # answer = 0
    for i in control:
        if i in "w":
            n += 1
        elif i in "s":
            n -= 1
        elif i in  "d":
            n += 10
        elif i in "a":
            n -= 10
        
    return n