x = 5
y = 3
z = 10

if x > y or x > z:
    print("x es mayor que y o z")
elif x == y and x == z:
    print("x es igual a y y z")
else:
    print("Ninguna de las condiciones anteriores se cumple")

a = "Python"
b = "Javascript"
c = "Python"

if a == b:
    print("a es igual a b")
elif a == c:
    print("a es igual a c")
else:
    print("a no es igual a b ni a c")

if a == c:
    if a == b:
        print("a es igual a b y c")
    else:
        print("a es igual a c pero distinto de b")
else:
    print("a no es igual a c")

e = 10
f = 10

if e == f:
    pass # No hace nada, solo se usa como marcador de posición
