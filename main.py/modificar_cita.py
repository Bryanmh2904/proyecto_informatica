def modificar_cita(citas):
    print("\n Modificar Cita ")
    
    if not citas:
        print("No hay citas registradas para modificar.")
        return
    
    servicios = ["Pediatría", "Geriatría", "Medicina General", "Odontología"]
    
    print("\nSeleccione el servicio en el que se encuentra la cita:")
    for i, servicio in enumerate(servicios):
        print(f"{i + 1}. {servicio}")
    
    while True:
        try:
            seleccion_servicio = int(input("Ingrese el número del servicio (1-4): "))
            if 1 <= seleccion_servicio <= 4:
                servicio_seleccionado = servicios[seleccion_servicio - 1]
                break
            else:
                print("Por favor, seleccione un número entre 1 y 4.")
        except ValueError:
            print("Entrada inválida, por favor ingrese un número válido.")

    cedula_busqueda = input("Ingrese el número de cédula para buscar la cita: ")
    cita_encontrada = None

    for cita in citas:
        if cita["cedula"] == cedula_busqueda and cita["servicio"] == servicio_seleccionado:
            cita_encontrada = cita
            break

    if not cita_encontrada:
        print("No se encontró ninguna cita con esa cedula en este servicio, verifique que selecciono el servicio correcto.")
        return

    print("\nCita encontrada:")
    print(f"Nombre: {cita_encontrada['nombre']}")
    print(f"Servicio: {cita_encontrada['servicio']}")
    print(f"Día: {cita_encontrada['dia']}")
    print(f"Hora: {cita_encontrada['hora']}")

    confirmar = input("¿Desea modificar esta cita? Escriba si o no: ").strip().lower()
    if confirmar not in ["si", "sí"]:
        return

    dias_disponibles = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    horas_disponibles = ["8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]

    print("\nSeleccione un nuevo día:")
    for i, dia in enumerate(dias_disponibles):
        print(f"{i + 1}. {dia}")
    
    while True:
        try:
            dia_seleccionado = int(input("Seleccione el día (1-6): "))
            if 1 <= dia_seleccionado <= 6:
                cita_encontrada["dia"] = dias_disponibles[dia_seleccionado - 1]
                break
            else:
                print("Por favor, seleccione un número entre 1 y 6.")
        except ValueError:
            print("Entrada inválida, por favor ingrese un número.")

    print("\nSeleccione una nueva hora:")
    for i, hora in enumerate(horas_disponibles):
        print(f"{i + 1}. {hora}")
    
    while True:
        try:
            hora_seleccionada = int(input("Seleccione la hora (1-9): "))
            if 1 <= hora_seleccionada <= 9:
                cita_encontrada["hora"] = horas_disponibles[hora_seleccionada - 1]
                break
            else:
                print("Por favor, seleccione un número entre 1 y 9.")
        except ValueError:
            print("Entrada inválida, por favor ingrese un número.")

    print("\n¡La cita ha sido modificada con éxito!")
    print(f"Nuevo Día: {cita_encontrada['dia']}")
    print(f"Nueva Hora: {cita_encontrada['hora']}")