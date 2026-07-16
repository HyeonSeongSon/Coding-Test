import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        if scoville[0] >= K:
            return answer
        
        if len(scoville) < 2:
            return -1
            
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        mix = min1 + min2*2
        heapq.heappush(scoville, mix)
        answer +=1

    return answer