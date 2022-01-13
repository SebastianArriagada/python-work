
def solution(N, A):
   
    arr = [0]*N
 
    maxNum = 0
    for token in A:
        
        if (token) <= N:
            arr[token - 1] += 1
            if arr[token - 1] > maxNum:
                maxNum += 1
        
        else:
            arr = [maxNum]*N

    return arr

"""
Correctness: 100%
Performance: 80%
Total score: 88%

Detected time complexity:
O(N + M)

expand allExample tests

example test ✔OK

expand allCorrectness tests

all max_counter operations ✔OK
only one counter ✔OK
small random test, 6 max_counter operations ✔OK
small random test, 10 max_counter operations ✔OK

expand allPerformance tests

medium random test, 50 max_counter operations ✔OK
medium random test, 500 max_counter operations ✔OK
large random test, 2120 max_counter operations ✔OK
large random test, 10000 max_counter operations ✔OK
all max_counter operations ✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.

"""