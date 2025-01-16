#recursively traverses array / List from back
#to front, summing the data

def sum_recursive_backwards(array, n):
    if n < 0:
        return 0
    return array[n] + sum_recursive_backwards(array, n-1)

def main():
    array = [1,2,3,4,5]
    length = len(array)
    index = 0
    result = sum_recursive_backwards(array, length-1)
    print(f"The sum of data is: {result}")

main()