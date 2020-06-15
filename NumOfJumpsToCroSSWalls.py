'''
https://www.geeksforgeeks.org/number-of-jumps-for-a-thief-to-cross-walls/
A thief trying to escape from a jail. He has to cross N walls each with
varying heights (every height is greater than 0). He climbs X feet every time.
But, due to the slippery nature of those walls, every time he slips back by Y feet.
Now the task is to calculate the total number of jumps required to cross all walls
and escape from the jail.

Examples :

Input : heights[] = {11, 11}
                X = 10;
                Y = 1;
Output : 4
He needs to make 2 jumps for first wall
and 2 jumps for second wall.

Input : heights[] = {11, 10, 10, 9}
                 X = 10;
                 Y = 1;
Output : 5
'''
import pdb
#pdb.set_trace()

def minJumps(arr,num1,num2):
    total_count = 0
    for i in arr:
        total_count = total_count + jumpsForAWall(i,num1,num2)

    return total_count



def jumpsForAWall(hight,num1,num2):
    i = 0
    count = 0

    if hight == num1 or hight < num1:
        return 1
    else:
        while i <= hight:
            i = i + (num1 - num2)
            count += 1
        return count

lst = [11,10,10,9]
print(minJumps(lst,10,1))