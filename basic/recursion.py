# fibonacci number
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return (fib(n-1) + fib(n-2))

# print([fib(i) for i in range(20)])


# def fact(n):
#     if n == 1:
#         return n
#     else:
#         return n * fact(n-1)

# print(fact(5))
# fact(5) = 5*fact(4)
# fact(4) = 4*fact(3) 
# fact(3) = 3*fact(2) 2*3 = 6
# fact(2) = 2*fact(1) 2*1=2
# fact(1) = 1


# S ="abcdef" 
# rev_S = "fedcba"

def rev_s(s):
    if len(s) == 0:
        return s
    else:
        return rev_s(s[1:]) + s[0]  #

# rev_s("abcdef") = rev_s("bcdef") + "a"
# rev_s("bcdef") = rev_s("cdef") + "b"
# rev_s("cdef") = rev_s("def") + "c"
# rev_s("def") = rev_s("ef") + "d"
# rev_s("ef") = rev_s("f") + "e"
# rev_s("f") = f


# Write a recursive function that, given a number  n, returns the sum of the digits of the number n.
# n = 1234 --> 10

# n = 1234 -> 4,3,2,1
# n = 34255 -> 5,5,2,4,3
# def print_digits(n):
#     for i in range
#     temp = n % 10
#     print (temp)


# def sum_of_digits(n):
#     return 

# # sum_of_digits(n) = 

# # print(rev_s("abcdef"), 6)

# um_of_digits(n):
#     return 

# sum_of_digits(n) = 

# print(rev_s("abcdef"), 6)


# # num1 = 603
# num2 = 5734
# # print(num1 // 7)
# # print(num1 % 7)
# # print(num2 % 10)
# # print(num2 // 10)

def digit_iterration(num2):
    dig = []
    sum1 = 0
    while num2 != 0:
        temp = num2 % 10
        num2 = num2 // 10
        # print(num2,temp)
        dig.append(temp)
        sum1 = sum1 + temp
#     print("Digits are: ",dig)
#     print("Sum of the digits are: ",sum1)

# digit_iterration(num2)


## Write a recursive function that, given a number n, returns the sum of the digits of the
## number n.

