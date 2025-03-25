import datetime


Reservas = [{"Cliente": "Pepillo", "Fecha": "12/05/2023", "Hora": "20:02", "Num_personas": 20, "Telefono": 690044592}, {"Cliente": "Juan", "Fecha": "19/01/2025", "Hora": "19:14", "Num_personas": 5, "Telefono": 890123409}]



def ver_reservas():
    for reserva in Reservas:
        print("Nombre del cliente:", reserva["Cliente"])
        print("Fecha:", reserva["Fecha"])
        print("Hora:", reserva["Hora"])
        print("Número de personas:", reserva["Num_personas"])
        print("---------------------------------------------")

def hacer_reserva():
    reserva_valida = False
    fecha_valida = False
    hora_valida = False
    personas_valida = False

    while reserva_valida == False:
        nom_cliente = input("Dime tu nombre: ")
        fecha_reserva = input("Perfecto, ahora dime la fecha para la reserva: ")
        fecha_reserva = datetime.datetime.strptime(fecha_reserva, "%d/%m/%Y").date()

        if fecha_reserva < datetime.date.today():
            print("Fecha no válida")
            continue
        else:
            reserva_valida = True
        
        hora_reserva = input("Ahora la hora de reserva: ")
        hora_reserva = datetime.datetime.strptime(hora_reserva, "%H:%M").time()

        hora_actual = datetime.datetime.now().time()

        if fecha_reserva == datetime.date.today() and hora_reserva < hora_actual:
            print("Hora no válida")
            return
        else:
            hora_valida = True

        num_personas = int(input("¿Cuántas personas seréis?: "))
        if num_personas <= 0:
            print("El número de personas debe ser mayor que 0")
        else:
            personas_valida = True
        if fecha_valida and hora_valida and personas_valida:
            reserva_valida = True
            break
        reserva_valida = True
        num_telefono = int(input("Finalmente, dime tu número de teléfono: "))

    nueva_reserva = {"Cliente": nom_cliente, "Fecha": fecha_reserva, "Hora": hora_reserva, "Num_personas": num_personas, "Telefono": num_telefono}
    Reservas.append(nueva_reserva)

# la edición funciona, pero cuando se pone un nombre o telefono no válido hace cosas raras  
def editar_reserva():
    while True:  # Bucle para seguir pidiendo datos hasta encontrar la reserva
        nombre_persona = input("Dime  tu nombre: ")
        num_telefono = int(input("Y ahora tu número de teléfono: "))

        encontrado = False  # Variable para verificar si encontramos la reserva

        for reserva in Reservas:
            if reserva["Cliente"] == nombre_persona and reserva["Telefono"] == num_telefono:
                encontrado = True  # Marcamos que encontramos la reserva
                print("Perfecto, ahora vamos a modificar la reserva.: ")
                while True:
                    modificar = input("¿Qué quieres modificar? escribe <NOMBRE>, <FECHA>, <HORA> o <PERSONAS>")
                    print("Escribe <FIN> si ya acabaste de modificar")
                    if modificar.lower() == "nombre":
                        nuevo_nombre = input("Dime el nombre a cambiar: ")
                        reserva["Cliente"] = nuevo_nombre
                    elif modificar.lower() == "fecha":
                        nueva_fecha = input("Dime una nueva fecha: ")
                        reserva["Fecha"] = nueva_fecha
                    elif modificar.lower() == "hora":
                        nueva_hora = input("Dime una nueva hora: ")
                        reserva["Hora"] = nueva_hora
                    elif modificar.lower() == "personas":
                        nueva_personas = input("Dime el nuevo número de personas: ")
                        reserva["Num_personas"] = int(nueva_personas)
                    elif modificar.lower() == "fin":
                        print("Edición finalizada, Gracias!")
                        return
        if not encontrado:
            print("No se encontró la reserva. Vuelve a intentar.")

def buscar_reserva():
    tipo_busqueda = input("Dime, ¿quieres buscar por <CLIENTE> o por <FECHA>? ")

    if tipo_busqueda.lower() == "cliente":
        nom_cliente = input("De acuerdo, dime tu nombre: ")
        for reserva in Reservas:
            if reserva["Cliente"] == nom_cliente:
                print(f"Nombre: {reserva['Cliente']}, Fecha: {reserva['Fecha']}, Hora: {reserva['Hora']}, Número de personas: {reserva['Num_personas']}")
    elif tipo_busqueda.lower() == "fecha":
        fecha_cliente = input("De acuerdo, dime la fecha: ")
        for reserva in Reservas:
            if reserva["Fecha"] == fecha_cliente:
                print(f"Nombre: {reserva['Cliente']}, Fecha: {reserva['Fecha']}, Hora: {reserva['Hora']}, Número de personas: {reserva['Num_personas']}")



def cancelar_reserva():
    nom_cliente = input("Dime el nombre del cliente de la reserva: ")
    fecha_reserva = input("Y finalmente la fecha de la reserva: ")
    encontrado = False
    while encontrado == False:
        posicion = 0
        for reserva in Reservas:

            if reserva["Cliente"] == nom_cliente and reserva["Fecha"] == fecha_reserva:
                del Reservas[posicion]
                print("Reserva eliminada con éxito!")
                encontrado = True
                break
            else:
                encontrado = False
        if encontrado == False:
            print("Reserva no encontrada, vuelve a intentarlo.")
def menu():
    while True:
        print("\nMenú:")
        print("1. Ver reservas")
        print("2. Hacer nueva reserva")
        print("3. Editar reserva")
        print("4. Buscar reserva")
        print("5. Cancelar reserva")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ver_reservas()
        elif opcion == '2':
            hacer_reserva()
        elif opcion == '3':
            editar_reserva()
        elif opcion == '4':
            buscar_reserva()
        elif opcion == '5':
            cancelar_reserva()
        elif opcion == '6':
            print("Datos guardados en memoria. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    menu()