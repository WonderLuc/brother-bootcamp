name = input('Name of customer\n')
greeting = 'Hello! Can I Help you?'
regularCustomers = 'Ann Braver HeadChop Abby and Garry'

if (name in regularCustomers):
    greeting = 'Hello, {0}! Did you want to see new products?'.format(name)

if (name == 'Ann'):
    greeting = greeting.lower().replace('ann', 'Ann')
elif (name == 'Braver'):
    greeting = greeting.upper()
elif (name == 'Abby and Garry'):
    greeting = greeting.replace('Abby and Garry', 'Good boys')

print(greeting)