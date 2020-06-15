'''
#Convert a number m to n with minimum operations. The operations allowed are :
#Multiply by 2, i.e., do m = 2 * m
#Subtract 1, i.e., do m = m – 1
#Print -1 if it is not possible to convert.

Input : m = 3, n = 11
Output : 3
1st operation: *2 = 3*2 = 6
2nd operation: *2 = 6*2 = 12
3rd operation: -1 = 12-1 = 11

Input : m = 15, n = 20
Output : 6
1st operation: -1 '5' times = 15 + (-1*5) = 10
2nd operation: *2 = 10*2 = 20

Input : m = 0, n = 8
Output : -1
Using the given set of operations 'm'
cannot be converted to 'n'

Input : m = 12, n = 8
Output : 4

The idea is based on below facts.
1) If m is less than 0 and n is greater than 0, then not possible.
2) If m is greater than n, then we can reach n using subtractions only.
3) Else (m is less than n), we must do m*2 operations. Following two cases arise.
……a) If n is odd, we must do a -1 operation to reach it.
……b) If n is even, we must do a *2 operation to reach it.
'''


def minSteps(m,n):
    if (m==n):
        return 0
    #If m is less than zero it is not possible to make m => n
    if m < 0 and n > 0:
        return -1
    #If m is greater than m
    if m > n:
        return m - n
    # if n is ODD
    if n%2 != 0 :
        return 1 + minSteps(m,n+1)
    # if n is Even
    else:
        return 1 + minSteps(m,n//2)



print(minSteps(15,20))




