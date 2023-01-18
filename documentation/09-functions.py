# Functions

# Gebruikt keywords def
# Parameters gescheiden door een komma
# Kunnen defaults meekrijgen
# Altijd aanroepen met evenveel parameters als gedefinieerd (zonder een default)
# Return value is niet noodzakelijk
# Default return waarde is 'None'

def greet(name, message='Hi! My name is'):
    return f"{message} {name}"


print(greet('Bjorn'))
print(greet('Bjorn', 'Koekoek! I am'))  # overwrite default message param
