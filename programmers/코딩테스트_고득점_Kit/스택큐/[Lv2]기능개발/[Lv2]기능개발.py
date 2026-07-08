from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100-x)/y) for x, y in zip (progresses, speeds)]
    days = deque(days)
    
    while days:
        fst = days.popleft()
        cnt = 1
        while days and days[0] <= fst:
            days.popleft()
            cnt += 1
        answer.append(cnt)
        
    return answer