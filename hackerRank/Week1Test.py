from math import ceil

def findMedian(arr):
    
    medianPosition = ceil( len(arr) / 2 ) - 1
    
    arr.sort()
    
    return arr[medianPosition ]

def flipColumn(arr, n , column):
    for i in range(n):
        bottomPos = (2*n) - i - 1
        
        arr[i][column], arr[bottomPos][column] = arr[bottomPos][column], arr[i][column]
    
    return arr 

def flipRow(arr, row):
    arr[row].reverse()
    
    return arr

def boxSum(arr, n):
    sume = 0
    for i in range(n):
        for j in range(n):
            sume += arr[i][j]
    
    return sume

def checkColumn(matrix, n):
    maxSum = boxSum(matrix,n)
    actualSum = 0
    for column in range(2*n):
        maxTop = 0
        maxBottom = 0
        
        for row in range(n):
            bottomPosition = 2*n - row - 1
            if matrix[row][column] > maxTop:
                maxTop =matrix[row][column]
            if matrix[bottomPosition][column] > maxBottom:
                maxBottom =  matrix[bottomPosition][column]
        if maxBottom > maxTop:
            print(column)
            matrix = flipColumn(matrix, n , column)
            actualSum = boxSum(matrix,n)
    if actualSum > maxSum:
        return matrix, actualSum
    return matrix, maxSum

def checkRow(matrix,n):
    maxSum = boxSum(matrix,n)
    actualSum = 0
    for row in range(n):
        maxLeft = 0
        maxRight = 0
        matrix , actualSum= checkColumn(matrix, n)
        for column in range(n):
            rightPosition = 2*n - column - 1
            if matrix[row][column] > maxLeft:
                maxLeft = matrix[row][column]
            if matrix[row][rightPosition] > maxRight:
                maxRight = matrix[row][rightPosition]
        if maxRight > maxLeft:
            matrix = flipRow(matrix,row)
            matrix,actualSum = checkColumn(matrix, n)
            if actualSum < boxSum(matrix,n):
                actualSum = boxSum(matrix,n)
        if actualSum > maxSum:
            maxSum = actualSum
            
    return matrix,maxSum
    
def flippingMatrix(matrix):
    n = int(len(matrix)/2)
    
    maxSum = boxSum(matrix,n)
   
    matrix, actualSum = checkColumn(matrix, n)
    
    if actualSum > maxSum:
        maxSum = actualSum
    
    matrix, actualSum  = checkRow(matrix,n)
    
    if actualSum > maxSum:
        maxSum = actualSum
    
    
    for i in range(2*n):
        print(matrix[i])
    
    return boxSum(matrix,n)
    