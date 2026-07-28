def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    answer = 0

    def dfs(s):
        nonlocal answer

        if len(s) > 5:
            return

        if s:
            answer += 1

            if s == word:
                return True

        for v in vowels:
            if dfs(s + v):
                return True

    dfs("")
    return answer