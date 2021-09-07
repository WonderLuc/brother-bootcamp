food = [
    ["Apple", 30], 
    ["Cake", 10], 
    ["Coffee", 100],
    ["Chocolate", 10],
    ["Orange", 50],
    ["Flour", 3],
    ["Mushrooms", 60], 
    ["Beer", 10]
]
spells = [
    ["Froggy", 15], 
    ["Ice", 29], 
    ["Fire", 99],
    ["Thunderbolt", 14],
    ["Cure", 50],
    ["Trap", 17],
    ["Search", 43], 
    ["Bag", 1000]
]
weapons = [
    ["Sword", 100], 
    ["Axe", 29], 
    ["Shield", 80],
    ["Bow", 40],
    ["Mace", 20],
    ["Spear", 10],
    ["Dart", 85], 
    ["Zweinhander", 1]
]

while (True):
    name = input("Welcome, whats your name?\n")

    # Manager actions
    if ('manager' in name):
        name = name.split(' ')
        if (name[1] == "close"):
            break
        elif (name[1] == "add"):
            store = food + spells + weapons
            isChanges = False
            for i in range(len(store)):
                if (name[2] == store[i][0]):
                    store[i][1] += int(name[3])
                    isChanges = True
                    break
                
    # Customer Action
    else:
        # Plays Once for each customer
        print('What I may do for you, {0}?\n'.format(name))
        # Customer Cycle
        while (True):
            print(' 1. Food\n 2. Spells\n 3. Weapons\n')
            category = input('Choose category\n').strip()

            if (category == "out"):
                break

            # Choose category
            print("That we have:\n")
            global arr
            if (category.lower() in '1. Food'.lower()):
                arr = food
            elif ( category.lower() in '2. Spells'.lower()):
                arr = spells
            elif (category.lower() in "3. Weapons".lower()):
                arr = weapons
            elif (category.lower() == "out"):
                print("Goodbye, {0}".format(name))
                break

            # print a list of products in list format - 1.Aplle - 30
            for i in range(len(arr)):
                print(
                    "{0}. {1} - {2}".format(
                        i + 1,
                        arr[i][0],
                        arr[i][1]
                    ))

            # Ask a certain product from the list
            product = input("What interesting for you?\n").split(' ')
            
            # Searching in a array product and show user a result
            for i in range(len(arr)):
                if (product[0].lower() == arr[i][0].lower()):
                    amount = arr[i][1]
                    userAmount = int(product[1])
                    if (amount - userAmount >= 0):
                        print("There your")
                        print("Thank you, {0}! Somthing more?\n".format(name))
                        arr[i][1] = amount - userAmount
                    else:
                        print ("Sorry we don't have enough")
                        print("{0} lefts you to buy".format(userAmount - amount))
                        arr[i][1] = 0
            print("\n---------------------------\n")
