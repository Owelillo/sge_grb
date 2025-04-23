import datetime


Vehiculos = [{"Id": "0001", "Marca": "Audi", "Modelo": "Si", "Num_pasajeros": 5, "Combustible": "gasolina", "Consumo": 20}]

Viajes = [{"Nombre": "Go", "Destino": "Manzanilla", "Fecha": "20/05/2025", "Vehiculo": "Audi", "Pasajeros": "2", "Distancia": 200}]

contador_ids = 1
def añadir_vehiculo():
    global contador_ids
    while True:
        marca = input("Dime la marca del vehículo: ")
        if not marca:
            print("La marca es obligatoria")
        else:
            break

    while True:
        modelo = input("Dime el modelo del vehículo: ")
        if not modelo:
            print("El modelo es obligatorio")
        else:
            break

    # debe ser un número
    while True:
        num_pasajeros = input("Ahora el número de pasajeros: ")
        if not num_pasajeros.isdigit():
            print("El número de pasajeros debe ser un número")
        else:
            break
    # debe ser una de las tres opciones
    while True:
        combustible = input("Dime el tipo de combustible ('Gasolina', 'Gasoleo' o 'GLP'): ")

        if combustible.lower() == 'gasolina' or combustible.lower() == 'gasoleo' or combustible.lower() == 'glp':
            break
        else:
            print("El combustible debe ser Gasolina, Gasóleo o GLP")

    # debe ser un número
    while True:
        consumo = int(input("Dime el consumo en litros: "))
        if not num_pasajeros.isdigit():
            print("El consumo debe ser un número")
        else:
            break
    
    # convierto en una cadena el contador. y se colocan 4 números, poniendo 0 si hace falta
    vehiculo_id = f"{contador_ids:04d}"
    contador_ids+=1


    nuevo_vehiculo = {"Id": vehiculo_id, "Marca": marca, "Modelo": modelo, "Num_pasajeros": num_pasajeros, "Combustible": combustible.lower(), "Consumo": consumo}
    Vehiculos.append(nuevo_vehiculo)
    print("Vehículo añadido con éxito!")


def mostrar_vehiculos():
    for vehiculo in Vehiculos:
        print(f"Id: {vehiculo['Id']}, Marca: {vehiculo['Marca']}, Modelo: {vehiculo['Modelo']} Número de pasajeros: {vehiculo['Num_pasajeros']} Combustible: {vehiculo['Combustible']} Consumo: {vehiculo['Consumo']}")



def eliminar_vehiculo():
    id = input("Dime el id del vehículo a eliminar: ")
    modelo = input("Dime el modelo del vehículo: ")

    vehiculo_encontrado = False
    for vehiculo in Vehiculos:
        if vehiculo['Id'] == id and vehiculo['Modelo'] == modelo:
            Vehiculos.remove(vehiculo)
            print(f"El vehículo {vehiculo['Marca']} ha sido eliminado con éxito")
            vehiculo_encontrado = True
            break            
    if vehiculo_encontrado == False:
        print("No se pudo encontrar el vehiculo.")

