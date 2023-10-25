def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer+= A[i]*B[i]
    #for i in range(len(A)):
    #    M = max(A)
    #    m = min(B)
    #    answer += M*m
    #    A[A.index(M)] = 0
    #    B[B.index(m)] = 1001

    return answer