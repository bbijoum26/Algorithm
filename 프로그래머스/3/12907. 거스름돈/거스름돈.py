def solution(n, money):
    # dp[i]: 거스름돈 i를 거슬러주는 방법의 수
    dp = [0] * (n + 1)
    
    # 초기값 설정
    dp[0] = 1
    
    # 동전을 하나씩 추가하며 dp 배열 갱신
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] = (dp[i] + dp[i - coin]) % 1000000007
    
    return dp[n]