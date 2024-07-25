def adicionar(x, y):
    return x + y
def subtrair(x, y):
    return x - y
def multiplicar(x, y):
    return x * y
def dividir(x, y):
    if y == 0:
        return "Não se pode dividir por 0"
    return x / y

while True:
    print("\nEscolha um número:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Escolha uma das operações: ")
    if escolha == '5':
        print("Saindo...")
        break
    elif escolha >= '6':
        print("Opção Invalida")
        break

    num1 = float(input("Escolha o Número1: "))
    num2 = float(input("Escolha o Número2: "))

    if escolha == '1':
        print(f"Resultado: {adicionar(num1, num2)}")
    elif escolha == '2':
        print(f"Resultado: {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"Resultado: {dividir(num1, num2)}")
    else:
        print("Operação invalida")

    continuar = input("Deseja fazer outra operação? (s/n): ")
    if continuar.lower() != 's':
        print("Saindo...")
        break