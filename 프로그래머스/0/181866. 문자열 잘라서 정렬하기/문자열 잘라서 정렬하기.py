def solution(myString):
    parts = myString.split('x')    
    parts = [part for part in parts if part]
    parts.sort()  
    return parts