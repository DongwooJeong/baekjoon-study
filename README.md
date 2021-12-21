# baekjoon-study
#### This repository is for studying problems on [baekjoon](https://www.acmicpc.net/) website.
***
## input, output - 10171, 10172
* how to use line break
    + \n
* how to escape
    + \
* how to use " and '
***
## arithmetics - 1000, 1001, 10998, 1008, 10869, 10430, 2588
* map(a, b): apply a transformation function to each item in an iterable and transform them into a new iterable
* A.split(): split A 
* quotient: a//b
* remainder: a%b
***
## if statement - 1330, 9498, 2753, 14681, 2884
* if/elif/else
* multiple of n: X%n == 0
***
## for statement - 2739,10950, 8393, 15552, 2741, 2742, 11021, 11022, 2438, 2439, 10871
* for i in range(a,b):
    + range(a): from 0 to a-1
    + range(a,b): from a to b-1
    + range(a,b,c): from a to b-1 with the increment of c
* list.append(n): add n to the list
* sys.stdin.readline()
    + import sys
    + similar to input(), but faster
        - don't have prompt message
        - return new-line character like \n
* '+' only concatenates same data type.
    + use str() or int() to change data type
* "%s" %(a)- add a string value(a) into a string
* strings can be multiplied
***
## while statement - 10952, 10951
* while condition: - loop will not end until the condition is false
* how to remove an item from a list
    + list.clear - clear all items from the list
    + list.pop(a) - take out a(index) from the list
        - if a is negative, count the index backward
            * -1 indicates the last item
        - list.pop() - take out the last item in the list
    + list.remove(a) - remove item in the list by value
    + del list[i] - delete the item by index
        - del can remove specific range in the list
* try - except
    + try: - execute the following code if there's no error
    + except: - if error occurs in try:, execute the code after except:
* break - escape the loop
***
## one-dimensional array - 10818, 2562, 2577, 3052, 1546, *8958, 4344
* max(list): find the largest number from the list
* min(list): find the smallest number from the list
* list.index(value): find the index number of the value in the list
* X = [int(k) for k in str(N)]: X is a list of integer k, where k is each letter from N converted into a string
* list(N): make a list where each component of N becomes an item of the list, N should be a string
* list.count(A): return how many As are in the list
* A in L: boolean type showing if A is in L(list)
* set(list): remove the duplicate item in the list
* len(list): return how many items are in the list
* list(map(int, input().split())): can get several inputs in a list
* average(list) = sum(list)/len(list)
* Percentage="{:.n%}".format(number) - format number as a percentage with n decimal places
***
## function - 15596, *4673, *1065
* format of function - def ~: return ~
***
## String - 11654, 11720, 10809, 2675, 1157, 1152, 2908, 5622, 2941, 1316
* ord(): string into ascii code
    + chr(): vice versa 
* [::-1]: arrange the number in reverse order
* string.replace(a,b): replace a in string with b
* string[n:]: string starting from nth index
    + ex) apple[1:] => pple
* string.count(A): count the number of A in the string
***
## Basic Math 1 - 1712, 2292, 1193, 2869, 10250, 2775, 2839, 10757, *1011
* sep='k': replace the separator between the arguments in print() function with the one inside the quotes
* iteration takes a long time to calculate
* from math import factorial: factorial(n) would return the factorial of n
***
## Basic Math 2 - 1978, 2581, 11653, *1929, *4948, *9020, 1085, 3009, 4153, 3053, *1002
* set()
    + efficiently remove duplicate values from a collection like a list
    + perform common math operations like unions and intersections
* 4948: n<i<=n*2 is a boolean type
* 1002: abs(m): absolute value of m
***
## Recursion - 10872, 10870, ***2447, *11729
* recursion: the process of defining something in terms of itself
    + recursion function: function to call itself
***
## Brute force - *2798, *2231, *7568, *1018, 1436
* brute force: the cyberattack equivalent of trying every key on your key ring
***
## Sorting - 2750, 2751, *10809, *2108, 1427, *11650, 11651, 10814, 18870
* sorted(): returns a sorted list of the specified iterable object
    + specify ascending or descending order
        - sorted(iterable) or sorted(iterable,reverse=True)
* strings are sorted alphabetically, and numbers are sorted numerically
* difference btwn 2750 and 2751: size of N
    + takes more time to sort: use sys.stdin.readline and sys.stdout.write
        - include new-line character
        - save the input value in the buffer at once
        - directly declare the variable type
* Sorting algorithms
    + O(n^2)
        - Insertion sort: compare kth element with 1st to k-1th element and insert by its size
        - Bubble sort: compare each element, starting with the first element and the second element, to the n-1 element and the nth element, until the array is aligned
    + O(nlogn)
        - Merge sort: binary divide the array up to each element and merge by comparing the size of the element
        - Heapsort: make the array into a heap tree, arrange it in reverse order from the maximum value of the root
    + Others
        - Counting sort (O(n+k)): Save the frequency within the array of specific data at a location corresponding to the value of the data, create an accumulated array, and using the values of the accumulated array as an index, arrange the values of the existing array in order in a new array
* Stats
    + mean
    ```python
        print(sum(anylist)/len(anylist))
    ```
    + median
    ```python
        print(list[len(anylist)//2])
    ```
    + mode
        ```python
        max(set(anylist), key = anylist.count)
        ```

        - use Counter module to create a dictionary indicating the frequency of each element in the list
        ```python
            from collections import Counter
            print(Counter(anylist).most_common()[0][0]) 
        ```
    + range
    ```python
        print(max(list) - min(list))
    ```
* how to print without line break: end=''
    ```python
    print("a", end='')
    print("b")
    ```
* how to sort dictionary
    + sort(key=lambda x: (x[0])): sort the list by x[0]
        - sort(key=lambda x: (x[0], x[1])): sort the list by x[0], and by x[1]
    ```python
        anylist.sort(key=lambda x: (x[0], x[1]))
    ```
    + sort(key=len) or sort(key=lambda x: len(x)): sort by length
***
## Backtracking - *15649, *15650, 15651, 15652, ***9663, ***2580, ***14888, ***14889
* backtracking: a method of attempting all combinations to solve problems with limited conditions, which is a method of examining trees with depth-first search and returning to the previous branch if there is no answer, mainly using recursion
* 'separator'.join(list): combining all the elements(should be str type) in the list with the separator
    ```python
        anylist = ['a', 'b', 'c']
        print(' '.join(anylist))
    ```
    + result
    ```
        a b c
    ```
***
## Dynamic programming - *1003, ***9184, *1904, 9461, *1149, 1932, *2579, *1463, *10844, *2156, *11053, *11054, *2565
* dynamic programming: a way to divide the given problem into several subproblems, to reduce the number of calculation and simplify the process
