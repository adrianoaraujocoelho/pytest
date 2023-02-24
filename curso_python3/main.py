
from math import pi
from help import helps
import sys
import errno

class TerminalColor:    
    ERRO = ' \033 [31m '
    NORMAL = '\033[0m' 

def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == '__main__':
    if len(sys.argv) < 2:
        helps()
        sys.exit(errno.EPERM)
    if not sys.argv[1].isnumeric():
        helps()
        print(TerminalColor.ERRO +'O raio deve ser um valor número' + TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print(f"Área do circulo, {area:.2f}")
        print(dir)    



