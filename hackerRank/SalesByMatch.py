"""

There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example

There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

int n: the number of socks in the pile
int ar[n]: the colors of each sock
Returns

int: the number of pairs
Input Format

The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers, , the colors of the socks in the pile.

Constraints

 where 

"""

from collections import Counter
from math import floor

def sockMerchant(n, ar):
    dict_socks = Counter(ar)
    parAmount = 0
    for sock in dict_socks:
        parAmount += floor(dict_socks[sock] / 2)
    
    return parAmount