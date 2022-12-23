import math

"""
'''TODO'''

f"Dia 1: Divisão e Raiz Quadrada

f"- Escreva uma função chamada divide_or_square que leva um
argumento (um número).

f"- retorna a raiz quadrada do número
se for divisível por 5, retorna seu resto se não for divisível por
5. 

f"-Por exemplo, se você passar 10 como argumento, sua função
deve retornar 3,16 como a raiz quadrada."
'''
"""


def divide_or_square(num):
    #num = float(input("enter a number:\n"))
    if float(num) % 5 == 0:
        source = math.sqrt(num)
        return (f'\nThe square root of {num} it is {source}\n')
    else:
        rest = float(num) % 5
        return (f"\n the rest of the number: {num} it is {rest}")


divide_or_square(9)


'''TODO
Desafio extra: valor mais longo
Escreva uma função chamada valor_longo que usa um dicionário
como um argumento e retorna o primeiro valor mais longo do
dicionário. Por exemplo, o seguinte dicionário deve retornar
– maçã como o valor mais longo.
frutas = {'fruta': 'maçã', 'cor': 'verde'}
'''
frutas = {'fruta': 'maçã',
          'cor': 'verde'}


def long_value():
    if len(frutas['cor']) > len(frutas['fruta']):
        print(frutas['cor'])
    else:
        print(frutas['fruta'])


long_value()
