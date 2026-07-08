from collections import deque

def solution(arr):
    que = deque(arr)
    answer = [que.popleft()]
    while que:
        num = que.popleft()
        if answer[-1] != num:
            answer.append(num)
    return answer