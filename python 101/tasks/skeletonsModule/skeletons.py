from base import *
from additional import *
from userInteraction import *


hero = {
  'health' : 100,
  'damage' : 10
}

army = []

id = 0

# Program Loop
print('Hello my Lord!\nThere are commands for your army:\n')
printUsage()
while(True):
  data = getInput().split(' ')
  command = data[0]
  data = data[1:]
  if (not isAvalible(command, army)):
    print('Error: Wrong Command or Army empty')
    continue
  
  if (command == 'add'):
    addToArmy(data, army, id)
  elif (command == 'find'):
    printSkeleton(find(int(data[0]), army))
  elif (command == 'showArmy'):
    printArmy(army)
  elif (command == 'attackHero'):
    if (sendToHero(find(int(data[0]), army), hero, army)): break
  elif (command == 'delete'):
    delete(int(data[0]), army)
  elif (command == 'help'):
    printUsage()
  elif (command == 'out'):
    break
  else:
    print('Unknown command')
