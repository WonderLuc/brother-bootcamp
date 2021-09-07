arr = ['bannana', 'cherry', 'orange', 'kiwi', 'strawberry', 'melon']

print(arr[1]) # cherry
print(arr[1:3]) # ['cherry','orange']
print(arr.index('orange')) # 2

arr[2] = 'watermelon' # change 'orange' to ''watermelon
print(arr)
arr[3:4] =  ['blackcurrant', 'mango'] # change 'kiwi' and add new item 
print(arr)

arr.append('potato') # add item to the end of array
print(arr)
arr.insert(0, 'lemon') # add lemon at 0 index and save all other items
print(arr)

arr.pop() # delete last item of array - 'potato'
print(arr)
arr.pop(0) # delete item on index 0 - 'lemon'
print(arr)
del arr[0] # also delete first - 'bananna'
# del arr # delete a list and variable too!
print(arr)

words = ['table', 'code', 'flower']
arr.extend(words)  # [... 'melon', 'table', 'code', 'flower']
print(arr)

# loop through array
for item in arr:
    print(item)

for i in range(len(arr)):
    print(i)
    print(arr[i])
    print('-------')

i = 0
while (i < len(arr)):
    print(arr[i])
    i += 1

[print(item) for item in arr]


# Copy and Join Lists

arr = [ x for x in range(4)]
arr2 = [ 4, 5, 6]

arr3 = arr.copy()

arr4 =list(arr)

print(arr3)
print(arr4)

arr3 = arr + arr2
# [0, 1, 2, 3, 4, 5, 6]

arr.extend(arr2)

newArr = []

for item in arr:
    newArr.append(item)

print(arr3)
print(arr)
print(newArr)
