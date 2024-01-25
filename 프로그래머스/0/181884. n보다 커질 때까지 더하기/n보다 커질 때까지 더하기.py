def solution(numbers, n):
    result_sum = 0
    for i in range(len(numbers)):
        result_sum += numbers[i]
        if result_sum > n:
            break

    return result_sum
