'''
Given an integer element ‘N’, the task is to find the minimum number of operations
that need to be performed to make ‘N’ equal to 1.
The allowed operations to be performed are:

Decrement N by 1.
Increment N by 1.
If N is a multiple of 3, you can divide N by 3.

Algo :
Approach:

If the number is a multiple of 3, divide it by 3.
If the number modulo 3 is 1, decrement it by 1.
If the number modulo 3 is 2, increment it by 1.
There is an exception when the number is equal to 2, in this case the number should be decremented by 1.
Repeat the above steps until the number is greater than 1 and print the count of operations performed in the end.
'''

def minSteps(num):
    if num == 1:
        return 0

    if num == 2:
        return (1 + minSteps(num-1))

    if num%3 == 0:
        return (1 + minSteps(num//3))
    if num%3 == 1:
        return (1 + minSteps(num-1))
    if num%3 == 2:
        return (1 + minSteps(num+1))

print(minSteps(4))