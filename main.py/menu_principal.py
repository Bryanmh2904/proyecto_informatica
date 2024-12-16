from reservar_cita import reservar_cita
from modificar_cita import modificar_cita
from cancelar_cita import cancelar_cita

def salir_sistema():
    print("Saliendo del sistema. ¡Gracias!")

def menu_principal():
    citas = []
    while True:
        print("\nMenú Clínica sin Dolor")
        print("1. Reservar Cita")
        print("2. Modificar Cita")
        print("3. Cancelar Cita")
        print("4. Salir")

        try:
            seleccion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if seleccion == 1:
            reservar_cita(citas)
        elif seleccion == 2:
            modificar_cita(citas)
        elif seleccion == 3:
            cancelar_cita(citas)
        elif seleccion == 4:
            salir_sistema()
            break
        else:
            print("Selección no válida, ingrese nuevamente.")


menu_principal()