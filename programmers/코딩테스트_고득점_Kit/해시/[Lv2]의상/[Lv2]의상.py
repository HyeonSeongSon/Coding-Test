from collections import defaultdict

def solution(clothes):
    cloth_dic = defaultdict(list)
    for name, kind in clothes:
        cloth_dic[kind].append(name)
    cnt = [len(val) for val in cloth_dic.values()]
    answer = 1
    for i in cnt:
        answer *= i+1
    return answer - 1