# Given n print n rows such that i'th row has i stars ('*'), stars are interspaced by a space (' ')
# Ex: for n = 3 output will be:
# *
# * *
# * * *

# list(range(0,1)) -> 
def print_1(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()
    return

# print_1(1)
# print("\n######\n")
# print_1(3)
# print("\n######\n")
# print_1(10)
# print("\n######\n")

# Given n print n rows such that i'th row has i stars ('*'), stars are interspaced by a space ('$')
# the print structure should be in pyramid form
# Ex: for n = 3 output will be:
# $$*$$
# $*$*$
# 

# n = 2
#   *
#  * *
# * * *
#* * * *
# sp = n - 1

def print_2(n):
    space = n - 1 #2
    for i in range(n): #01j in range(number_of_total_char) -> 2*N - 1
        for j in range(n):#012 01
            # if j < first_star_index or j > last_star_inded: print('$')
            # 
            if j < space: # $$*  $
                print("", end = "$")
            else:
                print("*", end = "$")
        space -= 1
        print()            
    return

# print_2(1)
# print("\n######\n")
# print_2(3)
# print("\n######\n")
# print_2(10)
# print("\n######\n")


# Given n print n rows such that i'th row has i stars ('*'), stars are interspaced by a space (' ')
# print from right to left
# Ex: for n = 3 output will be:
#    *
#  * *
#* * *
# n = 2
#  * 
#* *
# n = 5
#$ $ $ $ *  # i = 0
#$ $ $ * *
#$ $ * * *
#$ * * * *
#* * * * *


def print_3(n):
    for i in range(n):  #0
        count_dol = n - i -1  #2
        for j in range (n):    # 01 2       
            if j < count_dol: 
                print(" ", end = " ")  #$ $ *
            else:
                print("*", end=" ")
        print()
    return
# print_3(1)
# print("\n######\n")
# print_3(3)
# print("\n######\n")
# print_3(10)
# print("\n######\n")


## Question 3: Accept n number from user and calculate the sum of all number between 1 and n including n
# num1 = int(input("Enter the number: "))
# sum_ = 0
# for i in range(num1+1):
#     sum_ = sum_ + i
# print("Sum of the number : ", sum_)


# def print_2(n):
#     for i in range(0, n):              # 0
#         for j in range(n - 1, i, -1):  # 5 4 3
#             print("$", end='')     # $
#         for l in range(i+1):            # 0
#             print('*', end='')
#             if not (i == n-1 and l == i):
#                 print("$", end='')
#         for k in range(i + 1, n-1):      #
#             print("$",end='')     #
#         print()

#                                       # $ $ $ $ * 

# print_2(1)
# print("\n######\n")
# print_2(5)
# print("\n######\n")
# print_2(10)
# print("\n######\n")


# arr1, arr2 --> sorted 
# [1,2,3,4,6,7], [4,5,8,9]
# output: [1,2,3,4,4,5,6,7,8,9]
# [1,2,5,9], [3,4,5,6]
# i=0, j=0, [1]
# i = 1, j = 0, [1,2]
# i = 2, j = 0, [1,2,3]
# i = 2, j = 1, [1,2,3,4]
# i = 2, j = 2, [1,2,3,4,5]
# i = 3, j = 2, [1,2,3,4,5,5]
# i = 3, j = 3, [1,2,3,4,5,5,6]
# i = 3, j = 4, [1,2,3,4,5,5,6,9]
# i = 4, j = 4  return
# [1], [2,3,4]

def merge_sorted_arrays(arr1, arr2):
    arr3 = []
    i = 0
    j = 0
    n = len(arr1)
    m = len(arr2)
    while i < n and j < m:
        if (arr1[i] < arr2[j]):
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    while j < m:        
        arr3.append(arr2[j])
        j += 1
    while i < n:        
        arr3.append(arr1[i])
        i += 1
    
    return  arr3

print(merge_sorted_arrays([1,2,3,4,6,7],[4,5,8,9]))
print(merge_sorted_arrays([1,2,3,4,6,7],[]))
print(merge_sorted_arrays([1,2,3,4,6,7],[1,2,3,4,6,7,10,22]))



def merge_sorted_arrays_2(arr1, arr2, arr3):
    res = []
    return res

print(merge_sorted_arrays_2([1,2,3,4,6,7],[4,5,8,9], [55,66]))
print(merge_sorted_arrays_2([1,2,3,4,6,7],[],[]))
print(merge_sorted_arrays_2([1,2,3,4,6,7],[1,2,3,4,6,7,10,22],[5,6,7,8,9,10]))
