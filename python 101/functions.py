def helloWorld():
    print('Hello World')

def separate():
    print("_-_-_-_-_-_-_-_-_")

helloWorld()

# Args
def addFive(x):
    print(x + 5)

addFive(5) # 10
separate()

# Return 
def min(x, y):
    if( x > y): return y
    return x

print(min(5, 8)) # 5
separate()

# Arbitrary Arguments
def kidPrinter(*kids):
    for i in range(len(kids)):
        print(kids[i])
    
kidPrinter('Alex', 'Glory', 'Pickle')
separate()

# Named args
def bodySculpt(head, body, arms, legs):
    print(head)
    print(arms)
    print(body)
    print(legs)

bodySculpt(legs='Tail', head="Fairy", arms='Human Arm', body='bug')
# Fairy Human Arm bug Tail
separate()

#Kwargs
def beatMaker(**kwargs):
    for i in range(kwargs["times"]):
        str = ""
        for j in range(i):
            str += " "
        str += kwargs["beat"]
        print(str)

beatMaker(beat="LAmO", times=5)
separate()

# Default args
def greeting(name="Joe Doe"):
    print('Hello ' + name)

greeting('Alex') # Hello Alex
greeting() # Hello Joe Doe
separate()

# with Dict
def rentCalc(data):
    rentSum = data['time'] * data['money']
    str = f"""{data["obj"].title()} will costs you {rentSum},
{data["name"]}. And you can check in already {data["date"]}"""
    print(str)

rentCalc({
    "time": 3,
    "money": 100,
    "obj": "two-bedroom apartment",
    "name": "Adam",
    "date": "21/08/2021"
})
separate()

# Lambda
powerBy = lambda x,y: x**y
print(powerBy(4, 2)) # 16
separate()