def adjacentSet(n):
    return (n & (n >> 1))


def solution(N):

    if N == 0:
        return 0

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

"""

Task Score
50%
Correctness
80%
Performance
20%

    
Detected time complexity:
O(N * log(N))
expand allExample tests
▶example1
example test n=26✔OK
expand allCorrectness tests
▶simple1
n=1166✔OK
▶simple2
n=561892✔OK
▶simple3
n=1031✔OK
▶small_power_of_two_minus_one
n=1023✔OK
▶extreme
n <= 5✘WRONG ANSWER
got -1, but solution exists for example 1 (1=1+0)
expand allPerformance tests
▶medium1
n=74901729✘TIMEOUT ERROR
running time: 0.252 sec., time limit: 0.144 sec.
▶medium2
n=216188401✘TIMEOUT ERROR
running time: 3.580 sec., time limit: 0.144 sec.
▶power_of_two_minus_one
n=536870912✔OK
▶big_random
n=~1000000000✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
▶maximal
n=1000000000✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.    
    
"""