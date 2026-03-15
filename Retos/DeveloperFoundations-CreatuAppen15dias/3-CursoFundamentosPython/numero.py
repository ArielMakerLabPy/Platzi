from operator import neg
from tkinter import YES


x = 1
y = 2.5
z = 1j

print(type(x))
print(type(y))
print(type(z))

positivo = 5.5
negativo = -5.5

imaginario = -5 - 1j

xf = float(x)

print(xf)
print(type(xf))

ye = int(y)
print(ye)
print(type(ye))

enteroComplejo = complex(x)
flotanteComplejo = complex(y)

print(enteroComplejo)
print(flotanteComplejo) 
print(type(enteroComplejo))
print(type(flotanteComplejo))  

import random

print(random.randrange(1, 10)) # Output: un número entero aleatorio entre 1 y 10 (excluyendo el 10) es decir hasta 9
print(random.randint(1, 10)) # Output: un número entero aleatorio entre 1 y 10 (incluyendo el 10)
