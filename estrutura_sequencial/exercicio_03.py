def show_soma(n):
    """Esta função retorna a soma dos numeros digitados

    :param n: Valor somado na função soma
    :return: Retorna o valor somado
    """
    return print('Resultado da soma dos numeros digitados:', n)

def soma():
    """ Esta função realiza a soma dos valores digitados.

    :return: Retorna o valor somado para a função show_soma():
    """
    n1 = int(input('Digite o primeiro numero:'))
    n2 = int(input('Digite o segundo numero:'))
    return show_soma(n1+n2)

if __name__ == '__main__':
    try:
        soma()
    except:
        print('Digite apenas numeros!')