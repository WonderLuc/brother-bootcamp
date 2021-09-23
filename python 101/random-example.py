import random

random.random()
# 0.7395475772544029
random.randint(1, 10)
# 4
random.choice(['Alex', 'Bonny', 'Frank', 'Carlos'])
# Carlos
numbers = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(numbers)
print(numbers)
# [2, 9, 5, 10, 3, 7, 1, 4, 8, 6]
random.sample(['Alex', 'Bonny', 'Frank', 'Carlos'], 2)
# ['Bonny', 'Alex']

