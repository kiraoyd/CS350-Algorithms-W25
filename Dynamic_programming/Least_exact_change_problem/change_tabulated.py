# The Tabulated (DP) implementation of Least Exact Change (LEC)
# With only 3 coin denominations: 1-coin, 3-coin, 4-coin
# where 'n' represents the total number of pennies you want to make LEC from
def change_tab(n, table):
    i = 5 #start an index tracker at the smallest, UNSOLVED subproblem

    #Keep solving each subproblem, working our way up to the biggest, n-problem
    while i <= n:
        #Look back into the table to query the earlier solved subproblems
        a = table[i-4] #pick up a 4-coin
        b = table[i-3] #pick up a 3-coin
        c = table[i-2] #pick up a 1-coin

        #Which previous answer is the least number of coins?
        least = a
        if b < least:
            least = b
        if c < least:
            least = c

        #DON'T FORGET: add your answer to the table to set up future generations
        table[i] = 1 + least #add one to account for the fact that we must pick up one coin at this call

        #solve the next smallest unsolved subproblem
        i = i + 1

    #After the loop finishes, the answer for n, will be stored at table[n]
    return table[n]


def main():
    n = int(input("Enter the total number of pennies you have: "))

    table = [-1] * (n+1) #makes a List of size n+1, populated with -1s

    #Populate table with base cases
    table[1] = 1
    table[2] = 2
    table[3] = 1
    table[4] = 1

    print(f"The table after setting base cases: {table}")

    answer = change_tab(n, table)

    print(f"The table after tabulating: {table}")

    print(f"You can make least exact change from {n} pennies, in just {answer} coins.")

main()