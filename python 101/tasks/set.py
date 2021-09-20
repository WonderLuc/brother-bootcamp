names = ['Lucy', 'Frank', 'Ann', 'Garry', 'Frank', 'Alex', 'Penny', 'Garry', 'Tom', 'Frank']
Emails = ['josh', 'alex', 'lord', 'marry', 'penny', 'dog'] 
Magazine = ['alex', 'frank', 'harry', 'yourCrash', 'lord']


setNames = set(names)
print(setNames)

witoutDuplicates = []
for name in names:
  if (not name in witoutDuplicates):
    witoutDuplicates.append(name)
print(witoutDuplicates)

emails = set(Emails)
magazine = set(Magazine)

print(emails.difference(magazine))
print(magazine.difference(emails))
print(emails.intersection(magazine))