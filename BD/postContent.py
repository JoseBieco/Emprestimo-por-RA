from Validate import Validators

def cAluno(conn, cursor):

    data = getAlunoContent()
    # TODO: Validar Dados
    
    if not Validators.vAluno(data[0], data[1], data[2]):
        print("--- ERRO ---\n Valores inválidos!!!")
        return

    cursor.execute("""
        INSERT INTO Aluno
        VALUES
            (NULL,?,?,?)
    """, data)


def cCurso(conn, cursor):
    data = getCursoContent()
    # TODO: Validar Dados

    if not Validators.vCurso(data[0], data[1]):
        print("--- ERRO ---\n Valores inválidos!!!")
        return
        
    cursor.execute(""" 
        INSERT INTO Curso
        VALUES
            (NULL,?,?)
    """, data)


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


def getCursoContent():
    infoList = []

    print("\t-- Cadastro de Curso --")

    print("Curso: ", end="")
    nome = input()

    print("Semestres: ", end="")
    semestres = int(input())

    infoList.append(nome)
    infoList.append(semestres)

    return infoList