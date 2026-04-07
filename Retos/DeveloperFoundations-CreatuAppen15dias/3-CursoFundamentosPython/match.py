dia = 4

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número de día no válido")

# Ingresar un día de la semana por teclado y mostrar una 
# actividad planificada para ese día utilizando match-case.

dia = input ("Ingresa el día de la semana (lunes, martes, miércoles, jueves, viernes, sábado, domingo): ").lower()

match dia:
    case "lunes":
        print("Planificar la semana y establecer metas.")
    case "martes":
        print("Trabajar en proyectos importantes.")
    case "miércoles":
        print("Reuniones y seguimiento de tareas.")
    case "jueves":
        print("Día de aprendizaje y desarrollo personal.")
    case "viernes":
        print("Finalizar tareas pendientes y preparar el fin de semana.")
    case "sábado":
        print("Tiempo para actividades recreativas y descanso.")
    case "domingo":
        print("Planificar la próxima semana y relajarse.")
    case _:
        print("Día no válido. Por favor, ingresa un día de la semana.")

# Reemplazar el caso anterior utilizando if-elif-else en lugar de match-case.
dia = input ("Ingresa el día de la semana (lunes, martes, miércoles, jueves, viernes, sábado, domingo): ").lower()
if dia == "lunes":
    print("Planificar la semana y establecer metas.")
elif dia == "martes":
    print("Trabajar en proyectos importantes.")
elif dia == "miércoles":
    print("Reuniones y seguimiento de tareas.")
elif dia == "jueves":
    print("Día de aprendizaje y desarrollo personal.")
elif dia == "viernes":
    print("Finalizar tareas pendientes y preparar el fin de semana.")
elif dia == "sábado":
    print("Tiempo para actividades recreativas y descanso.")
elif dia == "domingo":
    print("Planificar la próxima semana y relajarse.")
else:
    print("Día no válido. Por favor, ingresa un día de la semana.")
