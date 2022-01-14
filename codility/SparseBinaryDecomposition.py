def adjacentSet(n):
    return (n & (n >> 1))


def solution(N):

    for n in range(0, int((N)/2)):
        
        if  not adjacentSet(n):
            num = n 
        else:
            continue
        
        if  not adjacentSet(N- n) :
            compl = N - n 
        else:
             continue

        if (num + compl) == N :
            return num
        
    return -1