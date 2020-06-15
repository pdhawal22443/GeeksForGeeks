'''Find next greater number with same set of digits
Given a number n, find the smallest number that has same set of digits as n and is greater than n.
If n is the greatest possible number with its set of digits, then print “not possible”.
Examples:
For simplicity of implementation, we have considered input number as a string.

Input:  n = "218765"
Output: "251678"

Input:  n = "1234"
Output: "1243"

Input: n = "4321"
Output: "Not Possible"

Input: n = "534976"
Output: "536479"

Algo ::
Following is the algorithm for finding the next greater number.
I) Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller
than the previously traversed digit. For example, if the input number is “534976”, we stop at 4 because
 4 is smaller than next digit 9. If we do not find such a digit, then output is “Not Possible”.

II) Now search the right side of above found digit ‘d’ for the smallest digit greater than ‘d’.
 For “534976″, the right side of 4 contains “976”. The smallest digit greater than 4 is 6.

III) Swap the above found two digits, we get 536974 in above example.

IV) Now sort all digits from position next to ‘d’ to the end of number. The number that
 we get after sorting is the output. For above example, we sort digits in bold 536974.
  We get “536479” which is the next greater number for input 534976.
'''
import pdb


#ex - 534976
lst = [5,3,4,9,7,6]

def arrange(lst):
    flag = 0

    for i in range(len(lst)-1,0,-1):
        if lst[i] > lst[i-1]:
            flag = 1 #this is to check that such number found
            break

    if flag == 0:
        print("Not Possible")
        exit(0)

    x = lst[i-1] #step-1 of algo

    #algo step2
    temp = lst[i]
    small = i
    for k in range(i+1,len(lst)):
        if lst[k-1] > x and lst[small] > lst[k]:
            small = k

    #step 3
    lst[i-1],lst[small] = lst[small],lst[i-1]

    pdb.set_trace()

    res = lst[0:i] + sorted(lst[i:])
    print(''.join(map(str,res)))

arrange(lst)






