nome = input("Digite seu nome: ")

print(f"Olá, usuário {nome} Bem-vindo ao nosso sistema de gestão financeira.")
print("Aqui, realizaremos diversos cálculos, como fluxo de caixa e outras operações financeiras para ajudar no seu controle.")


print("""
Digite o número referente à operação que deseja realizar:

1 - Fluxo de caixa
2 - Outra operação
3 - Outra operação
4 - Outra operação
""")


try:
    num1 = int(input("Escolha uma opção: "))

    if num1 == 1:
        print("Você escolheu Fluxo de Caixa.")
        print("""
Agora, escolha entre entrada e saida:

1 - Entrada
2 - Saída
""")
        
    elif num1 == 2:
        print(".")
       
    elif num1 == 3:
        print(".")
      
    elif num1 == 4:
        print(".")
        
    else:
        print("Opção inválida. Tente novamente.")
except ValueError:
    print("Erro: Digite um número válido.")
