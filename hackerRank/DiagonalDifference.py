"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:
1 2 3
4 5 6
7 8 9

he left-to-right diagonal 1 + 5 + 9 = 15 . The right to left diagonal 3 + 5 + 9 = 17. Their absolute difference is |15 - 17| = 2.

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

"""

def diagonalDifference(arr):
    decresingDiagonal = 0
    increasingDiagonal = 0
    lenght = len(arr)

    for i in range(lenght):
        decresingDiagonal += arr[i][i]
        increasingDiagonal += arr[ i ][lenght - i - 1]
     
    return abs(decresingDiagonal - increasingDiagonal)
        