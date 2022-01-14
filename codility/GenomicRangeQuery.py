from collections import Counter
def solution(S, P, Q):

    minDNA = []
    dnaSplit = list(S)

    for p, q in zip(P,Q ):
        dna = dnaSplit[(p):(q+1)]
        dna = Counter(dna)
        if "A" in dna:
            minDNA.append(1)
        elif "C" in dna:
            minDNA.append(2)
        elif "G" in dna:
            minDNA.append(3)
        else:
            minDNA.append(4) 
    
    return minDNA


"""
Detected time complexity:
O(N * M)
expand allExample tests
▶example
example test✔OK
expand allCorrectness tests
▶extreme_sinlge
single character string✔OK
▶extreme_double
double character string✔OK
▶simple
simple tests✔OK
▶small_length_string
small length simple string✔OK
▶small_random
small random string, length = ~300✔OK
expand allPerformance tests
▶almost_all_same_letters
GGGGGG..??..GGGGGG..??..GGGGGG✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
▶large_random
large random string, length✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
▶extreme_large
all max ranges✘TIMEOUT ERROR
Killed. Hard limit reached: 7.000 sec.



"""