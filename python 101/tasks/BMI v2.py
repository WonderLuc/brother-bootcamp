weight = float(input('Enter your weight(kg)\n'))
height = float(input('Enter your height(m)\n'))

result = weight / (height ** 2)

print(result)

if (result < 18.5): print('Underweight')
if (result >= 18.5 and result < 25): print('Normal')
if (result >= 25 and result < 30): print('Overweight')
if (result >= 30 and result < 35): print('Obese')
if (result >= 35 ): print('extremly obese')