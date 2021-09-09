str = "  hello WorlD {0}. My name is {name}    "


print(str.find('e'))
print(str.title())	
print(str.swapcase())
print(str.upper())
print(str.lower())
print(str.count('l'))
print(str.encode('ascii'))

print(str.format(334, name="Alex"))
print(str.replace(".", '\n'))
print(str.join("AB"))
print(str.split("."))
print(str.strip())
name = 'Oldrik'
print(f'It\'s my old friend - {name}')

print(str.isalnum())
print(str.isalpha())
print(str.isdecimal())
print(str.isdigit())
print(str.isidentifier())
print(str.islower())
print(str.isnumeric())
print(str.isprintable())
print(str.isspace())
print(str.istitle())
print(str.isupper())