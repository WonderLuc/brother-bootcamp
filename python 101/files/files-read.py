f = open('hello.txt', 'r')
print(f.read())
# Hello File!
# How are you?
f.close()

f = open('hello.txt', 'r')
print(f.readline())
# Hello File!
print(f.readline())
# How are you?
f.close()

f = open('hello.txt', 'r')
print(f.readlines())
# ['Hello File!\n', 'How are you?']
f.close()

# With arguments 
f = open('hello.txt', 'r')
print(f.read(1)) # H
print(f.read(3)) # ell
print(f.read())
# o File!
# How are you?
f.close()

f = open('hello.txt', 'r')
print(f.readline(4)) # Hell
print(f.readline()) # o File!
print(f.readline()) # How are you?
f.close()

f = open('hello.txt', 'r')
print(f.readlines(1))
# ['Hello File!\n']
f.close()

# Loop
f = open('hello.txt', 'r')
for x in f:
  print(x)
f.close()

# Prefer format
try:
  with open('hello.txt', 'r') as h:
    print(h.read())
    h.close()
except FileExistsError:
  print('File dosen\'t exists!')
