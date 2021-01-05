from BD.getContent import *
from BD.postContent import *


def menuInicial():
    print("\t--- Menu ---")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")
    print(">> ", end="")


def menuCadastro(conn, cursor):
    print("\t--- Menu de Cadastros ---")
    print("1 - Aluno")
    print("2 - Curso")
    print("0 - Sair")
    print(">> ", end="")
    
    op = int(input())
    if op == 0:
        return
    cWtd(op, conn, cursor)
    
    
def menuRegistros(cursor):
    print("\t--- Menu de Registros ---")
    print("1 - Aluno")
    print("2 - Curso")
    # print("3 - Emprestimos")
    print("0 - Sair")
    print(">> ", end="")

    op = int(input())
    if op == 0:
        return
    rWtd(op, cursor)


"""
    WTD -> What to DO
    i -> menu Inicial
    c -> menu de Cadastros
    r -> menu de Registros
"""


# Menu Inicial
def iWtD(op, conn, cursor):
    cases = {
        1: lambda: menuCadastro(conn, cursor),
        2: lambda: menuRegistros(cursor),
    }
    cases.get(op, lambda: print("\nOpção inválida!\n"))()


# Menu de Cadastros
def cWtd(op, conn, cursor):
    cases = {
        1: lambda: cAluno(conn, cursor),
        2: lambda: cCurso(conn, cursor),
    }
    cases.get(op, lambda: print("\nOpção inválida!\n"))()


# Menu de Registros
def rWtd(op, cursor):
    cases = {
        1: lambda: rAluno(cursor),
        2: lambda: rCurso(cursor),
    }
    cases.get(op, lambda: print("\nOpção inválida!\n"))()