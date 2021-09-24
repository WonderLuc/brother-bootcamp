try:
  with open('hello.txt', 'a') as f:
    f.write('\nI\'m fine')
    f.close()

  print(open('hello.txt', 'r').read())
  # Hello File!
  # How are you?
  # I'm fine

  with open('404.txt', 'w') as f:
    f.write('New File')
    f.close()

  print(open('404.txt', 'r').read())
  # New File
except:
  print('Smthg wrong')