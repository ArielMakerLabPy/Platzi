palabra = "Python"

for letra in palabra:
    print(letra)
# Salida:
# P
# y
# t
# h
# o
# n

adjetivos = ["rica", "saludable"]
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)

for fruta in frutas:
    if fruta == "banana":
        continue
    print("¡Encontré una banana!")
else:
    print("Ya termino el ciclo for")

for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, "es", adjetivo)

print("-------------------------------------------")

for fruta in frutas:
    for adjetivo in adjetivos:
        print(fruta, "es", adjetivo)


print("-------------------------------------------")
# Range
# Comienza en 0, termina antes de 10, incrementa de 1 en 1
for i in range(10):
    print(i)

print("-------------------------------------------")

for i in range(3, 5):
    print(i)
print("-------------------------------------------")
for i in range(0, 40, 2):
    print(i)
