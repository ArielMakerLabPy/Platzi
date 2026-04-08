# agrega en cada linea comentarios de lo que esta haciendo el codigo
i = 0 # inicializa la variable i con el valor 0

while i < 10: # inicia un ciclo while que se ejecutará mientras i sea menor que 10
    i += 1 # incrementa el valor de i en 1 en cada iteración del ciclo, lo que permite que el ciclo eventualmente termine cuando i alcance el valor de 10
    if i == 5: # si el valor de i es igual a 5
        continue # se ejecuta la instrucción continue, lo que hace que el ciclo while salte la iteración actual y pase a la siguiente, incluso si i aún es menor que 10    
    
    print(i) # imprime el valor actual de i en cada iteración del ciclo, lo que permite ver cómo va cambiando el valor de i a medida que se ejecuta el ciclo while.
else: # una vez que el ciclo while termina, se ejecuta el bloque de código dentro del else, lo que indica que el ciclo ha finalizado. El bloque de código dentro del else se ejecutará solo si el ciclo while termina normalmente (es decir, no se interrumpe con una instrucción break).
    print("i dejó de ser menor que 10") # una vez que el ciclo while termina, se imprime el mensaje "i dejó de ser menor que 10" para indicar que el ciclo ha finalizado.

