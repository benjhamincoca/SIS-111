# ejercicio 1 verficacion de orden
num1 = int(input("ingrese primer numero: "))
num2 = int(input("ingrese segundo numero: "))
num3 = int(input("ingrese tercer numero: "))
num4 = int(input("ingrese cuarto numero: "))
num5 = int(input("ingrese quinto numero: "))
if num1 < num2 < num3 < num4 < num5:
    print("ascendente")
elif num1 > num2 > num3 > num4 > num5:
    print("descendente")
else:
    print("ingrese numeros de manera ascendente o descendente")

#ejercicio 2
numeros = []

cantidad = int(input("¿Cuántos números quieres ingresar? "))

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)
buscado = int(input("¿Qué número quieres buscar? "))
encontrado = False
for numero in numeros:
    if numero == buscado:
        encontrado = True
        break
if encontrado:
    print(" Número encontrado")
else:
    print(" Número no encontrado")