def digit_recursion(num2):
    if num2 == 0:
        return 0
    else:
        return (num2%10 + digit_recursion(num2 // 10) )
num2 = 5734
# print(digit_recursion(num2))

# 5734 % 10 = 4 + 5734 // 10 = 573    19
# 573 % 10 = 3 + 573 // 10 = 57       15
# 57 % 10 = 7 + 57 // 10 = 5          12
# 5 % 10 = 5 + 5 // 10 = 0            5


## Write a recursive implementation of the factorial function. Recall that n! = 1 × 2 × ... × n,
## with the special case that 0! = 1.

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

n = 5
# print ("Factorial of",n, "is:",factorial(n))


# Write a recursive function that, given a string s, prints the characters of s in reverse order.

def reverse_string(s1):
    if len(s1) == 1:
        return s1
    else:
        return  reverse_string(s1[1:]) + s1[0]
s1 = "Shayani"
# print("Reverse of",s1, "is:",reverse_string(s1))


## Write a recursive function that checks whether a string is a palindrome (a palindrome is
## a string that's the same when reads forwards and backwards.)
def palindrome(s2):
    if len(s2) < 1:
        return True
    else:
        if s2[0] == s2[-1]:
            return palindrome(s2[1:-1])
        else :
            return False

# palindrome(s) = palindrome(s[1:-1]) if s[0] == s[-1]
#               = False
# len(s) == 0 -> True
              


# f(n) = f(n-1) if ...
#      = f(n-2)*f(n-1) else
# palindrome(s)  
# palindrome(s2[0]) = palindrome(s2[0]) if palindrome(s2[0]) == palindrome(s2[-1])
# palindrome("abca") = "a" or "b" -> True
        

# s2 = "mom"  #"baba"
# if(palindrome(s2)==True):
#     print(s2,"is a palindrome!")
# else:
#     print(s2,"isn't a palindrome!")


## Write a recursive function that, given a pointer to the root of a binary search tree, prints
## out the elements in that tree in sorted order.

class Binary:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key
def insert(root, node):
    if root == None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)   
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r = Binary(50) 
insert(r,Binary(30)) 
insert(r,Binary(20)) 
insert(r,Binary(40)) 
insert(r,Binary(70)) 
insert(r,Binary(60)) 
insert(r,Binary(80)) 
# print(inorder(r))



# Write a recursive function that, given two strings, returns whether the first string is a
# subsequence of the second. For example, given hac and cathartic, you should return true,
# but given bat and table, you should return false.

# s1 = "ac|defh" s2="c|ef" 
# "ef" -> "def" => True   => Known
# s1 = "ac" s2="c" 
# 
# sub(s1,s2) = sub(s1[1:],s2) if s1[0] != s2[0]
#            = sub(s1[1:],s2[1:]) else
# sub(s1,s2) = True if s2 == ""
#            = False if s1 == "" and s2 != ""
# 
# sub("acdef","cef") = sub("cdef","cef") if 'a' == 'c'
# sub("cdef","cef") = sub("def","ef")
#sub("def","ef") = sub("ef", "ef")
# sub("ef", "ef") = sub("f","f")
#sub("f","f") = sub("","")
# sub("","") = True because s2 is ""
# 

def subsequence(s1, s2):
    # terminating condition
    if s2 == "":
        return True    
    if s1 == "":
        return False
    # recurr.. logic
    if s2[0] == s1[0]:
        return subsequence(s1[1:], s2)
    return subsequence(s1[1:], s2[1:])
# s1 = 
# subsequence(s1, s2)

# [1,2,3] = [[],[1],[2],[3],[1,2],[2,3],[1,3],[1,2,3]]



# all subsets of a set
# [1,2,3,4,5] 
# 0 = []
# 1 = [1],[2],..
# 2 = [1,2]
# .
# .
# 5 = [1,2,3,4,5]

# generate all subsets of size 2 of a given set

# n = 2
# [[1,2],[1,3][1,4],[1,5],[2,3],[2,4][2,5],[3,4],[3,5],[4,5]] 
# list(range(2,5)) => [2,3,4]
def generate_subset_size_2(s):
    res = []
    for i in range(0,len(s)): # 1
        for j in range(i+1,len(s1)):
            # [1,2]
            res.append([s[i],s[j]])
            
    return res
    
# [1,2,3,4,5]
# s = [2,3,4,5] n=2  [[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
# n=3 => [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
def generate_subset_size_3(s, n):
    res = []
    for i in range(0,len(s)-2): 
        
        res1 = generate_subset_size_2(s[i+1:]) #[2,3]
    return res 

# l = [[2,3],[5,6],[4,5,6,7,8]] 
# # res = [[1,2,3],[1,5,6],[1,4,5,6,7,8]]
# def append_1(l):
#     res = []
#     return res

# # l = [3,4,5]
# # res = [1,3,4,5]
# def append_1_easy(l):
#     res = []
#     res.append(1)
    
#     res[] =1
#     return res 


# s = [1,2,3] = [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
# s1 = [2,3] = [[],[2],[3],[2,3]]   = [[],[2],[3],[2,3],[1],[1,2],[1,3],[1,2,3]]
# s2 = [3] = [[],[3]] = [[],[3],[2],[2,3]]

# def generate_subsets(s):
#     res = []
#     res = generate_subsets(s[0])
#     return res 

# #  n = 2
# # # [[1,2],[1,3][1,4],[1,5],[2,3],[2,4][2,5],[3,4],[3,5],[4,5]] 
# # # list(range(2,5)) => [2,3,4]
# def generate_subset_size_2(s):
#     res = []
#     for i in range(0,len(s)): # 1
#         for j in range(i+1,len(s)):
#             res.append([s[i],s[j]])
            
#     return res
    
# s = [1,2,3,4,5]
# print(generate_subset_size_2(s))

# s = [2,3,4,5] n=2  [[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
# n=3 => [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
# def generate_subset_size_3(s):
#     res = []
#     res1 = generate_subset_size_2(s)
#     for i in range(0,len(s)-2):        
#         res = generate_subset_size_2(s[i+1:]) #[2,3]
#         for j in range(len(res)):
#             res1.append([i+1] + res[j])
#     # print (res1)
#     # res1.append(generate_subset_size_2(s))
#     return res1 
# s = [1,2,3,4,5]
# print (generate_subset_size_3(s))

# l = [[2,3],[5,6],[4,5,6,7,8]] 
# # res = [[1,2,3],[1,5,6],[1,4,5,6,7,8]]
# def append_1(l):
#     res = []
    
#     for i in range(len(l)):
        
#         res.append([1] + l[i])
#     return res 

# print(append_1(l))


# l = [3,4,5]
# # # res = [1,3,4,5]
# def append_1_easy(l):
#     res = []
#     res.append(1)
#     res = res + l
#     return res 

# print(append_1_easy(l))

def generate_subsets(s):
    # res = []
    if s == []:
        return [[]]
    else:
        a = generate_subsets(s[1:])  # [[],[2],[3],[4],[2,3],[2,4],[3,4],[2,3,4]]
        res = a[:]  # deepcopy
        # res = a
        # a=[1,2,3] => res [1,2,3]
        # a[2] = 5 , a = [1,2,5]
        # res=[1,2,3]
        # a = 5
        # res = a
        # a = 4
        # res 
        for b in a: 
            res.append([s[0]] + b)
        res = list(sorted(res))
        print(f'{s} => {res}')
        return res # [[],[2],[3],[4],[2,3],[2,4],[3,4],[2,3,4]] + [[1],[1,2],[1,2,3],....]   
        # res = a + [[1],[1,2],[1,2,3],...]
         # return (a + [[s[0]] + b for b in a])

    # return res

s = [1, 2, 3, 4]   #[[]], [1], [] 
# [1,2,3,4] => [1] , generate_subsets([2,3,4])
# a = generate_subsets([2,3,4])
# a = [[]],[2],[3],[4],[2,3],[2,4],[3,4],[2,3,4]]
# for b in a:
#   print(b)
# [1] + [b for b in [[]],[2],[3],[4],[2,3],[2,4],[3,4],[2,3,4]]]
# print(list(sorted(generate_subsets(s))))



# 1. reverse a list using recursion
def reverse_list(l):
    if len(l) == 0:
        return []
    else:
        return (reverse_list(l[1:]) + [l[0]])

l = [1,2,3,4]
print (reverse_list(l))


# is palindrome
# 101 -> True, 102 -> False, 1 -> True
# def isPalNum(num):
#     if len(num) < 1:
#         return True
#     else:
#         if num[0] == num[-1]:
#             return isPalNum(num[1:-1])
#         else:
#             return False
# num= "jkhgad" #"madam"

# if(isPalNum(num)==True):
#     print("Palindrome!")
# else:
#     print("Not Palindrome!")
#     return 


# print(isPalNum(101))

# 2. reverse a linked list using recursion

# 3. is palindrome
# 101 -> True, 102 -> False, 1 -> True
def isPalNum(num, res):
    if num == 0:
        return res
    res = (res*10) + (num%10)
    return isPalNum((num//10), res)
num = 102
res = 0
p = isPalNum(num, res)
if (num == p):
    print("Palindrome")
else:
    print("Not Palindrome")
# print(isPalNum(102))

# [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# for key,val in dic.items():
# {'harry':10,'Tom':30}
# vals = dic.values()
# vals = sorted(list(set(vals)))
# vals = [10,20]
# second_max = vals[-2]
# for key,val in dic.items():
#   if val == second_max:
#       result.append(key)
# return list(sorted(result))[0]


# pow(n) == 2**n
# 2**4 = (2**2)**2  = pow_2((pow_2(2)))
# 2**8 = (2**4)**2
# 2**5 = (2**4) * 2
# 2**0 = 1


# O(n) calls
# O(logn) calls
# def pow_2(n):
#     m = n/2
#     if n == 0:
#         return 1
#     else:
#         return pow_2((2*pow_2(n//2))
#         return pow_2(m)*pow_2(2)


# pow2(n) = ? when n is odd     n = 5      ((2**n//5)**2)*2
#         = ? when n is even    n = 8       (2**n/2)**2
#         = ? when n is a special value ?    n = 0 , 1


# pow2(5) = ((2**2)**2)*2 = (pow2(2)**2)*2 = 32 
#pow2(2) = ((pow2(2/2)**2) = 4
#pow2 (1) = ((pow2(0)**2)*2) = 2
#pow2(0) = 1

# print(pow_2(10)) 
# print(pow_2(124)) 

# 2**4 = (2**2)**2  = pow_2((pow_2(2)))
# n= 8, (2 ** 4)**2,   n/2 
