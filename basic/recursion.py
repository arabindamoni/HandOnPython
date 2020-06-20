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
def print_digits(n):
    for i in range
    temp = n % 10
    print (temp)


def sum_of_digits(n):
    return 

# sum_of_digits(n) = 

# print(rev_s("abcdef"), 6)