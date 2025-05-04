# digitos pares e impares de numero
numero = int(input("Ingrese el numero: "))
num_par = 0
num_impar = 0
while numero > 0:
    digito = numero % 10
    if digito % 2 == 0:
        num_par += 1
    else:
        num_impar += 1
    numero = numero // 10    
print("Pares: ", num_par)
print("Impares: ", num_impar)

# Promedio de dos equipos

equipo_A = []
equipo_B = []

for i in range(5):
    resultado_A = int(input("Ingrese un resultado del equipo A: "))
    equipo_A.append(resultado_A)
for i in range(5):
    resultado_B = int(input("Ingrese un resultado del equipo B: "))
    equipo_B.append(resultado_B)
# promedio de ambos equipos
promedio_A = sum(equipo_A)/5
promedio_B = sum(equipo_B)/5

if promedio_A > promedio_B:
    print("Equipo A tuvo mayor rendimiento: ", promedio_A)
elif promedio_A == promedio_B:
    print("Ambos equipos tuvieron el mismo rendimiento")
else:
    print("Equipo B tuvo mayor rendimiento: ", promedio_B) 

# Mayor producto entre dos numeros

numeros = []

for i in range(4):
    num = int(input("Ingrese numeros a la lista: "))
    numeros.append(num)
producto = numeros[0]*numeros[1]
producto_mayor = 0
for i in range(4):
    for j in range(i + 1, 4):
        producto = numeros[i]*numeros[j]
if producto > producto_mayor:
    producto_mayor = producto
print("el producto mayor es:",producto_mayor)

# Meta de ahorros
meta = int(input("¿Cual es su meta de ahorro?  "))
ingreso_diario = float(input("¿Cuanto dinero desea ingresar hoy?  "))
incremento = int(input("¿Cuanto incrementara su ahorro diario?  "))

Total_ahorro = 0
contador_dias = 0
while Total_ahorro < meta:
    Total_ahorro = Total_ahorro + ingreso_diario
    ingreso_diario = ingreso_diario + incremento
    contador_dias = contador_dias + 1 
print("Se estima un tiempo de: ", contador_dias, "dias." )

#Verificador de numeros palidromos
numer = int(input("Ingrese un numero: "))

inicio = 0
fin = len(numero)-1

while numer < fin:
    if numer ==  fin:
        print("palindromo")
    else:
        print("no es palindromo")
