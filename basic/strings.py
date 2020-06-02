s = "hello munai"
# print(s)

# print "hel"
# print(s[0:3])
# print(s[3:5])


# forward index
 # h e l l o
 # 0 1 2 3 4

# backward index
 # h e l l o
 # -5 -4 -3 -2 -1

# print(s[0], s[-5])
# print(s[3:5], s[-2:])
# print(s[::-1])

# s = "hello munai"
# print "munai hello"
# m = s[-5:]

# p = s[0:5]
# print(m+" "+p)

# index of first space
# print(s.index(' '))
# i = s.index(' ')
# print(s[-i:] + " "+ s[0:i])
# print(s.index(' ',i+1))

s = "hello munai kemon achis"
# i = s.index(' ')
# index(char/str, start=0, end=-1)
# print(s.index(' ',i+1))
# print(s.split())
# i= s.index(' ')
# j = s.index(' ',i+1)
# k = s.index(' ',j+1)

# print(s[k+1:]+ " "+ s[j+1:k] + " " + s[i+1:j]+" "+ s[0:i])
# res = []
# i = 0
# for k in range(3):
#     j = s.index(" ",i)
#     r = s[i:j]
#     i = j + 1
#     res.append(r)
# res.append(s[i:])

# join
# print(res)
# print(" ".join(res[::-1]))

# split
# s = "hello munai kemon achis"
# # output = "achis kemon munai hello"
# # print(s.split())
# # print("my run")
# def rev(s):
#     p = s.split()
#     #print(p[::-1])
#     return " ".join(p[::-1])

# print(rev("abc def ghi"))

# print(s.upper())

# replace
# s = "hello munai kemon achis"
# s = "hello,munai,kemon,achis"
# print(s.replace(' ',','))


# l = [4,5,2,4,0,22,1]
# l.sort(reverse=True)
# print(l)

# l2 = sorted(l)
# print(l2)

# Tuple
# l = [(0,0),(1,0),(2,50),(8,3),(3,6)]
# # sort based on x/y coordinate
# # print(l[0][1])
# l2 = sorted(l, key = lambda item:item[1])
# print(l2)

# order of sort in tuple
l = [("one",1),("two",2),("one",2)]
#[('one', 1), ('two', 2), ('one', 2)]
#output: [('one', 1),  ('one', 2), ('two', 2)]
l1 = sorted(l, key = lambda item:(item[1], item[0]))
print (l1)