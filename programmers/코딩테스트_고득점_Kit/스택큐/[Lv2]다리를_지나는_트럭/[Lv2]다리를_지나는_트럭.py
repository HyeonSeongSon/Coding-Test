from collections import deque
def solution(bridge_length, weight, truck_weights):
    cnt = 0
    bridge = deque([0]*bridge_length)
    bridge_weight = 0
    trucks = deque(truck_weights)
    while trucks or any(bridge):
        cnt +=1
        left = bridge.popleft()
        bridge_weight -= left
        
        if trucks and bridge_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            bridge_weight += truck 
        else:
            bridge.append(0)
            
    return cnt