x1 = 5

if x1 > 5:
    print('x es mayor que 5')
elif x1 == 5:
    print('x es igual a 5')
else:
    print('x es menor')

print('Fuera de if')
    
x2 = 15
y2 = 20

if x2>10 and y2>25:
    print('x2 es mayor que 10 y y2 es mayor que 25')

if x2>10 or y2>25:
    print('x2 es mayor que 10 o y2 es mayor que 25')
    
if not x2>10:
    print('x2 no es mayor que 10')
    
is_member = False
age = 15

if is_member:
    if age>=15:
        print('Tienes acceso ya que eres miembro y mayor o igual a 15 años')
    else:
        print('No tienes acceso ya que eres miembro pero menor a 15 años')
else:
    print('No eres miembro y NO TIENES ACCESO')
    

# Bucles y control de iteraciones

numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("Aquí i es igual a:", i+1)
    
for i in range(3, 10):
    print(i)
    
fruits =['Manzana', 'Pera', 'Uva', 'Naranja','Tomate']
for fruit in fruits:
    print(fruit)
    if fruit == 'Naranja':
        print('Naranja encontrada')
        
x3 = 0

while x3<5:
    if x3 == 3:
        break
    
    print(x3)
    x3 += 1
    

numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i ==3:
        continue
    print("Aquí i es igual a:", i)

# while x3 < 5:
#     if x3 == 3:
#         continue

#     print(x3)
#     x3 += 1


#Ejemplo de iterador
# Crear una lista

my_list = [1, 2, 3, 4]

# Obtener el iterador
my_iter = iter(my_list)

# Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#Iterar en cadenas
#Creando la cadena
text = 'Hola mundo'

#Creando el objeo iterador
iter_text = iter(text)

#Iterar en la cadena
for char in iter_text:
    print(char)


#Crear un iterador para los numeros impares

#Limite
limit = 10

#Crear iterador
odd_itter = iter(range(1, limit+1,2))

#Usar el iterador

for num in odd_itter:
    print(num)

def my_generator():
    yield 3
    yield 2
    yield 1
    
for value in my_generator():
    print(value)


#Fibonacci
# 0 1 1 2 3 5 8 13 21

def fibonacci(limit):
    a, b = 0, 1
    while a<limit:
        yield a
        a, b = b, a+b
for num in fibonacci(500):
    print(num)
    
#Generador de numeros pares

def even_numbers(limit):
    num = 0
    while num < limit:
        yield num
        num += 2

def odd_numbers(limit):
    num = 1
    while num < limit:
        yield num
        num += 2
        
for num in even_numbers(20):
    print(num)
    
for num in odd_numbers(20):
    print(num)