def añadir_viaje():
    nombre_viaje = input("Dime el nombre del viaje: ")
    destino = input("Ahora el destino del viaje: ")
    while True:
        fecha = input("Perfecto, ahora dime la fecha: ")
        fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
        if fecha < datetime.date.today():
            print("Fecha no válida")
            return
        else:
            break
    
    for vehiculo in Vehiculos:
        print("Vehículos dados de alta: ")
        print(f"Id: {vehiculo['Id']}, Marca: {vehiculo['Marca']}")

    id = input("Escoge el id del vehículo que quieras: ")
    vehiculo_encontrado = False
    while vehiculo_encontrado == False:
        for vehiculo in Vehiculos:
            if id == vehiculo["Id"]:
                print(f"Perfecto, irás con tu {vehiculo['Marca']}")
                vehiculo_encontrado = True
                break
            else:
                print("Buscando vehículo...")
                vehiculo_encontrado = False
        if vehiculo_encontrado == False:
            print("No hemos encontrado el vehículo, inténtalo de nuevo.")
    
    pasajeros = int(input("Dime el número de pasajeros que queréis ir: "))

    for vehiculo in Vehiculos:
        if vehiculo['Id'] == id:
            while True:
                num_pasajeros = int(vehiculo['Num_pasajeros'])
                if pasajeros > num_pasajeros:
                    print("El número de pasajeros debe ser igual o menor al máximo.")
                    pasajeros = int(input("Dime un número de pasajeros válido: "))
                else:
                    print("Perfecto, ya casi lo tenemos.")
                    break
        while True:
            distancia = input("Finalmente dime la distancia que váis a recorrer: ")
            if not distancia.isdigit():
                print("La distancia debe ser un número.")
            else:
                break
    
        print("Ya tengo todos los datos, creando el viaje...")
        nuevo_viaje = {'Nombre': nombre_viaje, 'Destino': destino, 'Fecha': fecha, 'Vehiculo': vehiculo, 'Pasajeros': pasajeros, 'Distancia': distancia}
        Viajes.append(nuevo_viaje)
        print("Viaje añadido correctamente.")


def mostrar_viajes():
    for viaje in Viajes:
        # aquí entendí el coste dependiendo de los kms que se recorran
        distancia = int(viaje['Distancia'])
        # multipliqué el coste medio de cada km x la distancia
        coste_viaje = int(distancia * 0.26)
        num_personas = int(viaje["Pasajeros"])
        coste_por_persona = coste_viaje / num_personas

        print(f"Nombre del viaje: {viaje['Nombre']},  Coste del viaje: {coste_viaje}€, Coste por persona: {coste_por_persona}€, Destino: {viaje['Destino']}, Fecha: {viaje['Fecha']}, Vehiculo: {viaje['Vehiculo']}, Pasajeros: {viaje['Pasajeros']}, Distancia: {viaje['Distancia']}")

def buscar_viaje_por_destino():
    destino = input("Dime el destino del viaje que quieres encontrar: ")
    encontrado = False
    for viaje in Viajes:
        if viaje['Destino'] == destino:
            print(f"Nombre del viaje: {viaje['Nombre']}, Destino: {viaje['Destino']}, Fecha: {viaje['Fecha']}, Vehiculo: {viaje['Vehiculo']}, Pasajeros: {viaje['Pasajeros']}, Distancia: {viaje['Distancia']}")
            encontrado = True
    
    if encontrado == False:
        print("No pudimos encontrar un viaje con ese destino.")


def estadisticas_coste():
    suma = 0
    costes_cada_persona = []
    for viaje in Viajes:
        distancia = int(viaje['Distancia'])
        coste_viaje = int(distancia * 0.26)
        # aquí ya tengo el coste total de cada viaje
        suma = suma + int(coste_viaje)

        # ahora calculo el coste de viaje por persona
        num_personas = int(viaje["Pasajeros"])
        coste_por_persona = coste_viaje / num_personas
        costes_cada_persona.append(coste_por_persona)

    # sumo todos los costes y los divido entre cada uno de las personas
    media_persona = sum(costes_cada_persona) / len(costes_cada_persona)

    print(f"El coste del viaje de todos los viajes es: {coste_viaje} Y la media por persona es de {media_persona}")

