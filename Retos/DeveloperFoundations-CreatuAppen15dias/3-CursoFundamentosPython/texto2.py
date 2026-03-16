# ind o indentación 0123456...

texto = 'Este es un texto'

print(texto[0])  # E
print(texto[1])  # s
print(texto[2])  # t
print(texto[3])  # e
print(texto[4])  # ' ' (espacio)

#slicing
print(texto[:-2])  # Este es un tex

# replace
print(texto.replace('texto', 'string'))  # Este es un string

# split
print(texto.split())  # ['Este', 'es', 'un', 'texto']
# join
print(' '.join(['Este', 'es', 'un', 'texto']))  # Este es un texto

# Normalización
texto_mayusculas = texto.upper()
print(texto_mayusculas)  # ESTE ES UN TEXTO

texto_minusculas = texto.lower()
print(texto_minusculas)  # este es un texto

texto2 = 'Este texto contiene MAYúSCULAS y minusculas y necesito encontrar ciertas palabras'
print('Mayúsculas'.lower() in texto2.lower())  # True

palabra = "Python"
print(palabra[0:2])  # Py
