import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    entry_count = {}  # 삽입된 값의 개수를 카운트

    for op in operations:
        cmd, num = op.split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            entry_count[num] = entry_count.get(num, 0) + 1
        elif cmd == 'D':
            if not entry_count:
                continue

            if num == 1:  # 최대값 삭제
                while max_heap:
                    max_val = -heapq.heappop(max_heap)
                    if entry_count.get(max_val, 0) > 0:
                        entry_count[max_val] -= 1
                        break
            elif num == -1:  # 최소값 삭제
                while min_heap:
                    min_val = heapq.heappop(min_heap)
                    if entry_count.get(min_val, 0) > 0:
                        entry_count[min_val] -= 1
                        break

    # 남아있는 값 필터링
    min_val = max_val = 0
    valid_values = [k for k, v in entry_count.items() if v > 0]
    if valid_values:
        min_val = min(valid_values)
        max_val = max(valid_values)

    return [max_val, min_val]