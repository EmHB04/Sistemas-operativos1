num1=0
num2=0
opc=str(input("¿Qué operación deseas realizar?: \n1. Suma\n2. Resta\n3. Multiplica\n4. Divide\n5. Salir"))
num1=int(input("ingresa num1"))
num2=int(input("ingresa num2"))

def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b

if opc=="1":
    print("La suma es: ", sumar(num1,num2))
elif opc=="2":
    print("La resta es: ", restar(num1,num2))
elif opc=="3":
    print("La multiplicación es: ", multiplicar(num1,num2))
elif opc=="4":
    print("La division es: ", dividir(num1,num2))
else:
        print("Has salido del programa")

