def fibonacci(n):
  if (n == 1):
    return 0
  elif (n == 2):
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(7))