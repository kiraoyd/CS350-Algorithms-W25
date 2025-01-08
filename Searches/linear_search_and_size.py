#Write the search function to iterate over a collection of unique numbers,
#and determine if the parameter 'target' exists in the collection
#Assume must DETERMINE the size of the collection (total number of elements) in the function body
#When considering the formula for the approximate amount of work, the number of elements
#in a collection is represented as 'n'.
def search_and_size (collection, target):
    index = 0 #constant time, once per function call

    #To find the size of our collection List,
    #every element must be touched once: a total of 'n' times.
    #The python len() function does this work for us.
    #So it ADDS in 'n' more operations to our
    #approximate total work for linear search: 3n + 2 + n.
    #Simplified, this becomes 4n + 2.
    size_collection = len(collection)

    #This loop is where the bulk of the work is done
    #Specifically, the work that is DEPENDENT on how big our collection List is.
    #The size_collection value is our 'n', it can be small or very large.
    while index < size_collection:.
        if collection[index] == target: #constant time, once per iteration
            return index #constant time, once per function call
        index += 1 #constant time, once per iteration

    return -1 #constant time, once per function call

def main():
    data = [10,5,1,2,800,0]
    target = 800

    location_found = search_and_size(data, target)

    if location_found < 0:
        print(f"The target {target} is not found in this collection.")
    else:
        print(f"We found {target} at {location_found}.")

main()