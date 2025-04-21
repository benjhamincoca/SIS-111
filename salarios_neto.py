def calcular_salario_neto()
# 1. Ingresar salarion bruto y porcentajes
salario_bruto = float(input("ingrese el salario bruto: "))
# impuesto al valor agregado
iva_porcentaje = 13 
# impuesto a la transferencia
it_porcentaje = 3

# 2. calcular deducciones
deduccion_iva = (salario_bruto * (iva_porcentaje/ 100))
deduccion_it = (salario_bruto * (it_porcentaje / 100))
deducciones = deduccion_iva + deduccion_it

# 3. Restar las deducciones al salario bruto
calcular_salario_neto = salario_bruto - deducciones

# 4. Mostrar salario
print(f"salario Bruto: {salario_bruto}")
print(f"toral deducciones (IVA): {deduccion_iva}")
print(f"total deducciones (IT): {deduccion_it}")
print(f"salario (IVA+IT): {deducciones}")