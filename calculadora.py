# criando as funções das operações matemáticas da calculadora
def soma(a,b):
    return a + b
def subtracao(a,b):
    return a - b
def multiplicacao(a,b):
    return a * b
def divisao(a,b):
    if b == 0:
        return "ERRO!"
    return a / b
def potencia(a,b):
    if b == 0:
        return "ERRO!"
    return a ** b

# criando o loop de repetição contendo a escolha de qual operação escolher
# se caso escolher a opção 5 de sair, o loop se encerra e a aplicação será finalizada
def calculadora():
    while True:
        print("Escolha a opção")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potência")
        print("6. Sair")

        opcao = input("Digite o número da operação desejada:")
        if opcao == '6':
            print("Desligando...")
            break
# criando as variáveis de inclusão dos valores que você quer para fazer as operações matemáticas
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))
        if opcao == '1':
            print(f"Resultado: {soma(num1, num2)}")
        elif opcao == '2':
            print(f"Resultado: {subtracao(num1, num2)}")
        elif opcao == '3':
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif opcao == '4':
            print(f"Resultado {divisao(num1, num2)}")
        elif opcao == '5':
            print(f"Resultado {potencia(num1, num2)}")
        else:
            print("Opção não encontrada")
        print("____________________________________________")
#chamando a função para rodar a aplicação, no caso a calculadora
calculadora()