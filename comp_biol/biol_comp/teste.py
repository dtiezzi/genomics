def calculadora():
    operation= input(''' Por favor digite a operação matemática que você gostaria de completar
    + para adição
    - para subtração
    * para multiplicação
    / para divisão
    ''')
    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite outro número: "))
    if operation == '+':
        print('{} + {} = '.format(num_1, num_2))
        print(num_1 + num_2)
    elif operation == '-':
        print('{} - {} = '.format(num_1, num_2))
        print(num_1 - num_2)
    elif operation == '*':
        print('{} * {} = '.format(num_1, num_2))
        print(num_1 * num_2)
    elif operation == '/':
        print('{} / {} = '.format(num_1, num_2))
        print(num_1 / num_2)
    else:
        print('Você digitou um operador inválido, por favor, tente novamente')

calculadora()