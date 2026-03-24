# Operadores de comparación

x = 5
y = 3
z = 5

print("x es igual a y:", x == y) # False
print("x es diferente de y:", x != y) # True
print("x es mayor que y:", x > y) # True
print("x es menor que y:", x < y) # False
print("x es mayor o igual que y:", x >= y) # True
print("x es menor o igual que y:", x <= y) # False
print("z es igual a x", x == z) # True

# Operadores lógicos

#       True    False
print(x > y and y > z ) # False
print(x > y or y > z ) # True

v = True
f = False

print(not(v))
print(not(f))
