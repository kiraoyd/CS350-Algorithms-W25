import sys
import math
def min_rotated(rotated, size):
    if size == 0:
        return -1 #empty array error flag

    start = 0 #points to the element all the way on the left
    end = size -1  #points to the element all the way to the right

    #BEST CASE: the array is rotated n-times, back to its original state
    #We can then find the minimum value in constant time (skipping the loop that's dependent on n)
    if rotated[start] < rotated[end]:
        #The array is already in min to max sorted order
        return rotated[start] #so the minimum is the first value

    #Every iteation, determine if the minimum val will be on the left or right subarray
    while start < end: #go until start == end, indicating a single element subarray
        mid = math.floor((start+end) / 2)
        #the following check deduced from examplifying all rotations of a toy example array
        if rotated[mid] > rotated[end]:
            #When this is true, the pivot is guaranteed to be in the right subarray, so throw out the left
            start = mid + 1
        else:
            #The pivot is guaranteed to be in the left subarray (we count the array[mid] value as part of the left sub array), so throw out the right
            end = mid #We keep the value at array[mid], it is considered to be part of the left subarray

    #When the loop breaks, start and end point at the same element, and the subarry is just one element
    return rotated[start] 	#This will be the minimum value we have been searching for


def main():
    #--------------SASI'S CODE TO GRAB AND PARSE COMMAND LINE ARGUMENTS----------------#
    # This code brings in elements in the test array, and the values for the length of the array
    # They are saved in the variables: 'elements' (a Python List), and 'num_elements' respectively.
    # Command Line Example:
    #           For this sorted, shifted array with 7 elements: [4, 5, 6, 7, 0, 1, 2], the command line to enter is:
    #           python3 main.py 7 4 5 6 7 0 1 2
    # You will not need to alter Sasi's code in anyway
    # Call the function you write, after Sasi's code, and pass the 'elements' and 'num_elements' variables
    # to that functions call

    # Check if enough arguments are passed
    if len(sys.argv) < 2:
        print("Usage: python script.py <number_of_elements> <element1> <element2> ...")
        sys.exit(1)

    # Parse the number of elements
    num_elements = int(sys.argv[1])

    # Check if the number of elements provided matches the given array length
    elements = sys.argv[2:]
    if len(elements) != num_elements:
        print("Error: Number of provided elements does not match the given array size.")
        sys.exit(1)

    # Convert elements to integers
    elements = list(map(int, elements))


#------------------------------END OF SASI'S CODE--------------------------#
    #'elements' now contains the test array that was entered as command line arguments
    #'num_elements' now contains the value for the length of the array
    print(f"You entered this test array: {elements}")
    print(f"It contains {num_elements} elements.")


    # TODO - CALL YOUR FUNCTION(S) AND OUTPUT RESULTS HERE:
    # Call the appropriate subroutines /functions or do the required processing with the input array
    # Pass in 'elements', 'num_elements' and 'k'
    min_val = min_rotated(elements, num_elements)
    # Print the result(s)
    print(min_val)

#Kickstarts the main() calling routine
if __name__ == "__main__":
    main()