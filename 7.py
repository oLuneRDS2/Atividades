n1 = float(input("Digite o primeiro numero"))
n2 = float(input("Digite o segundo numero"))
n3 = float(input("Digite o terceiro numero"))

if n1>n2 and n1>n3:
    print("Maior: ", n1)
elif n2>n1 and n2>n3:
    print("Maior: ", n2)
elif n3>n1 and n3>n1:
    print("Maior: ", n3)
else:
    print("")