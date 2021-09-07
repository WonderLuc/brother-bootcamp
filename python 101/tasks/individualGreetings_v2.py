while (True):
    name = input('Name of customer\n').lower()
    if (name == 'out'):
        break
    greeting = 'Hello! Can I Help you?'
    regularCustomers = ['ann', 'braver', 'headchop']

    if (name in regularCustomers):
        greeting = 'Hello, {0}! Did you want to see new products?'.format(name.title())

    if (name == 'ann'):
        greeting = greeting.lower().replace('ann', 'Ann')
    elif (name == 'braver'):
        greeting = greeting.upper()

    print(greeting)