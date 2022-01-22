from math import ceil

def findMedian(arr):
    
    medianPosition = ceil( len(arr) / 2 ) - 1
    
    arr.sort()
    
    return arr[medianPosition ]