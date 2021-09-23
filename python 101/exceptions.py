try:
  raise Exception('Something went wrong')
  # Exception: Something went wrong
except:
  print('something wrong')

try:
  print(x)
  # NameError: x not defined
  raise NameError('no name')
  # NameError: no name
except:
  print('name dosent exsist')

try:
  x = '10'
  if not type(x) is int:
    raise TypeError("Only integers are allowed")
except TypeError:
  print('Only integers are allowed')

# Exception handling
try:
  print('Program adds 3 to number')
  x = float(input('Enter a number greater than 3: '))
  if x < 3:
    raise Exception()
except ValueError:
  print('Only numbers!')
except:
  print('Only greater than 3!')
else:
  print(3 + x)
finally:
  print('Thanks for try!')