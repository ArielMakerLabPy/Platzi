# Operadores aritméticos

x = 5
y = 10

# Suma +
print("Suma:", x + y)

# Resta -
print("Resta:", x - y)

# Multiplicación *
print("Multiplicación:", x * y)

# División / (siempre devuelve un float)
print("División:", x / y)

# Módulo % (devuelve el resto de la división)
print("Módulo:", y % x)

# Potencia **
print("Potencia:", y ** x) # 100000

# División entera // (devuelve el cociente sin el resto)
print("División entera:", y // x) # 2

par = 8
print(par % 2 == 0) # True, es par

impar = 7
print(impar % 2 == 0) # False, es impar

# Precedencia de operadores
# Paréntesis > Potencia > Multiplicación/División, divisiones enteras y restos > Suma/Resta > Comparaciones de identidad y pertenencia > Operadores lógicos

resultado = 3 + 4 * 2 # Multiplicación se evalúa primero
print("Resultado sin paréntesis:", resultado) # 11
