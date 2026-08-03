def solution(name):
    answer = 0
    n = len(name)

    for c in name:
        answer += min(ord(c) - ord('A'),
                      ord('Z') - ord(c) + 1)

    move = n - 1

    for i in range(n):
        next_idx = i + 1

        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        move = min(
            move,
            i * 2 + (n - next_idx),
            i + 2 * (n - next_idx)
        )

    return answer + move