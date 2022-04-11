def solution(A):
    
    numberDic = {}
    numCount = 0
    for n in A:
        if n not in numberDic:
            numberDic[n] = 0
            numCount += 1
    
    return numCount


"""
Task Score
100%
Correctness
100%
Performance
100%


O(N*log(N)) or O(N)
expand allExample tests
▶example1
example test, positive answer✔OK
expand allCorrectness tests
▶extreme_empty
empty sequence✔OK
▶extreme_single
sequence of one element✔OK
▶extreme_two_elems
sequence of three distinct elements✔OK
▶extreme_one_value
sequence of 10 equal elements✔OK
▶extreme_negative
sequence of negative elements, length=5✔OK
▶extreme_big_values
sequence with big values, length=5✔OK
▶medium1
chaotic sequence of value sfrom [0..1K], length=100✔OK
▶medium2
chaotic sequence of value sfrom [0..1K], length=200✔OK
▶medium3
chaotic sequence of values from [0..10], length=200✔OK
expand allPerformance tests
▶large1
chaotic sequence of values from [0..100K], length=10K✔OK
▶large_random1
chaotic sequence of values from [-1M..1M], length=100K✔OK
▶large_random2
another chaotic sequence of values from [-1M..1M], length=100K✔OK
"""