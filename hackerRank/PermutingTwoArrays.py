"""
here are two -element arrays of integers,  and . Permute them into some  and  such that the relation  holds for all  where .

There will be  queries consisting of , , and . For each query, return YES if some permutation ,  satisfying the relation exists. Otherwise, return NO.

Example
A = [0,1]
B = [0,2]
k = 1


A valid  is  and :  and . Return YES.

Function Description

Complete the twoArrays function in the editor below. It should return a string, either YES or NO.

twoArrays has the following parameter(s):

int k: an integer
int A[n]: an array of integers
int B[n]: an array of integers
Returns
- string: either YES or NO

Input Format

The first line contains an integer , the number of queries.

The next  sets of  lines are as follows:

The first line contains two space-separated integers  and , the size of both arrays  and , and the relation variable.
The second line contains  space-separated integers A[i].
The third line contains  space-separated integers B[i].

"""

def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse = True)
    
    for num1, num2 in zip(A,B):
        if num1 + num2 < k:
            return "NO"
        
    return "YES"