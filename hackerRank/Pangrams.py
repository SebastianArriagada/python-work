"""
Roy wants to improve his typing speed for programming contests. His friend told him to write the sentence "The quick brown fox jumps over the lazy dog" repeatedly because it is a pangram. (Pangrams are sentences constructed using all the letters of the alphabet, at least once.)

After writing the sentence many times, Roy got bored. So he started looking for other pangrams.

given a sentence Tell Roy if it's a pangram or not.

Input Format

The Input consists of a line containing .

Restrictions
The length of can be at most  and can contain spaces, lowercase and uppercase. Lowercase and uppercase letters of the same letter are considered the same letter.

Output format

Prints a line containing pangram if a is a pangram, otherwise it prints not pangram

"""

def pangrams(s):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for letter in alphabet:
        
        if ((letter) in s or letter.lower() in s):
            continue
        else:
            return "not pangram"
    
    return "pangram"