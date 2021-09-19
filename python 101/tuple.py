names = ('Alex', 'Andrey', 'Jess')

(alex, andrey, jess) = names
print(alex) # Alex

fruits = ('Apple', 'Orange', 'Melon')
(apple, *otherFruits) = fruits
print(apple) # Apple
print(otherFruits) # ['Orange', 'Melon']

mixed = names + fruits
print(mixed)
# ('Alex', 'Andrey', 'Jess', 'Apple', 'Orange', 'Melon')

print(fruits * 2)
# ('Apple', 'Orange', 'Melon', 'Apple', 'Orange', 'Melon')
