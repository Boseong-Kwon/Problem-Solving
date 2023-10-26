def solution(s):
    answer = []
    deleted_zero = 0
    trials = 0
    while(s!='1'):
        for i in s:
            if(i=='0'): deleted_zero +=1
        s = s.replace("0","")
        num = len(s)
        temp = ""
        while(num != 0):
            concat_num = num%2
            num = num//2
            temp = str(concat_num) + temp 
        s = temp
        trials += 1
    answer.append(trials)
    answer.append(deleted_zero)
    return answer