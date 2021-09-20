thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print("banana" in thisset)

anotherSet = {'a', 'b', 'c'}

anotherSet.add('d')
print(anotherSet)
# {'b', 'c', 'd', 'a'}

anotherSet.update(['slime', 'fruit'])
print(anotherSet)
# {'a', 'slime', 'c', 'd', 'fruit', 'b'}

anotherSet.remove('slime')
print(anotherSet)
# {'a', 'c', 'd', 'fruit', 'b'}

anotherSet.discard('fruit')
print(anotherSet)
# {'a', 'c', 'd', 'b'}

anotherSet.clear()
print(anotherSet)
# set()

del anotherSet
print(anotherSet)
# NameError: name 'anotherSet' is not defined 

# Union
{1, 2, 3, 4, 5}.union({3, 4, 5, 6}) # {1, 2, 3, 4, 5, 6}

# Difference
{1, 2, 3, 4}.difference({2, 3, 5}) # {1, 4}

# Intersection
{1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}) # {3, 4, 5}

# Superset check
{1, 2}.issuperset({1, 2, 3}) # False

# Subset check
{1, 2}.issubset({1, 2, 3}) # True
