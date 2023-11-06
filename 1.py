nacimento=int(input("Digite seu nacimento"))

idade=2023-nacimento
if idade<=11:
    print("criança")
elif idade <=18:
    print("adolescente")
elif idade<=24:
    print("Jovem")
elif idade <=40:
    print("Adulto")
elif idade <=60:
    print("Meia idade")
elif idade >60:
    print("Idoso")
print("Idade: {}" .format(idade))