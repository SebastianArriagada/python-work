from math import ceil,floor

def solution(A, B, K):
    # write your code in Python 3.6
    
    first = ceil(A/K)
    last = floor(B/K)

    if first > B:
        return 0
    
    if first == last:
        return 1
    
    return (last-first +1)

    """
    
Task Score
100%
Correctness
100%
Performance
100%

Detected time complexity:
O(1)
expand allExample tests
▶example
A = 6, B = 11, K = 2✔OK
expand allCorrectness tests
▶simple
A = 11, B = 345, K = 17✔OK
▶minimal
A = B in {0,1}, K = 11✔OK
▶extreme_ifempty
A = 10, B = 10, K in {5,7,20}✔OK
▶extreme_endpoints
verify handling of range endpoints, multiple runs✔OK
expand allPerformance tests
▶big_values
A = 100, B=123M+, K=2✔OK
▶big_values2
A = 101, B = 123M+, K = 10K✔OK
▶big_values3
A = 0, B = MAXINT, K in {1,MAXINT}✔OK
▶big_values4
A, B, K in {1,MAXINT}✔OK

"""