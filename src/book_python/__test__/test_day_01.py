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
        # return (f'\nThe square root of {num} it is {source}\n')
        return source
    else:
        rest = float(num) % 5
        # return (f"\n the rest of the number: {num} it is {rest}")
        return rest

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

def long_value(frutas): 
    frutas = frutas;
    frut = frutas['fruta']
    cor = frutas['cor']
    long_value = frut if len(frut) > len(cor) else cor
    print(long_value)


long_value(frutas)

def iter_long_value():
    pecas = {'portas': 9,'janelas': 2, 'motor': 3,'pneus': 10}
    #será necessario converte o dicionário em lista/vetor/array?
    for key, value in pecas.items():
        item_anterior = pecas['portas']
        if value > item_anterior:
            print(f"Value: {value} é maior que item_anterior {item_anterior}")
            break
        item_anterior = value
        print(item_anterior)
     
iter_long_value()

# test to return source the number
def test_divide_or_square_source():
    num = 10
    source = math.sqrt(num)
    assert divide_or_square(num) == source


# test to return rest the number
def test_divide_or_rest():
    num = 9
    rest = float(num) % 5
    assert divide_or_square(num) == rest

    
