def calcula_idade(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade
def main():
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        idade = calcula_idade(ano_nascimento)
        if idade >= 0:
            print(f"Sua idade é: {idade} anos")
        else:
            print("Ano de nascimento inválido (ano futuro).")
    except ValueError:
        print("Por favor, digite um ano válido (número inteiro).")
if __name__ == "__main__":
    main()