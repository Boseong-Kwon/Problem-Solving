def binary(n):
    ret = ""
    while(n != 0):
        ret = str(n%2) + ret
        n = n//2
    return ret

def num_counter(n):
    counter = 0
    for i in n:
        if(i == '1'):
            counter += 1
    return counter

def solution(n):
    input_one = num_counter(binary(n))
    answer = n
    while(1):
        answer +=1
        if(input_one == num_counter(binary(answer))):
            break
    return answer