hero = {
  'health' : 100,
  'damage' : 10
}

army = []

id = 0

# Basic functions 
def createSkeleton(name, health=20, damage=10):
  global id
  id = id + 1
  return {
    'name' : name,
    'health' : health,
    'damage': damage,
    'id': id
  }

def add(skeleton):
  global army
  army.append(skeleton)

def find(id):
  for unit in army:
    if (unit['id'] == id): return unit
  return 0

def delete(id):
  global army

  for i in range(len(army)):
    if (army[i]['id'] == id):
      army.pop(i)
      return 1
  return 0

def sendToHero(skeleton):
  round = 1
  while (skeleton['health'] > 0 and hero['health'] > 0):
    print('Round ', round)
    skeleton['health'] -= hero['damage']
    hero['health'] -= skeleton['damage']
    status = f"hero health - {hero['health']}\nSkeleton health - {skeleton['health']}"
    print(status)
    print('\n')
    round += 1

  print('Result:')
  if(hero['health'] <= 0):
    print('Hero defeated')
    return 1
  if(skeleton['health'] <= 0):
    print(skeleton['name'], ' defeated')
    delete(skeleton['id'])

# Additional functions
def addToArmy(data):
  if (len(data) == 3):
      (name, health, damage) = tuple(data)
      add(createSkeleton(name, int(health), int(damage)))
  elif (len(data) == 1):
      add(createSkeleton(data[0]))
  print('Unit added')

def printSkeleton(skeleton):
  print('skeletonID - ', skeleton['id'])
  print('Name - ', skeleton['name'])
  print('Health - ', skeleton['health'])
  print('Damage - ', skeleton['damage'])

def printArmy():
  for unit in army:
    print('\n')
    printSkeleton(unit)
    print('\n---------------')

# User Iteraction
commands = {
  'add': '(name) [health] [damage] Adds new skeleton to army. health and damage optional parameters',
  'find': '(id) Return a unit from army',
  'delete': '(id) Delete a unit from army',
  'showArmy': 'Show all units',
  'attackHero': '(id) Send skeleton to defeat the hero',
  'out': 'Programm exit',
  'help': 'Prints all command'
}

def printUsage():
  for command, desc in commands.items():
    print(command, ' : ', desc)
  print('\n')

def getInput():
  return input('Wait for command: ')

def isAvalible(command):
    return (command in commands and len(army) ) or command in ['out', 'add', 'help'] 

# Program Loop
print('Hello my Lord!\nThere are commands for your army:\n')
printUsage()
while(True):
  data = getInput().split(' ')
  command = data[0]
  data = data[1:]
  if (not isAvalible(command)):
    print('Error: Wrong Command or Army empty')
    continue
  
  if (command == 'add'):
    addToArmy(data)
  elif (command == 'find'):
    printSkeleton(find(int(data[0])))
  elif (command == 'showArmy'):
    printArmy()
  elif (command == 'attackHero'):
    if (sendToHero(find(int(data[0])))): break
  elif (command == 'delete'):
    delete(int(data[0]))
  elif (command == 'help'):
    printUsage()
  elif (command == 'out'):
    break
  else:
    print('Unknown command')
