#A partir dos valores da base e altura de um triângulo, calcular e exibir sua área.

base = float(input("Digite o valor da base do triangulo: "))
altura = float(input("Digite o valor da altura do triangulo: "))

area = (base*altura)/2
 
print(f"A area deste triangulo e {area:.2f}")