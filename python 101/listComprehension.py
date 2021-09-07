arr = [1, -1, 2, 3, -2]
arr2 = [x + 2 for x in arr] # [3, 1, 4, 5, 0]

arr3 = [x + 2 for x in arr if x > 0] # [3, 4, 5]

arr4 = ['buzz' if x == 2 else x for x in arr if x > 0]
# [1, 'buzz', 3]
# it like say -
# if x == 2 then return "buzz"
# else return x
# for each value in arr that more than 0 
 
arr5 = [i for i in range(10)] 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
