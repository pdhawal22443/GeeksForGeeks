'''
https://www.geeksforgeeks.org/find-the-total-guests-that-are-present-at-the-party/

A person hosts a party and invites N guests to it. However, each guest has a
condition, that each guest ‘Gi’ only stays at the party if there are at least
‘Pi’ people already at the party, otherwise leaves. The total number of guests N
and the number of people each guest needs ‘Pi’ are given as input for each guest.
The task is to find the total guests that are present at the party. It is also
given that the guests arrive at the party in the order given in the array ‘Pi’

Examples:

Input: N = 5, Pi = {1, 0, 2, 1, 3}
Output: 2
Explanation:
Since 5 guests are invited to the party.
Total guest present initially = 0

For Guest number 1:
The 1st guest needs at least 1 person,
since he is the first to arrive,
and there is no one else, so he leaves.
Therefore, Total guest so far = 0

For Guest number 2:
The 2nd guest needs 0 people, so he stays.
Therefore, Total guest so far = 0 + 1 = 1

For Guest number 3:
The 3rd guest needs at least 2 people,
And there are still only 1 guest present,
so he leaves.
Therefore, Total guest so far = 1 + 0 = 1

For Guest number 4:
The 4th guest needs at least 1 people,
And there is 1 guest present, so he stays.
Therefore, Total guest so far = 1 + 1 = 2

For Guest number 5:
The 5th guest needs at least 3 people,
And there is only 2 guest present, so he leaves.
Therefore, Total guest so far = 2 + 0 = 2

Total guests that are present at the party = 2.

Input: N = 3, Pi = {0, 2, 1}
Output: 2
Explanation:
Since 3 guests are invited to the party.
Total guest present initially = 0

For Guest number 1:
The 1st guest needs 0 people, so he stays.
Therefore, Total guest so far = 1

For Guest number 2:
The 2nd guest needs at least 2 people,
And there are still only 1 guest present,
so he leaves.
Therefore, Total guest so far = 1 + 0 = 1

For Guest number 3:
The 3rd guest needs at least 1 people,
And there is 1 guest present, so he stays.
Therefore, Total guest so far = 1 + 1 = 2

Total guests that are present at the party = 2.
'''

def guests(arr,num):
    guest_count = 0

    for i in range(0,num):
        if arr[i] == guest_count:
            guest_count += 1

    return guest_count

print(guests([0,2,1],3))