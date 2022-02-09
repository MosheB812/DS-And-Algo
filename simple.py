# Check if there are two numbers in an array that sum up to a given value.
# Return TRUE if two numbers add up to sum, otherwise FALSE.
# Do both sorted and unsorted arrays.
def funcSorted(arr, sum):
    low = 0
    high = len(arr)-1

    while (low < high):
        ans = arr[low] + arr[high]

        if (ans == 8):
            return 'YES'
        elif (ans < sum):
            low += 1
        elif (ans > sum):
            high -= 1

    return 'NO'


def funcUnsorted(arr, sum):
    comp = []

    for num in arr:
        if (num in comp):
            return 'YES'
        else:
            comp.append(sum-num)

    return 'NO'


print(funcUnsorted([8, 1, 6, 98, 4, 6, 2, 86, 3, 1, 7], 8))
