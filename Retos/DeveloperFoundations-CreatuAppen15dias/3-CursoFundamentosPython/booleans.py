from pathlib.types import PathInfo


v = True
f = False

print(v)
print(f)

print(5 > 3) # Verdadero
print(5 < 3) # Falso

print(type(v)) # <class 'bool'>
print(type(f)) # <class 'bool'>

# True
print(bool(132)) # True
print(bool("abc")) # True
print(bool([1, 2, 3])) # True
print(bool(["Manzana", "Pera"])) # True

# False
print(bool(0)) # False
print(bool("")) # False
print(bool([])) # False
print(bool(())) # False
print(bool({})) # False
print(bool(None)) # False

x = 10
y = 3.12
print(isinstance(x, int)) # True
print(isinstance(y, float)) # True
print(isinstance(x, float)) # False
print(isinstance(y, int)) # False

