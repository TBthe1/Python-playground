# Lambda

# Aanvraadt 1 of meerdere args
# Heeft een uitdrukking
# Retourneert het resultaat

# lambda params: expression
# is hetzelfde als
# def anonymous(parameters)
#   return expression

# Add 10 to argument a
def x(a): return a + 10
print(x(5))

# Multiply argument a with argument b
def x(a, b): return a * b
print(x(5, 6))

# Summarize argument a, b, and c
def x(a, b, c): return a + b + c
print(x(5, 6, 2))

# Anonymous functions
# That makes a number double
# And another one that triples a number
def myfunc(n):
  return lambda a : a* n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))