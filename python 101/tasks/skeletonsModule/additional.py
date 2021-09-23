from base import add, createSkeleton
# Additional functions
def addToArmy(data, army, id):
  if (len(data) == 3):
      (name, health, damage) = tuple(data)
      add(createSkeleton(name, id, int(health), int(damage)), army)
  elif (len(data) == 1):
      add(createSkeleton(data[0], id), army)
  print('Unit added')

def printSkeleton(skeleton):
  print('skeletonID - ', skeleton['id'])
  print('Name - ', skeleton['name'])
  print('Health - ', skeleton['health'])
  print('Damage - ', skeleton['damage'])

def printArmy(army):
  for unit in army:
    print('\n')
    printSkeleton(unit)
    print('\n---------------')