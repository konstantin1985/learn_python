print "-"*20 + "Create dictionaries" + "-"*20

a = [[1,2], [3,4], [5,6], [7,8]]
a_dict1 = {k: v for (k, v) in a}
print a_dict1 #{1: 2, 3: 4, 5: 6, 7: 8}
a_dict2 = dict((k, v) for (k, v) in a)
print a_dict2
a_dict3 = dict(a = 2, b = 4, c = 6, d = 8)
print a_dict3
