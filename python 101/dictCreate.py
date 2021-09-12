dog = { 'name' : 'Ruby' }
# {'name': 'Ruby'}

cat = dict([('name', 'Fee'), ('isBusy', True)])
# {'name': 'Fee', 'isBusy': True}

duck = dict.fromkeys(['name', 'flightLenght'])
# {'name': None, 'flightLenght': None}
salary = dict.fromkeys(['officer', 'postman'], 1000)
# {'officer': 1000, 'postman': 1000}

numbers = { x: x*2 for x in range(10) }
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}

print(dog)
print(cat)
print(duck)
print(salary)
print(numbers)