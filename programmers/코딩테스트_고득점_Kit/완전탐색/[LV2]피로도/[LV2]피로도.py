def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def dfs(pirodo, cnt):
        nonlocal answer

        # 현재까지 방문한 개수로 최대값 갱신
        answer = max(answer, cnt)
        
        for i in range(len(dungeons)):
            need, cost = dungeons[i]
            
            if not visited[i] and pirodo >= need:
                visited[i] = True # 방문 
                dfs(pirodo - cost, cnt+1) # 다음 탐색
                visited[i] = False # 방문 취소
    
    dfs(k, 0)
    return answer