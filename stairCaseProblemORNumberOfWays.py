#GeeksForGeeks
'''https://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/'''
'''Algorithm learnt - https://www.youtube.com/watch?v=CFQk7OQO_xM'''
'''
Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps.
Examples:

Input: n = 3
Output: 4
Explantion:
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step

Input: n = 4
Output: 7
Explantion:
Below are the four ways
 1 step + 1 step + 1 step + 1 step
 1 step + 2 step + 1 step
 2 step + 1 step + 1 step 
 1 step + 1 step + 2 step
 2 step + 2 step
 3 step + 1 step
 1 step + 3 step
'''
#it is solved using recursion

def waysToReach(num):
    #base Case
    if num < 0:
        return 0

    if num == 0:
        return 1

    sum =  (waysToReach(num - 1) + waysToReach(num - 2) + waysToReach(num - 3))
    return sum

test = 4
print(waysToReach(test))