def estadisticas_por_vehiculo():
    su_vehiculo = input("¿De qué vehículo quieres ver sus estadísticas?")
    id = input("Dime el id del vehículo: ")
    suma = 0
    for vehiculo in Vehiculos:
        km_totales = 0
        if vehiculo['Id'] == id:
            for viajes in Viajes:
                if viajes['Vehiculo'] == su_vehiculo:
                    # aquí ya tengo los km totales
                    km_totales += viajes['Distancia']

            combustible = vehiculo['Combustible']
            precio_por_litro = 0.00
            if combustible == 'gasolina':
                # precio custom para cada tipo de combustible
                precio_por_litro = 0.26
            elif combustible == 'gasoleo':
                # precio custom para cada tipo de combustible
                precio_por_litro = 1.44  
            elif combustible == 'GLP':
                # precio custom para cada tipo de combustible
                precio_por_litro = 1.76
            for viaje in Viajes:
                distancia = int(viaje['Distancia'])
                coste_viaje = int(distancia * precio_por_litro)
                # aquí ya tengo el coste total de todos los viajes con ese vehiculo
                suma = suma + int(coste_viaje)
            todos_pasajeros = []
            for viaje in Viajes:
                pasajeros = int(viaje['Pasajeros'])
                todos_pasajeros.append(pasajeros)
                # aquí ya tengo la media de pasajeros
            media_pasajeros = sum(todos_pasajeros) / len(todos_pasajeros)

            # el coste medio por pasajero cada 100 km no lo hice

            print(f"Kilómetros totales: {km_totales}, Combustible: {combustible}, Precio por litro: {precio_por_litro}, Coste total de todos los viajes: {suma}, Media pasajeros: {media_pasajeros}")

def mostrar_viajes_mas_cortos_largos():
    viajes_cortos = []
    viajes_largos = []

    if not Viajes:
        print("No hay ningún viaje.")

    # inicializo min y max distancia para que la primera vez SIEMPRE se añada (porque no hay nada en las listas)
    min_distancia = float('inf')
    max_distancia = float('-inf')
    for viaje in Viajes:
        distancia = int(viaje['Distancia'])
        nombre = viaje['Nombre']

        # compruebo las posiciones 1, 2 y 3 de viajes_cortos para colocar el viaje en el lugar adecuado
        if len(viajes_cortos) < 3:
            viajes_cortos.append((distancia, nombre))  # si hay menos de 3 viajes, agrego el nuevo directamente
            viajes_cortos.sort(reverse=True)
        else:
            ## si ya hay al menos 3 viajes
            if distancia < viajes_cortos[2][0]:  # con el 2 escojo el 3er viaje, y con el 0 escojo la distancia de la tupla
                viajes_cortos[2] = (distancia, nombre)  # reemplazo al más largo de los 3 más cortos
                viajes_cortos.sort()  # ordeno de nuevo

        if len(viajes_largos) < 3:
            viajes_largos.append((distancia, nombre))
            viajes_largos.sort()
        else:
            ## si ya hay al menos 3 viajes
            if distancia > viajes_largos[2][0]:
                viajes_largos[2] = (distancia, nombre)
                viajes_largos.sort()

    print(f"Viajes más cortos: {viajes_cortos}, Viajes más largos: {viajes_largos}")       

# INFO:
# -------------
# en el caso de que tenga una tupla, por ejemplo tupla = [["Gabriel", 2]]
# se accede con tupla[0][1] si quisiese tener el 2, por ejemplo

# si no es una tupla, simplemente se accede con lista[0], lista[1], etc

def menu():
    while True:
        print("\nMenú:")
        print("1. Añadir vehículo")
        print("2. Mostrar vehóculos")
        print("3. Eliminar vehículo")
        print("4. Añadir viaje")
        print("5. Mostrar viajes")
        print("6. Buscar viaje por destino")
        print("7. Estadísticas de coste")
        print("8. Estadísticas por vehículo")
        print("9. Mostrar viajes mas cortos/largos")
        print("Q. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            añadir_vehiculo()
        elif opcion == '2':
            mostrar_vehiculos()
        elif opcion == '3':
            eliminar_vehiculo()
        elif opcion == '4':
            añadir_viaje()
        elif opcion == '5':
            mostrar_viajes()
        elif opcion == '6':
            buscar_viaje_por_destino()
        elif opcion == '7':
            estadisticas_coste()
        elif opcion == '8':
            estadisticas_por_vehiculo()
        elif opcion == '9':
            mostrar_viajes_mas_cortos_largos()
        elif opcion == 'q':
            print("Datos guardados en memoria. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    menu()