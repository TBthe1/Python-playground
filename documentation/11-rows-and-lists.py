# Rows and lists

# Ongeorde verzameling items + veranderbaar

# Element ophalen o.b.v. index
# Laatste element staat op -1
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
print(fruits[0])
print(fruits[-3])

# Sorteer een list
sortedFruits = sorted(fruits)
print(sortedFruits)

# Nieuwe lijst die omgedraaid is
fruitsReversed = fruits[::-1]
print(fruitsReversed)

# Deel van een lijst ophalen
# subLijst = lijst[begin: end: step]
# Alle parameters zijn optioneel
firstThreeFromFruits = fruits[0: 3]
print(firstThreeFromFruits)

# Waarden toekennen 
# Lijst uitbreiden (door meer waarden toe te kennen)
fruits[0:2] = ['coconut', 'kiwi', 'orange']
print(fruits)

# Waarden verwijderen
# 1 waarde          --> del fruits[0]
# Meerdere waardes  --> del fruits[0:2]
del fruits[0:2]
print(fruits)

# Aantal tellen                             --> count()
# Element achteraan toevoegen               --> append()
# Element invoegen op een plaats            --> insert(pos)
# Laatste element verwijderen en returnen   --> pop()
# Een bepaald element verwijderen           --> remove()
# Volgorde omdraaien                        --> reverse()
# Concatenatie                              --> +
