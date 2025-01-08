#Write the search function to iterate over a collection of unique numbers,
#and determine if the parameter 'target' exists in the collection.
#Assume we have the size of the collection (total number of elements) as a parameter.

#When considering the formula for the approximate amount of work, the number of elements
#in a collection is represented as 'n'.
#If we do a rough count of the constant time operations, to approximate the amount of
#work done when this function runs, we get 3n + 2.
#The constant time operations inside the n-dependent loop (in this case, 3 of them)
#become a constant multiplier for 'n'.
#The 2 operations outside the n-dependent loop are simply added into to the equation.
def search (collection, target, size_collection):
    index = 0 #constant time, once per function call

    #This loop is where the bulk of the work is done.
    #Specifically, the work that is DEPENDENT on 'n', on how big our collection List is.
    while index < size_collection:
        if collection[index] == target: #constant time, once per iteration
            return index #constant time, once per function call
        index += 1 #constant time, once per iteration

    return -1 #constant time, once per function call

def main():
    data = [10,5,1,2,800,0]
    target = 800
    size = len(data)

    location_found = search(data, target, size)

    if location_found < 0:
        print(f"The target {target} is not found in this collection.")
    else:
        print(f"We found {target} at index {location_found}.")

main()