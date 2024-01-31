def solution(arr, queries):
    answer = []
    
    for query in queries:
        s, e, k = query
        sub_arr = arr[s:e+1] 
        filtered_values = [value for value in sub_arr if value > k]
        
        if filtered_values:
            answer.append(min(filtered_values))
        else:
            answer.append(-1)
    
    return answer