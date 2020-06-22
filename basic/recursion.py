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











