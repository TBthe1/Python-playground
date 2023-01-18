# Strings

# Iets printen
print('Hello World')

# Variabelen
# Type definiëren niet nodig
# Kan verschillende types krijgen
# Single en double quotes zijn ok
# Nieuwe lijn --> \n
var1 = 'Hello'
var2 = 'World'
print(var1 + " " + var2 + "\nnieuwe lijn")

# Over meerdere lijnen --> tipple single or double quotes
var3 = '''This is
a long string over multiple lines
that will be overwritten'''
var3 = 2
print(var3)

# Speciale characters
print("It\'s a special character in the string here")

# Lengte + int to string
print('De lengte van var1 is ' + str(len(var1)))

# Slicing
# [startPositie : eindPositie]
# bv. print letters 1 en 2
print(var1[0:2])

# bv. print vanaf 3e letter tot het einde
print(var1[2:])

# Een character (char type) bestaat niet (in Python = een string met lengte 1)
# String kan je na declaratie niet aanpassen --> nieuwe maken
# Bv. Eerste letter van een string vervangen
print("B" + var1[1:])

# Tellen van achter naar voor --> negatieve
print(var1[-1])
print(var1[-2])
