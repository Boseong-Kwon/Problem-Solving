def solution(s):
    answer = True
    flag = 0
    for i in s:
        if i == '(':
            flag += 1
        if i ==')':
            if flag > 0:
                flag -= 1
            elif flag <= 0:
                answer = False
    if flag != 0:
        answer = False

    return answer