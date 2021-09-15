user = {
  'name': 'Alex',
  'sex': 'helicopter',
  'salary': 60,
  'isFriend': True
}

# ----- Access ------
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

# ----- Add | Delete ------
user['job'] = 'postman' # {... , 'job' : 'postman'}
user.update({'job': 'freelancer' }) # {... , 'job' : 'freelancer'}
print(user)

user.pop('job')
print('after pop', user)

user.popitem()
print('after popitems', user)

del user['sex']
print('after del sex', user)

user.clear()
print('after clear', user)

#del user
# Error: name 'user' is not defined



# ----- Loop ------
user.update({
  'name': 'Alex',
  'sex': 'helicopter',
  'salary': 60,
  'isFriend': True,
})

for x in user:
  print(x)
# name
# sex
# salary
# isFriend
print('--------')

for x in user:
  print(user[x])
# Alex
# helicopter
# 60
# True
print('--------')

for x in user.keys():
  print(x)
print('--------')

for x in user.values():
  print(x)
print('--------')

for x,y in user.items():
  print(x, ' - ', y)
# name  -  Alex
# sex  -  helicopter
# salary  -  60
# isFriend  -  True
print('--------')

# ----- Copy ------
userCoppy = user.copy()
userCopy2 = dict(user)
