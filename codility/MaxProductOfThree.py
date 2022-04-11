def solution(A):
    A.sort()
    
    mult1 = A[-1] * A[-2] * A[-3]
    mult2 = A[0] * A[1] * A[-1]

    if mult1 > mult2:
        return mult1
    else:
        return mult2

"""
Task Score
100%
Correctness
100%
Performance
100%

O(N * log(N))
expand allExample tests
▶example
example test✔OK
expand allCorrectness tests
▶one_triple
three elements✔OK
▶simple1
simple tests✔OK
▶simple2
simple tests✔OK
▶small_random
random small, length = 100✔OK
expand allPerformance tests
▶medium_range
-1000, -999, ... 1000, length = ~1,000✔OK
▶medium_random
random medium, length = ~10,000✔OK
▶large_random
random large, length = ~100,000✔OK
▶large_range
2000 * (-10..10) + [-1000, 500, -1]✔OK
▶extreme_large
(-2, .., -2, 1, .., 1) and (MAX_INT)..(MAX_INT), length = ~100,000✔OK
"""