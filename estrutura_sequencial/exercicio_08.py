def show_calc(n):
    """Esta função retorna o total do salario do referido mês

    :param n: Valor calculado na função calc
    :return: Retorna o valor calculo
    """
    return print('Resultado do salário no referido mês:', n)

def calc():
    """ Esta função realiza o calculo dos valores digitados.

    :return: Retorna o valor calculado para a função show_calc():
    """
    n1 = int(input('Digite quanto você ganha por hora: '))
    n2 = int(input('Digite o número de horas trabalhadas no mês: '))
    return show_calc(n1*n2)

if __name__ == '__main__':
    try:
        calc()
    except:
        print('Digite apenas numeros!')