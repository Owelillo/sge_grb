Alumnos = [
    {"Nombre": "Gabriel", "Apellidos": "Rojas Barredo", "Codigo": "0001", "Modulos": {"Programacion": 8}},
    {"Nombre": "Lucía", "Apellidos": "Fernández Pérez", "Codigo": "0002", "Modulos": {}},
    {"Nombre": "Carlos", "Apellidos": "Gómez Ruiz", "Codigo": "0003", "Modulos": {}}
]
Modulos = ["Acceso a datos", "Programacion", "Interfaces", "Sistemas de gestion empresarial"]


def registrar_modulo():
    nom_modulo = input("Dime el nombre del módulo a registrar: ")
    if nom_modulo in Modulos:
        print("Este módulo ya existe")
    else:
        Modulos.append(nom_modulo)
        print(f"El módulo '{nom_modulo}' ha sido registrado correctamente")


def ver_modulos():
    for modulo in Modulos:
        print(modulo)

def eliminar_modulo():
    modulo_eliminar = input("Dime el módulo a eliminar")
    if modulo_eliminar not in Modulos:
        print(f"El módulo '{modulo_eliminar}' no existe")
    else:
        # para listas se usa remove, para diccionarios 'del'
        Modulos.remove(modulo_eliminar)
        print("Módulo eliminado")

def matricular_alumno():
    nom_alumno = input("Dime el nombre del alumno")
    apellidos_alumno = input("Ahora los apellidos")
    # si quiero iterar en un diccionario, hay que hacer un for y luego buscarlo
    # si quiere iterar sobre una lista, simplemente con poner 'if x in Alumnos' sirve
    for alumno in Alumnos:    
        if alumno["Nombre"] == nom_alumno and alumno["Apellidos"] == apellidos_alumno:
            print("Ese alumno ya existe")
            return
    nuevo_alumno = {"Nombre": nom_alumno, "Apellidos": apellidos_alumno, "Modulos": {}}


    # el codigo va incrementando
    contador = 0
    while(contador != 1):
        asig_alumno = input("Dime una asignatura")
        asig_nota = int(input("Ahora su nota"))
        
        if asig_alumno in nuevo_alumno["Modulos"]:
            print("Ese módulo ya lo está cursando")
        else:
            nuevo_alumno["Modulos"][asig_alumno] = asig_nota
            contador+=1
    Alumnos.append(nuevo_alumno)

    for alumno in Alumnos:
        print(alumno["Nombre"])

# ----- LISTAS -------
# añadir a una lista es con .append
# eliminar es remove

# ----- DICCIONARIOS -----
# añadir a un diccionario es con diccionario[clave] == valor
# eliminar es del

def eliminar_alumno():
    alumno_encontrado = False

    nom_alumno = input("Dime el nombre del alumno a eliminar")
    for alumno in Alumnos:
        if alumno["Nombre"] == nom_alumno:
            Alumnos.remove(alumno)
            print(f"El alumno {nom_alumno} ha sido eliminado")
            alumno_encontrado = True
            break
    if not alumno_encontrado:
        print("El alumno no existe")

def introducir_nota():
    nombre_alumno = input("Dime el nombre del alumno: ")
    nombre_modulo = input("Ahora el nombre del módulo: ")
    nota_modulo = input("Y finalmente la nota del módulo: ")

    for alumno in Alumnos:
        if alumno["Nombre"] == nombre_alumno:
            for modulo, nota in alumno["Modulos"].items():
                print(f"{modulo}: {nota}")
                break
        else:
            print("El alumno no existe")

def mostrar_alumnos():
    for alumno in Alumnos:
        print(alumno["Nombre"])
        for modulo, nota in alumno["Modulos"].items():
            print(f"{modulo}: {nota}")

def informacion_alumnos():
    cod_alumno = input("Dime el código del alumno")
    for alumno in Alumnos:
        if cod_alumno == alumno["Codigo"]:
            print(alumno["Nombre"])
            for modulo, nota in alumno["Modulos"].items():
                print(f"{modulo}: {nota}")

def menu():
    while True:
        print("\nMenú:")
        print("1. Registrar módulo")
        print("2. Ver módulos")
        print("3. Eliminar módulo")
        print("4. Matricular alumno")
        print("5. Eliminar alumno")
        print("6. Introducir nota")
        print("7. Mostrar alumnos")
        print("8. Información alumnos")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_modulo()
        elif opcion == '2':
            ver_modulos()
        elif opcion == '3':
            eliminar_modulo()
        elif opcion == '4':
            matricular_alumno()
        elif opcion == '5':
            eliminar_alumno()
        elif opcion == '6':
            introducir_nota()
        elif opcion == '7':
            mostrar_alumnos()
        elif opcion == '8':
            informacion_alumnos()
        elif opcion == '9':
            print("Datos guardados en memoria. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    menu()