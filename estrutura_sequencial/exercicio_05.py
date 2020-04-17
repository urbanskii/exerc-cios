def show_calc(n):
    """Esta função retorna a conversão de metros em centimetros

    :param n: Valor calculado na função calc
    :return: Retorna o valor da conversão de metros em centimetros
    """
    return print('Resultado da conversão de metros em centimetros:', n, 'cm')

def calc():
    """ Esta função realiza o calculo dos valores digitados.

    :return: Retorna o valor calculado para a função show_calc():
    """
    n1 = int(input('Digite a metragem: '))
    return show_calc(n1*100)

if __name__ == '__main__':
    try:
        calc()
    except:
        print('Digite apenas numeros!')