##################################################
# CHALLENGE 1
# Implement a function that removes all the even elements from a given list. Name it remove_even(lst).
# Input     - A list with random integers   [1,2,4,5,10,6,3]
# Output    - A list with only odd integers [1,5,3]
##################################################


def remove_even(lst):
    retLst = []
    for num in lst:
        if num % 2 == 1:
            retLst.append(num)

    return retLst


##################################################
# CHALLENGE 2
# Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).
# Input     - Two sorted lists                                                          [1,3,4,5] [2,6,7,8]
# Output    - A merged and sorted list consisting of all elements of both input lists   [1,2,3,4,5,6,7,8]
##################################################


def merge_lists(lst1, lst2):
    ind1 = 0
    ind2 = 0

    while(ind1 < len(lst1) and ind2 < len(lst2)):
        if(lst2[ind2] < lst1[ind1]):
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1
            ind2 += 1
        else:
            ind1 += 1

    if(ind2 < len(lst2)):
        lst1 = lst1 + lst2[ind2:]

    return lst1


##################################################
# CHALLENGE 3
# In this problem, you have to implement the find_sum(lst,k) function which will take a number k as input and return two numbers that add up to k.
# Input     - A list and a number k                                 [1,21,3,14,5,60,7,6]
# Output    - A list with two integers a and b that add up to k     [21,60]
##################################################


def find_sum(lst, k):
    # Bubble sort the list
    z = len(lst) - 1
    while(z > 0):
        for i in range(len(lst)):
            if((i > 0) and (lst[i] < lst[i-1])):
                temp = lst[i-1]
                lst[i-1] = lst[i]
                lst[i] = temp
        z -= 1

    # Find sums by comparing first and last indexes
    indA = 0
    indZ = len(lst) - 1
    while(indA < indZ):
        if(lst[indA] + lst[indZ] == k):
            return [lst[indA], lst[indZ]]
        elif(lst[indA] + lst[indZ] < k):
            indA += 1
        else:
            indZ -= 1

    return []


##################################################
# CHALLENGE 4
# Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.
# Input     - A list of numbers (could be floating points or integers)                                                        [1,2,3,4]
# Output    - A list such that each index has a product of all the numbers in the list except the number stored at that index [24,12,8,6]
##################################################


def find_product(lst):
    retLst = []
    prod = 1

    # Idea here is to multiple all numbers going forward and store in a new list.
    # Then multiple new list by lst in a reverse order.
    # First prod is set to 1 to offset the list index not being multiplied by itself.

    # Loop beg to end of lst, keeping track of all products before the index
    # Store in new list
    for i in range(len(lst)):
        retLst.append(prod)
        prod *= lst[i]

    prod = 1
    # Loop end to beg of lst, multiplying new list by lst in reverse order
    # Update new list
    for i in range(len(lst) - 1, -1, -1):  # range(start, stop, inc)
        retLst[i] *= prod
        prod *= lst[i]

    return retLst


##################################################
# CHALLENGE 5
# Implement a function findMinimum(lst) which finds the smallest number in the given list.
# Input     - A list of integers                [9,2,3,6]
# Output    - The smallest number in the list   2
##################################################


def find_minimum(arr):

    # No values in arr
    if len(arr) <= 0:
        return None
    # One of more values in arr
    else:
        # Assign the first num as min, loop through the rest and compare with min value
        min = arr[0]
        for num in arr:
            if(num < min):
                min = num

    return min


##################################################
# CHALLENGE 7
# Implement a function find_second_maximum(lst) which returns the second largest element in the list.
# Input     - A List                                [9,2,3,6]
# Output    - Second largest element in the list    6
##################################################


def find_second_maximum(lst):
    # No values in lst.
    if(len(lst) <= 0):
        return None
    # Only one value in lst.
    elif(len(lst) == 1):
        return lst[0]
    # More than one value in lst.
    else:
        max1 = lst[0]
        max2 = lst[0]
        for num in lst:
            # Make sure max1 and max2 are not the same.
            if(max1 == max2):
                max2 = num
            # Check if new value is greather than max1, if so assign max1 to max2 and max1 to new high num.
            if(num > max1):
                max2 = max1
                max1 = num
            # Num is less than max1, check if it's at least higher than max2. If so assign new value.
            elif(num > max2):
                max2 = num

        return max2


##################################################
# CHALLENGE 8
# Implement a function right_rotate(lst, k) which will rotate the given list by k. This means that the right-most elements will appear at the left-most position in the list and so on. You only have to rotate the list by one element at a time.
# Input     - A list and a positive number by which to rotate that list     [10,20,30,40,50],3
# Output    - The given list rotated by k elements                          [30,40,50,10,20]
##################################################


def right_rotate(lst, k):
    # List has no values
    if(len(lst) <= 0):
        return []
    # List only has one value, return that value
    elif(len(lst) == 1):
        return [lst[0]]
    # List has more than 1 value
    else:
        retVal = []
        complete = False

        if(k <= len(lst)):
            start = len(lst) - k
        else:
            start = len(lst) - (k % len(lst))

        inc = start

        while(complete == False):
            retVal.append(lst[inc])

            if(inc + 1 > len(lst) - 1):
                inc = 0
            else:
                inc += 1

            if(inc == start):
                complete = True

        return retVal
