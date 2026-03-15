
print('Hola "Mundo"')

ingles = "I'm a developer"

Multilinea = """Esto
 es
   un
     texto
multilinea"""
print(Multilinea)
print(type(Multilinea))
print(ingles)

palabra = 'Murciélago'
print(len(palabra))

texto = 'Este curso es de fundamentos de Python'
estaIncluida = 'Python' in texto
noEstaIncluida = 'Javascript' not in texto
noEstaIncluida2 = 'es' not in texto

print(texto)
print(estaIncluida)
print(noEstaIncluida)
print(noEstaIncluida2)

mayuscula = texto.upper()
minuscula = texto.lower()
print(mayuscula)
print(minuscula)

espacios = '         Este es el texto'
sinEspacios = espacios.strip()
print(espacios)
print(sinEspacios)

textoMinuscula = texto.lower()
busqueda = 'python' in textoMinuscula
print(busqueda)

