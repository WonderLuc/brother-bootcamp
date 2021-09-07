name = input('Enter customer name\n')
print('How may items store have?')
number = int(input()) * len(name)

print('-------------------')
print('Welcome {name}!\nOur store have {number} items'.format(name = name, number = number))