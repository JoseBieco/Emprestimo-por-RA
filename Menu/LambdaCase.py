
# TODO: Criar e importar .py com as funcoes de cadastro e listar
from BD.getContent import *


"""
    WTD -> What to DO
    i -> menu Inicial
    c -> menu de Cadastros
    r -> menu de Registros
"""

# Menu Inicial
def iWtD(op, conn, cursor):
    cases = {
        1: lambda: cadastrar(conn, cursor),
        2: lambda: listar(cursor),
    }
    cases.get(op, lambda: print("\nOpção inválida!\n"))()


# Menu de Cadastros
def cWTD(op, conn, cursor):
    cases = {
        1: lambda: cAluno(conn, cursor),
        2: lambda: cCurso(conn, cursor),
    }
    cases.get(op, lambda: print("\nOpção inválida!\n"))()


# Menu de Registros
def rWTD(op, cursor):
    cases = {
        1: lambda: rAluno(cursor),
        2: lambda: rCurso(cursor),
    }
    cases.get(op, lambda: print("\nOpção inválida!\n"))()