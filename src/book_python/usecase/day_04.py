"""

13 | P a g e
Day 4: Only Floats

Write a function called only_floats, which takes two
parameters a and b, and returns 2 if both arguments are floats,
returns 1 if only one argument is a float, and returns 0 if neither
argument is a float. If you pass (12.1, 23) as an argument, your
function should return a 1.

"""

# Escrever uma função chamada: only_floats
# A função recebe dois paramentros(a,b)
# Retorne 2 se ambos os paramentros forem float
# Retorne 1 se apenas um argumento for float
# Retorne 0 se nenhum dos argumento for float
# Exemplo: (12.1,13) retorno será 1

# Algoritimo


def only_floats(a,b):
    list=[]
    if type(a) == float:
        list.append(a)
    if type(b) == float:
        list.append(b)
    print( f" A quantidade de argumentos float é: {0 if len(list) == 0 else len(list)}"             )
    return 0 if len(list) == 0 else len(list)
 


"""
Extra Challenge: Index of the Longest Word

Write a function called word_index that takes one argument,
a list of strings and returns the index of the longest word in the
list. If there is no longest word (if all the strings are of the same
length), the function should return zero (0). For example, the list
below should return 2.
words1 = ["Hate", "remorse", "vengeance"]
And this list below, shoul return zero (0)
words2 = ["Love", "Hate"]
"""

"""
Escreva uma função chamada word_index que receba um argumento,
uma lista de strings e retorna o índice da palavra mais longa na
lista.
Se não houver palavra mais longa (se todas as strings forem do mesmo
length),
a função deve retornar zero (0).

Por exemplo, a lista
abaixo deve retornar 2.
palavras1 = ["ódio", "remorso", "vingança"]
E esta lista abaixo, deve retornar zero (0)
palavras2 = ["Amor", "Ódio"]
"""

def word_index(list):
    index_start = "0"
    mesmo_length = []
    index_palavra_longa = [] 
    for name in words1:
        if len(name) > len(index_start):
            index_palavra_longa = name
            index_start = name
        else:
            if len(name)==len(index_start):
                mesmo_length.append(name)

    if len(mesmo_length) > len(index_palavra_longa):
          print(0)

    return 

#words1 = ["Hate", "remorse", "vengeance","deudneidni", "Testandoomedidor destring"]
words1 = ["Hate", "remor", "venge","deudn", "Testa","todo"]
word_index(words1)