#classic traversal to sum data in an array / List
def sum_iterative(array,n):
    sum = 0
    index = 0
    while index < n:
        sum += array[index]
        index += 1
    return sum

def main():
    array = [1,2,3,4,5]
    length = len(array)
    result = sum_iterative(array,length)
    print(f"The sum of data is: {result}")

main()
