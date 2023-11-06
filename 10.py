combustivel= (input("digite o que voce quer gasolina ou alcool"))
while combustivel =="acool":
    quantidade = int(input("Digite o quanto voce que de litro de acool"))
    if quantidade ==20:
        c=3/100
        c1=(2.50*quantidade)-c
        print("preço: {}".format(c1))
    elif quantidade >20:
        c=5/100
        c1=(2.50*quantidade)-c
        print("Preço: {}" .format(c1))
    break

#Gasolina: até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6%por litro

while combustivel =="gasolina":
    quantidade = int(input("Digite a quanto você que de litro de Gasolina"))
    if quantidade==20:
        c=4/100
        c1=(1.90*quantidade)-c
        print("Preço: {}" .format(c1))
    elif quantidade>20:
        c=6/100
        c1=(1.90*quantidade)-c
        print("Preço: {}" . format(c1))
    break