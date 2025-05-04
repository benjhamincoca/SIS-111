#Verificador de numeros palidromos
numer = (input("Ingrese un numero: "))

inicio = 0
fin = len(numer) - 1
es_palindromo = True
while inicio < fin:
    if numer[inicio] != numer[fin]:
        es_palindromo = False
    inicio = inicio + 1
    fin = fin - 1
if es_palindromo:
    print("Es un palindromo")
else:
    print("no es un palindromo")

# combinaciones posibles de numeros

numers = []

for i in range(4):
    nume = int(input("ingrese un numero a la lista: "))
    numers.append(nume)

print("posibles combinacioes:")

for i in range(len(numers)):
    for j in range(i + 1, len(numers)):
        print(f"({numers[i]}, {numers[j]})")

# Verificador de número primo

number = int(input("Ingresa un número: "))
es_primo = True

if number <= 1:
    es_primo = False
else:
    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            es_primo = False
            break
        divisor += 1

if es_primo:
    print("Es primo")
else:
    print("No es primo")
    
# Suma de números pares

nume = []

# Pedimos 6 números al usuario
for i in range(6):
    num = int(input("Ingresa un número: "))
    nume.append(num)

# Sumamos solo los pares
suma_pares = 0
for n in nume:
    if n % 2 == 0:
        suma_pares += n

print("La suma de los números pares es:", suma_pares)