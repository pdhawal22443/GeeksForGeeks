'''
https://www.geeksforgeeks.org/maximum-size-subset-given-sum/

This is an extended version of subset sum problem. Here we need to find size of maximum size subset whose sum is equal to given sum.

Examples:

Input : set[] = {2, 3, 5, 7, 10, 15},
         sum  = 10
Output : 3
The largest sized subset with sum 10
is {2, 3, 5}

Input : set[] = {1, 2, 3, 4, 5}
         sum = 4
Output : 2

'''


def getSubs(arr):
    if arr == []:
        return [[]]

    x = getSubs(arr[1:])

    return (x + [[arr[0]] + y for y in x ])



def getMaxSubArrWithGivenSum(arr,target_sum):

    subs = getSubs(arr)
    max_subset = 0

    for i in subs:
        if sum(i) == target_sum:
            if len(i) > max_subset:
                max_subset = len(i)

    return max_subset

print(getMaxSubArrWithGivenSum([1, 2, 3, 4, 5],4))