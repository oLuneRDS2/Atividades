n1 = float(input("Digite sua primeira nota parcial: "))
n2 = float(input("Digite sua segunda nota parcial: "))
media = (n1+n2) /2
tabela = media
if media >= 9:
    tabela = "A"
elif media >= 7.5 and  media < 9:
    tabela = "B"
elif media > 6.0 and  media < 7.5:
    tabela = "C"
elif media > 4 and  media < 6:
    tabela = "D"
else:
    tabela = "E"

print(" sua media:", media,"\n Média de Aproveitamento conceito:")