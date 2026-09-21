def solution(n, times):
    left = 0
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        count = 0
        for time in times:
            count += mid // time
        if count >= n:
            right = mid - 1
        else:
            left = mid + 1

    return left