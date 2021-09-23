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

def isAvalible(command, army):
    return (command in commands and len(army) ) or command in ['out', 'add', 'help'] 