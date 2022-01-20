"""

You will be given a list of 32 bit unsigned integers. Flip all the bits ( 1 -> 0 and 0 -> 1) and return the result as an unsigned integer.

Example

. We're working with 32 bits, so:
Take 1 for example, as unsigned 32-bits is 00000000000000000000000000000001 and doing the flipping we get 11111111111111111111111111111110 which in turn is 4294967294.


Return .

Function Description

Complete the flippingBits function in the editor below.

flippingBits has the following parameter(s):

int n: an integer
Returns

int: the unsigned decimal integer result
Input Format

The first line of the input contains , the number of queries.
Each of the next  lines contain an integer, , to process.
"""

def flippingBits(n):
    
    bitNumber = '{:032b}'.format(n)
    
    reverseBit = "".join([ "1" if bit == "0" else  "0" for bit in bitNumber])
    
    return int(reverseBit,2)
