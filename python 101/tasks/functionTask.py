# Avarage Task
def avarage(*args):
  sum = 0
  for x in args:
    sum += x
  return int( sum / len(args))

print(avarage(10, 15, 72))

# Decorator Task
def argsDecorator(func):
  def f(*args, **kwargs):
    print('Args - ', args)
    print('Kwargs - ', kwargs)
    result = func(*args, **kwargs)
    print('Return - ', result)
    return result
  return f

@argsDecorator
def min(x, y):
  if (x < y): return x
  return y

min(2, 5)

