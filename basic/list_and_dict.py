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


# def merge_dict(d1, d2):
#     d = {}
#     # d1 -> d
#     keys = list(d1.keys())
#     values = list(d1.values())
#     for i in range(len(keys)):
#        key = keys[i]
#        val = values[i]
#        d[key] = val
    
#     # d2 -> d
#     keys = list(d2.keys())
#     values = list(d2.values())
#     for i in range(len(keys)):
#        key = keys[i]
#        val = values[i]
#        d[key] = val    
#     return d


# def copy_dict(d1):    
#     keys = d1.keys()
#     values = d1.values()      
#     return make_dict(keys, values)

# output: print(d1.keys()) : ten , twenty, thirty

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50, "sixty":60}
# print(merge_dict(dict1, dict2))
# print(copy_dict(dict1))


##Assignment - 3
# sampleDict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# a = sampleDict['class']['student']['marks']['history']
# print(a)




##Assignment - 4


##Assignment - 5
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# d = {"name": sampleDict["name"],"salary": sampleDict["salary"]}


# def newDict(keys, values):
#     val1 = sampleDict["name"]
#     val2 = sampleDict["salary"]
#     values = []
#     values.append(val1)
#     values.append(val2)
#     keys = []
#     keys.append("name")
#     keys.append("salary")
    
#     #keys = ["name", "Salary"]
    
#     # newDict = {}
# # print(keys)
# # print(values)
# print(newDict(keys, values))

# #Assignment - 6
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# del sampleDict["name"]
# del sampleDict["salary"]
# print(sampleDict)



# #Assignment - 7
# sampleDict = {'a': 100, 'b': 200, 'c': 300}

# print(200 in sampleDict.values())



# ##Assignment - 8
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# sampleDict['location'] = sampleDict.pop('city')
# print(sampleDict)


# ##Assignment -9
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

items = list(sampleDict.items())
print(items) # [("Physics", 82), ("Math",65), ('history':75)]
min = items[0][1]  
key = items[0][0]
for key, value in items:       
    if value < min:
        min = value 
        ans = key 
print(ans)


# #Assignment- 10
# sampleDict = {
#      'emp1': {'name': 'Jhon', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}
# }

# sampleDict['emp3']['salary'] = 8500
# print (sampleDict)


