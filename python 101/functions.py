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
# Two-Bedroom Apartment will costs you 300,
# Adam. And you can check in already 21/08/2021
separate()

# Lambda
powerBy = lambda x,y: x**y
print(powerBy(4, 2)) # 16
separate()

def pow(n):
    return lambda x: x**n

powByTwo = pow(2)
powByThree = pow(3)
print(powByTwo(2)) # 4
print(powByThree(2)) # 8
separate()

# Scope
def printFive():
    x = 5
    print(x)

printFive() # 5
# print(x) # NameError: name 'x' is not defined
separate()

y = 10
def printNine():
    y = 9
    print(y)

printNine() # 9
print(y) # 10
separate()

def printNum():
    global z
    z = 12
    global y
    y = 5
    print(z)
    print(y)

printNum() # 12 \n 5
print(z) # 12
print(y) # 5
separate()

# Decorators

def printHello(func):
    def newfunc():
        print('Hello Decorator')
        func()
    return newfunc

decorated = printHello(printFive)
decorated() # Hello Decorator \n 5
printHello(printFive)() # Hello Decorator \n 5

@printHello
def printTwo():
    print(2)

printTwo() # Hello Decorator \n 2

def printBorders(func):
    def newF(*args, **kwargs):
        print('---TOP---')
        result = func(*args, **kwargs)
        print(result)
        print('---BOTTOM---')
        return result
    return newF

printBorders(min)(1,5)
# ---TOP---
# 1
# ---BOTTOM---

def printBordersForMin(func):
    def newF(x,y):
        print('---TOP---')
        result = func(x, y)
        print(result)
        print('---BOTTOM---')
        return result
    return newF

printBordersForMin(min)(10, 3)
# ---TOP---
# 3
# ---BOTTOM---
