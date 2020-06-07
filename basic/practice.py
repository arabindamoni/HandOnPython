# # list

# l = list(range(0,10,2))

# # l = [0,2,4,6,8]
# # l = [0,2,4,66,8]

# l[3] = 66

# # l = [0,1,2,3,4,5] -> [5,4,3,2,1,0]
# l[::-1]

# # 
# l1 = [1,2,3,4,5]
# l2 = [5,6,7,3,4]
# l3 = [1,2,3,4,5,6,7] # union
# l4 = [3,4,5] # intersection

# def union_list(l1, l2):
#     l3 = []
#     l = l1+l2
    
#     return l3

# def intersect_list(l1,l2):
#     l3 = []
#     return l3


# print(union_list(l1,l2))


# l1 = [1,2,3,4,5]  # n
# l2 = [5,6,7,3,4]  # m
# # l3 = [1,2,3,4,5,6,7] # union
# # l4 = [3,4,5] # intersection

# def union_list(l1, l2):
#     l3 = []
#     l = l1+l2
#     for i in l:
#         if i not in l3:
#             l3.append(i)
#     return l3

# def intersect_list(l1,l2):
#     l4 = []
#     l = l1+l2
#     l.sort()
#     # length = len(l)
#     for i in range(len(l) - 1):
#         if l[i] == l[i+1]:
#             l4.append(i)
#     # print(l4)                
#     return l4
# print(union_list(l1,l2))
# # intersect_list(l1,l2)
# print(intersect_list(l1,l2))


# ## Question 6: Given a number count the total number of digits in a number
# 7893 -> 
# count  | out
# 1      | 789  11
# 2      | 78   1
# 3      | 7    
# 4      | 0

# num3 = 1
# num3 = int(input("Enter the number: "))
# count = 1
# while num3 != 0:
#     if num3 < 10:
#         break
#     else:
#         num3 = num3 / 10
#         count += 1
            
# print(count)


# l = [5,6,7,8,-1]
# len(l)

# return length of l
# last element is -1
# [3,4,5,3,2,-1] --> 5
# # [-1] -> 0
 

# print list
# [1,2,3,-1,4,5,1] -> 3
def print_it(l):
    count = 0
    i = 0
    while l[i] != -1:
        count += 1
    print(count)      


# LOOP while
# integer division, mod, variable assignment      
        
