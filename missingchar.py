#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def missingCharacters(s):
    # Write your code here
    output = "0123456789abcdefghijklmnopqrstuvwxyz"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(s)):
        try:
            value = int(s[i])
            if value >= 0 & value <= 9:
                output = output.replace(s[i],'');
        except:
            for l in range(len(alphabet)):
                if alphabet[l] == s[i]:
                    output = output.replace(s[i],'')
    return output

if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
