# Iteration

# break --> verlaat binnenste lus
# continue --> keert terug naar begin van lus
# pass --> gebruik als tijdelijke TODO

# For lus
# Start default 0
# Step default 1
# bv. for index in range(start, stop, step):
#       something

startValue = 1
for i in range(5):
    startValue += 1
print(startValue)

# While lus
# Bv. while condition:
#       something
secondStartValue = 1
while secondStartValue <= 10:
    secondStartValue += 1
print(secondStartValue)

# Iteratie over een list
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
for fruit in fruits:
    print(fruit)

# Met index erbij
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print("-------------------------------")

# Controle if item exists, met index
# Geeft bij duplicates altijd de eerste index
print(fruits)
for fruit in fruits:
    if fruit in fruits:
        print(f"{fruits.index(fruit)}: {fruit}")

# Nieuwe lijst met bestaande items
fruitsStartingWithAnA = [fruit for fruit in fruits if fruit[0]=='a']
print(fruitsStartingWithAnA)