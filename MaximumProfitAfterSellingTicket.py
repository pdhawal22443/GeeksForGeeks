'''
https://www.geeksforgeeks.org/maximize-the-profit-after-selling-the-tickets/?ref=leftbar-rightbar

Maximize the profit after selling the tickets
Given an array seats[] where seat[i] is the number of vacant seats in the ith row in a stadium for a cricket match. There are N people in a queue waiting to buy the tickets. Each seat costs equal to the number of vacant seats in the row it belongs to. The task is to maximize the profit by selling the tickets to N people.

Examples:

Input: seats[] = {2, 1, 1}, N = 3
Output: 4
Person 1: Sell the seat in the row with
2 vacant seats, seats = {1, 1, 1}
Person 2: All the rows have 1 vacant
seat each, seats[] = {0, 1, 1}
Person 3: seats[] = {0, 0, 1}


'''


def maxProfit(arr,num_person):
    max_profit = 0
    tckt_sold = 0

    while tckt_sold < num_person:
        arr = sorted(arr)

        max_profit += arr[-1]

        arr[-1] = arr[-1] - 1

        tckt_sold += 1

    return max_profit

print(maxProfit( [2, 3, 4, 5, 1],6))