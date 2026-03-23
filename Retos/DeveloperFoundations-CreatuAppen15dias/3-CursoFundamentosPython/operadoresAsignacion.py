# Operadores Asignación

x = 5
x = x + 3 # x ahora es 8

x = x - 3 # x ahora es 5

x += 3 # x ahora es 8 SUMA
x -= 3 # x ahora es 5 RESTA
x *= 3 # x ahora es 15 MULTIPLICACIÓN
x /= 3 # x ahora es 5.0 (float) DIVISIÓN
x %= 2 # x ahora es 1.0 (resto de la división) MÓDULO

y = 20
y //= 2 # y ahora es 10 (división entera)
y **= 3 # y ahora es 1000 (potencia)


print(x) # 1.0
print(y) # 10

# WALRUS (Python 3.8+) Morsa
# Permite asignar y devolver un valor en la misma expresión
print(z := 3)
print(z) # 3