# ZTM-DS-And-Algo

## **Big-O Cheat Sheet**

| O Notation | Description    |
| ---------- | -------------- |
| O(n)       | Linear         |
| O(1)       | Constant Time  |
| O(n^2)     | Quadratic Time |

https://bigocheatsheet.com/

### **Big Os**

-   O(1) Constant - no loops
-   O(log N) Logarithmic - usually searching algorithms have log n if they are sorted (Binary Search)
-   O(n) Linear - for loops, while loops through n items
-   O(n log(n)) Log Liniear - usually sorting operations
-   O(n^2) Quadratic - every element in a collection needs to be compared to ever other element. Two
    nested loops
-   O(2^n) Exponential - recursive algorithms that solves a problem of size N
-   O(n!) Factorial - you are adding a loop for every element (most likely won't see anywhere)

_Iterating through half a collection is still O(n)_

_Two separate collections: O(a \* b)_

### **What can cause time in a function?**

-   Operations (+, -, \*, /)
-   Comparisons (<, >, ==)
-   Looping (for, while)
-   Outside Function call (function())

### **Rule BookRule 1: Always worst Case**

-   Rule 2: Remove Constants
-   Rule 3: Different inputs should have different variables. O(a+b). A and B arrays nested would be O(a\*b)

    -   \+ for steps in order

    -   \- for nested steps
        Rule 4: Drop Non-dominant terms

### What causes Space complexity?-

-   Variables
-   Data Structures
-   Function Call
-   Allocations

## **O(n) - Single loop**

```
def calc(input):
    a = 10 #O(1)
    a = 50 + 3 #O(1)

    for i in range(len(input)): #O(n)
        anotherFunc() #O(n)
        stranger = True #O(n)
        a+=1 #O(n)

    return a #O(1)
```

BigO = 1 + 1 + n + n + n + n + 1 = (3 + 4n)

Simplified: **O(n)**

## **O(n) - Two loops same input**

```
def func(input):
    for i in range(input): #O(n)
        x = i + 1 #O(n)
        y = i + 2 #O(n)
        z = i + 3 #O(n)

    for j in range(input): #O(n)
        p = j * 2 #O(n)
        q = j * 2 #O(n)
```

Simplified: **O(n)**

## **O(n) - Two loops different input**

```
def func(input1, input 2):
    for i in range(input1): #O(a)
        x = i + 1 #O(n)
        y = i + 2 #O(n)
        z = i + 3 #O(n)

    for j in range(input2): #O(b)
        p = j * 2 #O(n)
        q = j * 2 #O(n)
```

Simplified: **O(a + b)**

## **O(n^2) - Nested loops same input**

```
def func(arr):
    for i in arr:
        for j in arr:
            print(i + j)
```

Simplified: **O(n^2)**

## **O(n^2) - Nested loops different input**

```
def func(arr1, arr2):
    for i in arr1:
        for j in arr2:
            print(i + j)
```

Simplified: **O(a \* b)**
