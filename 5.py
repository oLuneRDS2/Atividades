a = float(input("digite quantas horas você trabalha por mes"))
b = float(input("digie quanto você recebe por hora"))
c = b*a

imposto = c*(11/100)
INSS = c*(8/100)
Sindicato = c*(5/100)
resto = imposto + INSS + Sindicato
salarioLiq = c-resto

print(" Salario Bruto:", c)
print("Imposto de renda:", imposto)
print("INSS:", INSS)
print("sindicato:", Sindicato)
print(" slario liquido:", salarioLiq)