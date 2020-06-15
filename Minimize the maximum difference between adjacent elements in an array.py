'''
Minimize the maximum difference between adjacent elements in an array
Given a non-decreasing array arr[] and an integer K, the task is to remove K
elements from the array such that maximum difference between adjacent element is minimum.
Note: K < N – 2

Examples:
Input: arr[] = {3, 7, 8, 10, 14}, K = 2
Output: 2
Explanation:
After removing elements A[0] and A[4],
The maximum difference between adjacent elements is minimum.
After removing elements, the remaining array is [7, 8, 10]

Input: arr[] = [12, 16, 22, 31, 31, 38], K = 3
Output: 6
Explanation:
After removing elements A[3], A[4] and A[5],
The maximum difference between adjacent elements is minimum.
After removing elements, the remaining array is [12, 16, 22]

Idea is to remove
'''

# Python3 implementation to find the
# minimum of the maximum difference
# of the adjacent elements after
# removing K elements from the array
import sys
import pdb

INT_MAX = sys.maxsize
INT_MIN = -(sys.maxsize - 1)


# Function to find the minimum
# of the maximum difference of the
# adjacent elements after removing
# K elements from the array
def minimumAdjacentDifference(a, n, k):
    # Intialising the
    # minimum difference
    minDiff = INT_MAX

    # Iterating over all
    # subarrays of size n-k
    for i in range(k + 1):

        # Maximum difference after
        # removing elements
        maxDiff = INT_MIN
        for j in range(n - k - 1):
            for p in range(i, i + j + 1):
                maxDiff = max(maxDiff, a[p + 1] - a[p]);

                # Minimum Adjacent Difference
        minDiff = min(minDiff, maxDiff);

    return minDiff;

pdb.set_trace()
a = [3, 7, 8, 10, 14];
k = 2
print(minimumAdjacentDifference(a, len(a), k));
