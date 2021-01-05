def cAluno(conn, cursor):

    data = getAlunoContent()
    # TODO: Validar Dados
    
    cursor.execute("""
        INSERT INTO Aluno
        VALUES
            (NULL,?,?,?)
    """, data)

def cCurso(conn, cursor):
    print("TODO")


def getAlunoContent():
    infoList = []

    print("\t-- Cadastro de Aluno --")

    print("Nome: ", end="")
    nome = input()

    print("Ra: ", end="")
    ra = input()

    print("IdCurso: ", end="")
    idCurso = int(input())


    infoList.append(nome)
    infoList.append(ra)
    infoList.append(idCurso)

    return infoList