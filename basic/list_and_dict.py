# def make_dict(keys, values):
#     d = {}
#     for i in range(len(keys)):
#        # print(i)
#        key = keys[i]
#        val = values[i]
#        d[key] = val

#     # d.pop('Ten')
#     # d.pop()
#     return d


# keys = ['Ten', 'Twenty', 'Thirty', 'Fourty']
# values = [10, 20, 30, 40]
# print(make_dict(keys,values))


def merge_dict(d1, d2):
    d = {}
    # d1 -> d
    keys = list(d1.keys())
    values = list(d1.values())
    for i in range(len(keys)):
       key = keys[i]
       val = values[i]
       d[key] = val
    
    # d2 -> d
    keys = list(d2.keys())
    values = list(d2.values())
    for i in range(len(keys)):
       key = keys[i]
       val = values[i]
       d[key] = val    
    return d


# def copy_dict(d1):    
#     keys = d1.keys()
#     values = d1.values()      
#     return make_dict(keys, values)

# output: print(d1.keys()) : ten , twenty, thirty

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50, "sixty":60}
print(merge_dict(dict1, dict2))
# print(copy_dict(dict1))