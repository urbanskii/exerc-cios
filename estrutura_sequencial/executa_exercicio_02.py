from estrutura_sequencial.exercicio_02 import show_numero as sh

try:
    print(sh(int(input('Digite um numero: '))))
except:
    print('Digite apenas numeros!')