def solution(array, commands):
    answer = []
    for i,j,k in commands:
        com = array[i-1:j]
        com = sorted(com)
        answer.append(com[k-1])
    return answer