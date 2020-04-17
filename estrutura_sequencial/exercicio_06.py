def show_calc(n):
    """Esta função retorna a area de um circulo

    :param n: Valor calculado na função calc
    :return: Retorna o valor calculo
    """
    return print('Resultado da area de um circulo:', n)

def calc():
    """ Esta função realiza o calculo dos valores digitados.

    :return: Retorna o valor calculado para a função show_calc():
    """
    n1 = int(input('Digite o raio de um circulo: '))
    return show_calc((n1**2)*3.14159)

if __name__ == '__main__':
    try:
        calc()
    except:
        print('Digite apenas numeros!')