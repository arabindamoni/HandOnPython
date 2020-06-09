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
# *$*$*
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

print_2(1)
print("\n######\n")
print_2(3)
print("\n######\n")
print_2(10)
print("\n######\n")


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