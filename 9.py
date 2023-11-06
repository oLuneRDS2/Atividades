lado= float(input("Diga o valor desse lado"))
lado1= float(input("Diga o valor desse lado"))
lado2= float(input("Diga o valor desse lado"))

if lado==lado1 and lado==lado2:
    print("Triângulo Equilátero")
elif lado==lado1  and lado!=lado2 :
    print("Triângulo Triângulo Isósceles")
elif lado==lado2  and lado!=lado1 :
    print("Triângulo Triângulo Isósceles")
elif lado1==lado2  and lado!=lado1 :
    print("Triângulo Triângulo Isósceles")
elif lado!=lado1 and lado!=lado2:
    print("Triângulo Escaleno")