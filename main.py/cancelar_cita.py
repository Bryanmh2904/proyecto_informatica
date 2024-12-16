def cancelar_cita(citas):
    print("\n Cancelar Cita ")
    
    if not citas:
        print("No hay citas registradas para cancelar.")
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
            print("Entrada inválida, por favor ingrese un número valido.")

    cedula_busqueda = input("\nIngrese el número de cédula del usuario: ").strip()

    cita_encontrada = None
    for cita in citas:
        if cita["cedula"] == cedula_busqueda and cita["servicio"] == servicio_seleccionado:
            cita_encontrada = cita
            break

    if not cita_encontrada:
        print("\nNo se encontró ninguna cita que coincida con los datos ingresados.")
        return

    print("\nCita encontrada:")
    print(f"Nombre: {cita_encontrada['nombre']}")
    print(f"Servicio: {cita_encontrada['servicio']}")
    print(f"Día: {cita_encontrada['dia']}")
    print(f"Hora: {cita_encontrada['hora']}")

    confirmar = input("\n¿Desea cancelar esta cita? (sí/no): ").strip().lower()
    if confirmar in ["si", "sí"]:
        citas.remove(cita_encontrada)
        print("\nLa cita ha sido cancelada con éxito.")
    else:
        print("\nLa cancelación fue anulada por el usuario.")
