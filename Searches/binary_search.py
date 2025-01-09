#Binary Search
#Given a 1D array of 'n' number of positive integers
#sorted in ascending order, and some target integer 'k'
#If k exists, return the index location where it can be found
#If k does not exist, return the fail flag of -1
#Note: Pythons array-like type is called a List

import math  #(or just use // division)
def binary_search(sorted, k, size):
    start = 0
    end = size -1
    #We must also check the situation where start equals end
    # to check the value of the last remaining element
    while start <= end:
        #calculate the midpoint, represents the index location
        # of the value in the array we want to check against k
        mid = math.floor((start + end) / 2)
        #run the checks
        if sorted[mid] == k:
            #We found k, return it's index location
            return mid
        #We did not find k, shrink the search space
        if k > sorted[mid]:
            #k must be in the right half (if it exists), so throw out the left
            start = mid + 1
            #end is unchanged, as it still points to the correct "upper end" of the new search space
        if k < sorted[mid]:
            #k must be in the left half (if it exists), so throw out the right
            end = mid - 1
            #start is unchanged, as it still points to the correct "lower end" of the search space

    #If we run the loop to completion, we didn't find k, return fail flag
    return -1

def main():
    array = [1,2,3,4,6]
    k = 6
    size = len(array)
    result = binary_search(array, k, size)

    if result < 0:
        print("Not found")
    else:
        print(f"We found {k} at index {result}")

#To run file: python3 binary_search.py
main()

