arr = [
    ['Alice', True, 100],
    ['Joe', 30, False],
    [True, 'Megan', 200],
    [50, 'Oliver', False],
    [200, True, 'Rassel'],
    ['Molly', True, 2147000000]
]

# Print persons once
for person in arr:
    print(person)

while (True):
    print('\n')
    userCommand = input('Input who will take damage now\n')
    if (userCommand == 'out'):
        break
    elif (userCommand == 'show'):
        for person in arr:
            print(person)
        continue
    
    # Make array from user inputs for comfortable
    data = userCommand.split(' ')
    if (len(data) < 2):
        print('Incorrect input. Try again...\n')
        continue
    data[0] = data[0].title()
    data[1] = int(data[1])
    isFound = False
    global item

    # Founding person
    for i in range(len(arr)):
        if (isFound):
            break

        for j in range(len(arr[i])):
           item = arr[i]

           if (type(item[j]) == str):
               if (item[j].lower() == data[0].lower()):
                   isFound = True

    # Handle error with missing person
    if (not isFound):
        print("Error, target died or not exist")
        break
    
    # Calculate damage and friends status
    isFriend = False
    for i in range(len(item)):
        if (type(item[i]) == bool and not item[i]):
            print("Hey! Don’t touch yours friend, wierdo!")
            print("{0} try to dodge".format(data[0]))
            isFriend = True
        elif (type(item[i]) == int):
            if (item[i] <= 0):
                print("Error, target died or not exist")
                break
            if (isFriend): 
                print("{0} dodged".format(data[0]))
                break
            item[i] -= data[1]
            print("{0} had {1} damage".format(data[0], data[1]))
            if (item[i] <= 0):
                print("{0} die".format(data[0]))
                arr.pop(arr.index(item))
                break
    