'''Diff Veriations in this question
https://www.geeksforgeeks.org/minimum-steps-minimize-n-per-given-condition/
'''

'''
Given a number n, count minimum steps to minimize it to 1 according to the following criteria:

If n is divisible by 2 then we may reduce n to n/2.
If n is divisible by 3 then you may reduce n to n/3.
Decrement n by 1.
Input : n = 10
Output : 3

Input : 6
Output : 2
'''
import pdb
pdb.set_trace()


# function to calculate min steps
def getMinSteps(num, memo):
    # base case
    if (num == 1):
        return 0
    if (memo[num] != -1):
        return memo[num]

    res = getMinSteps(num-1,memo)

    if (num%2 == 0):
        res = min(res,getMinSteps(num//2,memo))
    if (num%3 == 0):
        res = min(res,getMinSteps(num//3,memo))

    memo[num] = 1 + res
    return memo[num]




# This function mainly
# initializes memo[] and
# calls getMinSteps(n, memo)
def getsMinSteps(k):
    memo = [-1 for i in range(k + 1)]

    return getMinSteps(k,memo)


print(getsMinSteps(10))
