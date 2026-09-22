def solution(tickets):
    tickets.sort()

    visited = [False] * len(tickets)
    route = ["ICN"]

    def dfs(airport):
        if len(route) == len(tickets) + 1:
            return True

        for i in range(len(tickets)):
            if visited[i]:
                continue
            if tickets[i][0] != airport:
                continue
            visited[i] = True
            route.append(tickets[i][1])

            if dfs(tickets[i][1]):
                return True
            route.pop()
            visited[i] = False

        return False

    dfs("ICN")

    return route