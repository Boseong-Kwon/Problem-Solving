def solution(n):
    first = 0
    second = 1
    temp = 0
    answer = 1
    for i in range(n-1):
        temp = second
        second = first + second
        first = temp
    answer = second % 1234567
    return answer