
def solution(N, A):

    arr = [0]*N
    maxNum = 0
    actMax = 0
    for token in A:

        if (token) <= N:
            if arr[token - 1] < maxNum:
                arr[token - 1] = (maxNum + 1)
            else:
                arr[token - 1] += 1

            if arr[token - 1] > actMax:
                actMax = arr[token - 1]
        else:
            maxNum = actMax

    for i in range(len(arr)):
        if arr[i] < maxNum:
            arr[i] = maxNum

    return arr


"""
Correctness: 100%
Performance: 100%
Total score: 100%

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
all max_counter operations ✔OK

"""
