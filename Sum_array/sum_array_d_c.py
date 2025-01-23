#A silly way to sum up an array, but a nice simple example
#of recursive Divide and Conquer at work
#Big O(n)
def sum_array_dc(array, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    left_sum = sum_array_dc(array, start, mid-1)
    right_sum = sum_array_dc(array, mid+1, end)
    return left_sum + right_sum + array[mid]

def main():
    array = [1,2,3,4,5]
    start = 0
    end = len(array) -1
    result = sum_array_dc(array, start, end)
    print(f"The sum of these numbers {array} is {result}.")

main()