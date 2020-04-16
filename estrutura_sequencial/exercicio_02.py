def show_numero(n):
    return print(n)

if __name__ == '__main__':
    try:
        print(show_numero(int(input('Digite um numero: '))))
    except:
        print('Digite apenas numeros!')