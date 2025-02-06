# The naiive recurisve implementation of Least Exact Change (LEC)
# With only 3 coin denominations: 1-coin, 3-coin, 4-coin
# where 'n' represents the total number of pennies you want to make LEC from
def change(n):
    #base cases
    if n == 4 or n == 3 or n ==1:
        return 1 #just pick up one of the three coin denominations

    #make some kids to do your work
    a = change(n-4) #pick up a 4-coin
    b = change(n-3) #pick up a 3-coin
    c = change(n-1) #pick up a 1-coin

    #Which kid ends up picking up the lease amount of coins for their subproblem?
    least = a
    if b < least:
        least = b
    if c < least:
        least = c

    return 1 + min #add one to account for the fact that we must pick up one coin at this call

