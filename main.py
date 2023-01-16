

# 1. Write a function to create a 2-D List/Array with random integers between 0 to 100.
# This function should take two arguments - numberOfRows and numberOfColumns and return 2D list.
# 2. Write a function to sort the 2-D list based on column index keeping the rows intact.
# This function should take two arguments - 2D list created above and column Index and return sorted 2D list.

import random


def create2darray(r,c):
    rows, cols = (r, c)
    arr = [[1 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = random.randint(0,100)
    return arr


def sort2darray(arr, c):
    return [x for x in sorted(arr, key=lambda x: x[c])]

arr = create2darray(5,5)
print(arr)
arr2 = sort2darray(arr, 2)
print(arr2)


# def sort_2d_list(lst, columnIndex):
    # return [x for x in sorted(lst, key=lambda x: x[columnIndex])]
# import random
# r = int(input())
# c = int(input())
# l = [[0 for i in range(c)] for j in range(r)]
# for i in range(r):
#     for j in range(c):
#         l[i][j]=random.randint(0, 100)
# print(l)
