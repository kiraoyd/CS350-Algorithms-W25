# The Memoized (DP) implementation of Least Exact Change (LEC)
# With only 3 coin denominations: 1-coin, 3-coin, 4-coin
# where 'n' represents the total number of pennies you want to make LEC from
def change_memo(n, table):
    #base cases
    if n == 0:
        return
    if table[n] != -1: #a valid answer is in the table
        return table[n] #no work needed, return the answer


    #If you are the first one to encounter this value of n...
    #Then it is your responsibility to solve for it
    #Make some kids to do your work
    a = change_memo(n-4, table) #pick up a 4-coin
    b = change_memo(n-3, table) #pick up a 3-coin
    c = change_memo(n-1, table) #pick up a 1-coin

    #Which kid ends up picking up the least amount of coins for their subproblem?
    least = a
    if b < least:
        least = b
    if c < least:
        least = c

    #DON'T FORGET: add your answer to the table to set up future generations
    table[n] = 1 + least #add one to account for the fact that we must pick up one coin at this call

    #THEN return your answer up the callstack
    return 1 + least


def main():
    n = int(input("Enter the total number of pennies you have: "))

    table = [-1] * (n+1) #makes a List of size n+1, populated with -1s

    #Populate table with base cases
    table[1] = 1
    table[2] = 2
    table[3] = 1
    table[4] = 1

    print(f"The table after setting base cases: {table}")

    answer = change_memo(n, table)

    print(f"The table after memoizing: {table}")

    print(f"You can make least exact change from {n} pennies, in just {answer} coins.")

main()