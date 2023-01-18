# Conditions

# If statement
# Kan je combineren met (meerdere) elif en een else
# Gebruikt : op einde van lijn
varSmallNumber = 6

if varSmallNumber < 5:
    varResult = 'Eerste if'
elif varSmallNumber > 7:
    varResult = 'Eerste elif'
elif varSmallNumber == 3:
    varResult = 'Tweede elif'
else:
    varResult = 'Else'

print("varResult is " + str(varResult))

# Switch-case in Python is een match-case
# Gebruik | om voorwaarden te scheiden
varStatus = 419

match varStatus:
    case 400:
        varStatusResult = "Bad request"
    case 404:
        varStatusResult = "Not found"
    case 418 | 419 | 420:
        varStatusResult = "This is nonsense"
    case _:
        varStatusResult = "Something's wrong with the internet"

print("varStatusResult is " + str(varStatusResult))
