def reservar_cita(citas):
    servicios = ["Pediatría", "Geriatría", "Medicina General", "Odontología"]
    dias_disponibles = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    horas_disponibles = ["8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]

    print("\nSeleccione un servicio:")
    for i, servicio in enumerate(servicios):
        print(f"{i + 1}. {servicio}")
    
    while True:
        try:
            seleccion = int(input("Ingrese el número del servicio (1-4): "))
            if 1 <= seleccion <= 4:
                servicio = servicios[seleccion - 1]
                break
            else:
                print("Por favor, seleccione un número entre 1 y 4.")
        except ValueError:
            print("Entrada inválida, por favor ingrese un número.")

    print("\nSeleccione un día:")
    for i, dia in enumerate(dias_disponibles):
        print(f"{i + 1}. {dia}")
    
    while True:
        try:
            dia_seleccionado = int(input("Seleccione el día (1-6): "))
            if 1 <= dia_seleccionado <= 6:
                dia = dias_disponibles[dia_seleccionado - 1]
                break
            else:
                print("Por favor, seleccione un número entre 1 y 6.")
        except ValueError:
            print("Entrada inválida, por favor ingrese un número.")

    print("\nSeleccione una hora:")
    for i, hora in enumerate(horas_disponibles):
        print(f"{i + 1}. {hora}")
    
    while True:
        try:
            hora_seleccionada = int(input("Seleccione la hora (1-9): "))
            if 1 <= hora_seleccionada <= 9:
                hora = horas_disponibles[hora_seleccionada - 1]
                break
            else:
                print("Por favor, seleccione un número entre 1 y 9.")
        except ValueError:
            print("Entrada inválida, por favor ingrese un número.")

    for cita in citas:
        if cita["servicio"] == servicio and cita["dia"] == dia and cita["hora"] == hora:
            print(f"\nLo siento, ya hay una cita para {servicio} el {dia} a las {hora}.")
            return

    nombre = input("Ingrese su nombre y apellidos: ")
    cedula = input("Ingrese su número de cédula: ")
    telefono = input("Ingrese su número de teléfono: ")

    cita = {
        "nombre": nombre,
        "cedula": cedula,
        "telefono": telefono,
        "servicio": servicio,
        "dia": dia,
        "hora": hora
    }
    citas.append(cita)

    print(f"\n¡Hola! Su cita para el servicio de {servicio} ha sido reservada para el día {dia} a las {hora}. ")