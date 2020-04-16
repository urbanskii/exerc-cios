def show_media(n):
    """Esta função retorna a media das notas digitadas

    :param n: Valor calculado na função calc
    :return: Retorna o valor da media das notas
    """
    return print('Resultado da media das notas digitadas:', n)

def calc():
    """ Esta função realiza o calculo dos valores digitados.

    :return: Retorna o valor calculado para a função show_media():
    """
    n1 = int(input('Digite a primeira nota:'))
    n2 = int(input('Digite a segunda nota:'))
    n3 = int(input('Digite a terceira nota:'))
    n4 = int(input('Digite a quarta nota:'))
    return show_media((n1+n2+n3+n4)/4)

if __name__ == '__main__':
    try:
        calc()
    except:
        print('Digite apenas numeros!')