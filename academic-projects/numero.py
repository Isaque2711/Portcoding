valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))
maior = valor1 
if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3
print(f"O maior valor é: {maior}")