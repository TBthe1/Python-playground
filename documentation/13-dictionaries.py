# Dictionaries

# List        []
# Tuple       ()
# Dictionary  {}

# Bevat key-value pairs
# Kinda een list van tuples

# Nieuwe dictionary aanmaken
emptyDict = {}

# Voorbeeld opgevulde dictionary
person = {
  'firstName': 'John',
  'lastName': 'Doe',
  'age': 25,
  'favoriteColors': ['blue', 'green']
}

# Item ophalen
# [index] of get()
varFirstName = person['firstName']
print(varFirstName)
varFirstName = person.get('firstName')
print(varFirstName)

# Nieuwe waarde toekennen
print(person.get('age'))
person['age'] = 26
print(person.get('age'))

# Over keys lopen
for key in person:
# for key in person.keys():
  print(key)

print("-----------------------------")

# Over values lopen
for val in person.values():
  print(val)

print("-----------------------------")

# Over key en value lopen
for key, val in person.items():
  print(f'{key} --> {val}')

print("-----------------------------")

# Een paar verwijderen
del person['age']
print(person)