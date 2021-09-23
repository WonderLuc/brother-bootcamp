# Basic functions 
def createSkeleton(name, id, health=20, damage=10):
  id = id + 1
  return {
    'name' : name,
    'health' : health,
    'damage': damage,
    'id': id
  }

def add(skeleton, army):
  army.append(skeleton)

def find(id, army):
  for unit in army:
    if (unit['id'] == id): return unit
  return 0

def delete(id, army):
  for i in range(len(army)):
    if (army[i]['id'] == id):
      army.pop(i)
      return 1
  return 0

def sendToHero(skeleton, hero, army):
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
    delete(skeleton['id'], army)