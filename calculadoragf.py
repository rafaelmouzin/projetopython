nome = input("Digite seu nome: ")

print(f"Olá, usuário {nome}. Bem-vindo ao nosso sistema de gestão financeira.")
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
Agora, escolha entre entrada e saída:

1 - Entrada
2 - Saída
""")
        
        entradas = []
        saidas = []

        while True:
            valor = input("Digite uma entrada (ou 'sair' para parar): ")
            if valor.lower() == 'sair':
                break
            try:
                entradas.append(float(valor))
            except ValueError:
                print("Valor inválido. Digite um número válido.")

        
        while True:
            valor = input("Digite uma saída (ou 'sair' para parar): ")
            if valor.lower() == 'sair':
                break
            try:
                saidas.append(float(valor))
            except ValueError:
                print("Valor inválido. Digite um número válido.")

        total_entradas = sum(entradas)
        total_saidas = sum(saidas)
        saldo = total_entradas - total_saidas

        print("\n===== Fluxo de Caixa =====")
        print(f"Entradas: R$ {total_entradas:.2f}")
        print(f"Saídas: R$ {total_saidas:.2f}")
        print(f"Saldo Final: R$ {saldo:.2f}")
    
    elif num1 == 2:
        print("Operação 2 em desenvolvimento...")
       
    elif num1 == 3:
        print("Operação 3 em desenvolvimento...")
      
    elif num1 == 4:
        print("Operação 4 em desenvolvimento...")
        
    else:
        print("Opção inválida. Tente novamente.")
except ValueError:
    print("Erro: Digite um número válido.")
