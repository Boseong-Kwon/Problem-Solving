def solution(n):
    answer = 0
    for i in range(n):
        counter = i+1
        adder = 0
        while(adder < n):
            adder += counter
            counter += 1
            if(adder == n):
                answer += 1
                break
    return answer