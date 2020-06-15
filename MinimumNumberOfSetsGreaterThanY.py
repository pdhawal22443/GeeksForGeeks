'''
https://www.geeksforgeeks.org/minimum-number-of-sets-with-numbers-less-than-y/

Given a string of consecutive digits and a number Y, the task is to find the
number of minimum sets such that every set follows the below rule:

Set should contain consecutive numbers
No digit can be used more than once.
The number in the set should not be more than Y.
Examples:

Input: s = "1234", Y = 30
Output: 3

Three sets of {12, 3, 4}


Input: s = "1234", Y = 4
Output: 4
Four sets of {1}, {2}, {3}, {4}
'''

import pdb
#pdb.set_trace()

def minSets(test_string,target_sum):
    i = 0
    min_count = len(test_string)
    count = 1
    while i < len(test_string)-1:
        if int(test_string[i] + test_string[i+1]) < target_sum:
            count += 1
            i += 2
        else:
            count += 1
            i += 1

    if count < min_count:
        min_count = count

    return min_count

print(minSets('1234',4))


