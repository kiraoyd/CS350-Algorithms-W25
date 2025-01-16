#recursively traverses array / List from front
#to back, summing the data
#mimicking our iterative, loop version

def sum_recursive_forwards(array, n, index):
    if index == n:
        return 0
    return array[index] + sum_recursive_forwards(array, n, index+1)

def main():
    array = [1,2,3,4,5]
    length = len(array)
    index = 0
    result = sum_recursive_forwards(array, length, index)
    print(f"The sum of data is: {result}")

main()