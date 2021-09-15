dictionary = {
  "cat": 'кошка',
  'house': 'дом',
  'word': 'слово',
  'score': 'счет',
  'apple': 'яблоко'
}

while(True):
  userInput = input('Dicitionary: ').split(' ')
  command = userInput[0]
  if (command == 'close' ):
    print('See you later!')
    break
  elif (command == 'translate'):
    # Seacrh by key
    if (userInput[1] in dictionary):
      print(dictionary[userInput[1]])
    # Search by value
    elif (userInput[1] in dictionary.values()):
      for key,value in dictionary.items():
        if (value == userInput[1]):
          print(key)
    else:
      print('Sorry, there is no that word')
  elif (command == 'add'):
    if (len(userInput) != 3):
      print('Wrong arguments number')
      continue
    dictionary.update({userInput[1]: userInput[2]})
  else:
    print('There is no that command')