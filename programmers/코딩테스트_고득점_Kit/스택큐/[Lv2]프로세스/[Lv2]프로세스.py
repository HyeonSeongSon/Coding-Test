from collections import deque

def solution(priorities, location):
    queue = deque([(v, i) for i, v in enumerate(priorities)])
    cnt = 0
    
    while queue:
        val = queue.popleft()
        if any(val[0] < q[0] for q in queue):
            queue.append(val)
        else:
            cnt += 1
            if val[1] == location:
                return cnt