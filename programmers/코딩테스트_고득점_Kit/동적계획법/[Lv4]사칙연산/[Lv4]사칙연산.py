def solution(arr):
    numbers = list(map(int, arr[::2]))
    operators = arr[1::2]
    n = len(numbers)
    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp_max[i][i] = numbers[i]
        dp_min[i][i] = numbers[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp_max[i][j] = float("-inf")
            dp_min[i][j] = float("inf")
            for k in range(i, j):
                operator = operators[k]
                left_max = dp_max[i][k]
                left_min = dp_min[i][k]
                right_max = dp_max[k + 1][j]
                right_min = dp_min[k + 1][j]
                if operator == "+":
                    max_value = left_max + right_max
                    min_value = left_min + right_min
                else:  # "-"
                    max_value = left_max - right_min
                    min_value = left_min - right_max
                dp_max[i][j] = max(
                    dp_max[i][j],
                    max_value
                )
                dp_min[i][j] = min(
                    dp_min[i][j],
                    min_value
                )

    return dp_max[0][n - 1]