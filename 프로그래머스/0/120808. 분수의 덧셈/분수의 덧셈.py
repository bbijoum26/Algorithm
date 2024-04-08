def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    common_denom = lcm(denom1, denom2)
    numer1_adjusted = numer1 * (common_denom // denom1)
    numer2_adjusted = numer2 * (common_denom // denom2)
    
    result_numer = numer1_adjusted + numer2_adjusted
    result_denom = common_denom
    
    divisor = gcd(result_numer, result_denom)
    
    return [result_numer // divisor, result_denom // divisor]