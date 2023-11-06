n1=float(input("Digite sua primera nota"))
n2=float(input("Digite sua sengunda nota"))

m=(n1+n2)/2
if m>=7 and m<10:
    print("Aprovado")
elif m==10:
    print("Aprovado com Distinção",)
else:
    print("reprovado")