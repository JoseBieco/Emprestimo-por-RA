from Menu.LambdaCase import *
from BD.Connection import *
from BD import *

continuar  = True

while continuar:
    menuInicial()
    op = int(input())
    if op == 0:
        continuar = False
        continue
    
    iWtD(op, conn, cursor)