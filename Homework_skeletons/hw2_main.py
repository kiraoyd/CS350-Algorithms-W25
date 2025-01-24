
import sys
def main():

    #--------------SASI'S CODE TO GRAB AND PARSE COMMAND LINE ARGUMENTS----------------#
    # This code brings in elements in the test array,the values for the length of the array, and the value for 'k'
    # Command Line Example:
    #           For the array with 5 elements: [10,2,34,7,10], when k = 4 the command line to enter is:
    #           python3 main.py 5 4 10 2 34 7 10
    # They are saved in the variables: 'elements' (a Python List), 'num_elements', and 'k',  respectively.
    # You will not need to alter Sasi's code at all
    # Call the function you write, after Sasi's code, and pass  the 'elements', 'num_elements', and 'k' variables
    # to that functions call

    # Check if enough arguments are passed
    if len(sys.argv) < 4:
        print("Usage: python script.py <number_of_elements> <value of k> <element 1> <element 2> ... <element n>")
        sys.exit(1)

    # Parse the number of elements
    num_elements = int(sys.argv[1])
    # Parse the value of k
    k = int(sys.argv[2])
    # Check if the value of k is valid
    if ((k < 1) or (k > num_elements)):
        print("Error: Invalid k value.")
        sys.exit(1)

    # Check if the number of elements provided matches the given array length
    if len(sys.argv) != (num_elements + 3):
        print("Error: Number of provided elements does not match the given array size.")
        sys.exit(1)
    elements = sys.argv[3:]

    # Convert elements to integers
    elements = list(map(int, elements))

    #-----------------------------------END OF SASI'S CODE--------------------------------#

    # 'elements' now contains the test array that was entered as command line arguments
    # 'k' now contains the value for k
    # 'num_elements' now contains the value for the length of the array
    # Verify this (remove these test print lines before submitting):
    print(f"You entered this test array: {elements}")
    print(f"It contains {num_elements} elements.")
    print(f"The k value: {k}.")


    # TODO - CALL YOUR FUNCTION(S) AND OUTPUT RESULTS HERE:
    # Call the appropriate subroutines /functions or do the required processing with the input array
    # Pass in 'elements', 'num_elements' and 'k'

    # Print the result(s)




#Kickstarts the main() calling routine
if __name__ == "__main__":
    main()