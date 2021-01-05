import sqlite3

# Teste Switch lambda
def opcoes(op, conn, cursor):
    cases = {
        1: lambda: cadastrar(conn, cursor),
        2: lambda: listar(cursor),
    }
    cases.get(op, lambda: print("\nOpção inválida!\n"))()


def menuOpcoes():
    print("\t--- Menu ---")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")
    print(">> ", end="")

def cadastrar(conn, cursor):
    print("\t --- Cadastro ---\n")


def listar(cursor):
    print("\t --- Listar ---")

    cursor.execute("""
        SELECT 
            A.RA, A.Nome, C.Nome 
        FROM 
            Aluno AS A INNER JOIN Curso AS C
                ON A.IDCurso = C.IDCurso
        """)

    for linha in cursor.fetchall():
        print("\nRA: " + linha[0])
        print("Nome: " + linha[1])
        print("Curso: " + linha[2])
    print("\n")


# Connection
conn = sqlite3.connect("Faculdade.db")

# Defining Cursor
cursor = conn.cursor()

# Main -> Teste de Inserção no Banco

continuar = True

while continuar:
    menuOpcoes()
    op = int(input())

    if op == 0:
        continuar = False
        continue

    opcoes(op, conn, cursor)

conn.close()