'''
https://www.geeksforgeeks.org/find-the-point-where-maximum-intervals-overlap/

Consider a big party where a log register for guest’s entry and exit times is maintained. Find the time at which there are maximum guests in the party. Note that entries in register are not in any order.
Example :

Input: arrl[] = {1, 2, 9, 5, 5}
       exit[] = {4, 5, 12, 9, 12}
First guest in array arrives at 1 and leaves at 4,
second guest arrives at 2 and leaves at 5, and so on.

Output: 5
There are maximum 3 guests at time 5.
'''

def maximumOverlap(entry,exit):
    temp_arr = []

    time = 0
    max_guests = 1
    guest = 1

    for i in range(0,len(entry)):
        temp_arr.append([entry[i],exit[i]])

    temp_arr = sorted(temp_arr)

    for i in range(1,len(temp_arr)):
        if temp_arr[i][0] < temp_arr[i-1][1] and temp_arr[i][1] > temp_arr[i-1][1]:
            guest += 1
        if guest > max_guests:
            max_guests = guest
            time = temp_arr[i-1][0]

    return ([time,max_guests])



print(maximumOverlap([1, 2, 9, 5, 5],[4, 5, 12, 9, 12]))