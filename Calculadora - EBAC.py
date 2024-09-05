# Calculadora Simples
print("Olá, Digite o Índice da operação que deseja realizar: ")
interface = int(input("[1 - Soma]  [2 - Subtração]  [3 - Multiplicação]  [4 - Divisão]  [5 - Outras operações]\nÍndice: "))

##### OUTRAS OPERAÇÕES ######
if interface == 5:
    print("Olá, Digite o Índice da operação que deseja realizar: ")
    interface2 = int(input("[1 - Exponenciação]  [2 - Divisão inteira]  [3 - Resto]\nÍndice: "))
    valor_a = int(input("Por favor, informe o primeiro valor: "))
    valor_b = int(input("Por favor, informe o segundo valor: "))

    if interface2 == 1:
        print("O resultado é:", valor_a ** valor_b)
    elif interface2 == 2:
        print("O resultado é:", valor_a // valor_b)
    elif interface2 == 3:
        print("O resultado é:", valor_a % valor_b)
    else:
        print("Operação inválida.")

##### INTERFACE PRINCIPAL ######
else:
    def principal(interface):
        valor_um = int(input("Por favor, informe o primeiro valor: "))
        valor_dois = int(input("Por favor, informe o segundo valor: "))

        if interface == 1:
            print("O resultado é:", valor_um + valor_dois)
        elif interface == 2:
            print("O resultado é:", valor_um - valor_dois)
        elif interface == 3:
            print("O resultado é:", valor_um * valor_dois)
        elif interface == 4:
            if valor_dois != 0:  # Verifica para evitar divisão por zero
                print("O resultado é:", valor_um / valor_dois)
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Operação inválida.")

    principal(interface)