
def partition (array, start, end):
    pivot_value = array[end]
    i = start #index tracker to process the array
    p = start #tracks and holds the pivots final location

    #as long as we have elements in the array to examine
    while i < end:
        #is the value at the current index (i) less than the pivot value?
        if array[i] < pivot_value:
            #if it is, do the work to ensure that value is
            #to the LEFT of the placeholder (p)

            #swap...
            temp = array[p]
            array[p] = array[i]
            array[i] = temp

            #then advance p
            p += 1

        #the value at the current index has been processed
        #advance i to check the value at the next index
        i+=1

    #We break the loop once all non-pivot values have
    #been examined
    #so all that remains is to put the pivot in the right spot held by p
    #swap the value at array[p] with the pivot value
    array[end] = array[p]
    array[p] = pivot_value

    #quicksort needs to split recursively around the
    #LOCATION of the pivot value, so we return the index value of p
    return p


#The recursive Quicksort function USES partition at each call
def quicksort(array, start, end):
    #base case: one element, or invalid index values
    if start >= end:
        return

    #find the index to split around
    pivot_index = partition(array, start, end)

    #split left
    quicksort(array, start, pivot_index-1)
    #split right
    quicksort(array, pivot_index+1, end)

def main():
    #test quicksort
    #Note: Pythons array-like data structure is a List
    #Lists are passed by reference by default
    array = [3,10,5,4,8,9,3,20,1]
    print(f"The unsorted array is: {array}")
    start = 0
    end = len(array) - 1
    quicksort(array,start,end)
    print(f"Our sorted array is now: {array}")

main()