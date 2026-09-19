def solution(N, number):
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        repeated = int(str(N) * i)
        dp[i].add(repeated)
        
        for j in range(1, i):
            k = i - j
            for a in dp[j]:
                for b in dp[k]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
        if number in dp[i]:
            return i

    return -1