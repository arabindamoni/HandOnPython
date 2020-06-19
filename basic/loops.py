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

# print(merge_sorted_arrays([1,2,3,4,6,7],[4,5,8,9]))
# print(merge_sorted_arrays([1,2,3,4,6,7],[]))
# print(merge_sorted_arrays([1,2,3,4,6,7],[1,2,3,4,6,7,10,22]))



# def merge_sorted_arrays_2(arr1, arr2, arr3):
#     res = []
#     return res

# print(merge_sorted_arrays_2([1,2,3,4,6,7],[4,5,8,9], [55,66]))
# print(merge_sorted_arrays_2([1,2,3,4,6,7],[],[]))
# print(merge_sorted_arrays_2([1,2,3,4,6,7],[1,2,3,4,6,7,10,22],[5,6,7,8,9,10]))


# def merge_sorted_arrays_2(arr1, arr2, arr3):
#     temp = merge_sorted_arrays(arr1, arr2)
#     return merge_sorted_arrays(temp, arr3)
    
    # res = []
    # i = 0
    # j = 0
    # k = 0    
    # m = len(arr1)
    # n = len(arr2)
    # p = len(arr3)

    # while i < m and j < n and k < p:
    #     if arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
    #         res.append(arr1[i])
    #         i += 1
    #     elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]:
    #         res.append(arr2[j])
    #         j += 1
    #     else:
    #         res.append(arr3[k])
    #         k += 1
    # while i < m:        
    #     res.append(arr1[i])
    #     i += 1
    # while j < n:        
    #     res.append(arr2[j])
    #     j += 1 
    # while k < p:        
    #     res.append(arr3[k])
    #     k += 1 


    # temp = []
    # while i < m and j < n:
    #     if (arr1[i] < arr2[j]):
    #         temp.append(arr1[i])
    #         i += 1
    #     else:
    #         temp.append(arr2[j])
    #         j += 1
    # while j < n:        
    #     temp.append(arr2[j])
    #     j += 1
    # while i < m:        
    #     temp.append(arr1[i])
    #     i += 1
    # l = 0
    # s = len(temp)    
    # while l < s and k < p:
    #     if (temp[l] < arr3[k]):
    #         res.append(temp[l])
    #         l += 1
    #     else:
    #         res.append(arr3[k])
    #         k += 1
    # while l < s:        
    #     res.append(temp[l])
    #     l += 1
    # while k < p:        
    #     res.append(arr3[k])
    #     k += 1
    # return res

# print(merge_sorted_arrays_2([1,2,3,4,6,7],[4,5,8,9], [55,66]))
# print(merge_sorted_arrays_2([1,2,3,4,6,7],[],[]))
# print(merge_sorted_arrays_2([1,2,3,4,6,7],[1,2,3,4,6,7,10,22],[5,6,7,8,9,10]))



# arr = [3,4,2,4,5,6,4,5]
# output = {2:1,3:1,4:3,5:2,6:1}
#arr1 = [1,1,1,1]    # arr1[4]
#temp = [1,2,2,2,3]
# k = 5, v=10
# dic[5]= 10
# dic[5] = 15
# {5:15}
# def list_count(arr):
#     res = {}
#     count = 1
#     temp = set(arr)
#     for i in range(len(arr) - 1): #0123

#         if arr[i] == arr[i+1]:
#             count += 1
#             res[arr[i]] = count
#         else:
#             # res[arr[i]] = count  #res = {1,}
#             res[arr[i]] = count
#             count = 1
       
#     return res


# rotate an array k place
# arr= [1,2,3,4,5,6] k = 2 --> arr=[3,4,5,6,1,2]
# arr_rev=[6,5,4,3,2,1]
# def rotate_arr(arr, k):
#     l = len(arr)
#     new_arr = []
#     for i in range(k, l):
#         new_arr.append(arr[i])
#     for j in range(0, k):
#         new_arr.append(arr[j])
#     return new_arr

# arr= [1,2,3,4,5,6] 
# print(rotate_arr(arr, 7)) 


# arr = [3,4,2,4,5,6,4,5]
# def dictionary(arr):
#     res = {}
#     # arr.sort()
#     for i in arr: 
#         res[i] = arr.count(i)
#     return res
    
# print (dictionary(arr))
# print (list_count(arr))

# given arr and a target number T, return True 
# if there exists i,j such that arr[i] + arr[j] == T , i != j
# arr = [3,4,2,5,1],  T = 8 --> True (5+3 == T)
# T = 10 return False
# def two_sum(arr, T):
#     # for i in range(len(arr)):
#     #     for j in range(i+1, len(arr)):
#     #         if arr[i] + arr[j] == T:
#     #             return True           
    
#     # for i in range(len(arr)):
#     #     var = T - arr[i]
#     #     if var in arr:
#     #         return True
   
#     # [3,4,5] , T =7 
#     new_dict = {}
#     for i in range(len(arr)):
#         var = T - arr[i]   # 6 - 3 = 3
#           # {3:1}
#         if var in new_dict:# 3 in new_dict => True
#             return True  # True
#         new_dict[arr[i]] = 1
#     return False


# arr = [3,4,2,5,1]
# T = 8
# print(two_sum(arr, T))


# Given an array return a sum_arr such that i'th element 
# of sum_arr is cumulative prefix sum upto i'th index in arr 
# arr = [1,2,3,4,5] => [1,3,6,10,15]
def prefix_sum(arr):
    res = []
    sum_ = 0
    for i in range(len(arr)):
        sum_ = arr[i] + sum_
        res.append(sum_)
    return res

print(prefix_sum([1,2,3,4,5]))

#Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. 
# If there is no lucky integer return -1.

 

# Example 1:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Example 3:

# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.
# Example 4:

# Input: arr = [5]
# Output: -1
# Example 5:

# Input: arr = [7,7,7,7,7,7,7]
# Output: 7

# https://leetcode.com/
def dictionary(arr):
    res = {}
    arr.sort()
    for i in arr: 
        res[i] = arr.count(i)
    return res
    
# print (dictionary(arr))
def findLucky(arr):
    
    new_arr = []
    
    new_dict = dictionary(arr)
    for key, value in new_dict.items():
        if key == value:
            new_arr.append(key)
    if len(new_arr) < 1:
        print("Lucky number: -1, As there are no lucky numbers in the array.")
    else:
        print("Lucky number: ",new_arr[-1])
            
    return False
arr1 = [2,2,3,4,5,5,5,5,5]
arr2 = [1,2,2,3,3,3]
arr3 = [2,2,2,3,3]
arr4 = [5]
arr5 = [7,7,7,7,7,7,7]
arr6= [1,1,2,4,4,4,4,3,3,3]
print("Try 1:")
findLucky(arr1)
print("Try 2:")
findLucky(arr2)
print("Try 3:")
findLucky(arr3)
print("Try 4:")
findLucky(arr4)
print("Try 5:")
findLucky(arr5)
print("Try 6:")
findLucky(arr6)