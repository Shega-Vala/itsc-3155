import collections


dict1 = {'a': 200, 'b': 300,'c': 300} #first dictionary set
dict2 = {'a': 200, 'b': 100, 'd':400} #second dictionary set

counter = collections.Counter()
for d in dict1,dict2:
    counter.update(d)

res = dict(counter)

print("New sorted dictionary : ", res)