user = {
  'name': 'Alex',
  'sex': 'helicopter',
  'salary': 60,
  'isFriend': True
}

print(user['name']) # Alex

print(user.get('salary')) # 60

print(user.keys()) # [name, sex, salary, isFriend]
print(user.values()) # [Alex, helicopter, 60, True]

print(list(user.items()))
# [('name', 'Alex'), 
# ('sex', 'helicopter'), 
# ('salary', 60), 
# ('isFriend', True)]

print('salary' in user) # True
