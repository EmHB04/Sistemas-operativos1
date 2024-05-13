#Autor: Emanuel Herrera Briseño
import subprocess

def ejecutar(comando):
    subprocess.run(comando, shell=True)

while True:
    print("PROYECTO COMANDOS BASICOS")
    print("1. Crear un archivo llamado misnotas.txt")
    print("2. Crear una carpeta llamada calificaciones")
    print("3. Crear una carpeta llamada primer parcial dentro de la carpeta calificaciones")
    print("4. Mover el archivo misnotas.txt a la carpeta calificaciones")
    print("5. Mover el programa calculadora.py a la carpeta primer parcial")
    print("6. Salir")

    opc = input("Elige una opción DE 1 a 6: ")

    if opc == "1":
        ejecutar("touch misnotas.txt")
        print("Archivo misnotas.txt se ha creado")
    elif opc == "2":
        ejecutar("mkdir calificaciones")
        print("Carpeta calificaciones cse ha creado")
    elif opc == "3":
        ejecutar("mkdir calificaciones/primer\ parcial")
        print("Carpeta primer parcial se ha puesto dentro de calificaciones.")
    elif opc == "4":
        ejecutar("mv misnotas.txt calificaciones/")
        print("Archivo misnotas.txt se ha movido a la carpeta calificaciones.")
    elif opc == "5":
        ejecutar("mv calculadora.py calificaciones/primer\ parcial/")
        print("Programa calculadora.py seha movido a la carpeta primer parcial dentro de calificaciones.")
    elif opc == "6":
        print("Has salido")
    else:
        print("OpciOn no valida, elige unA opciOn del 1 al 6.")


