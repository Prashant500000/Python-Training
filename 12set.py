set = {2, 4, 6, 8, 10}
print(set)
print(type(set))
print(len(set))

#methods

s = {3, 5, 7, 9}
s.add(4)
s.remove(3)
print(s)

a1 = {1, 2, 3}
a2 = {2, 4, 5}
print(a1.union(a2))
print(a1.intersection(a2))