'''
https://www.geeksforgeeks.org/reduce-a-number-to-1-by-performing-given-operations/
Given a number N. The task is to reduce the given number N to 1
in the minimum number of steps. You can perform any one of the below operations in each step.

Operation 1: If the number is even then you can divide the number by 2.
Operation 2: If the number is odd then you are allowed to perform either (n+1) or (n-1).
You need to print the minimum number of steps required to reduce the number N to 1 by
 performing the above operations.'''

def minSteps(num):
    if num == 1:
        return 0

    if num %2 ==0:
        return (1 + minSteps(num//2))
    else:
        return 1 + (min(minSteps(num+1) , minSteps(num-1)))

print(minSteps(15))