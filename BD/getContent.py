def rAluno(cursor):
    print("\t --- Lista de Alunos ---")

    cursor.execute("SELECT * FROM Aluno")

    for linha in cursor.fetchall():
        print("\nRA: " + linha[2])
        print("Nome: " + linha[1])
        print("IDCurso: ", linha[3])
    print("\n")

def rCurso(cursor):
    print("\t --- Lista de Cursos ---")

    cursor.execute("SELECT * FROM Curso")

    for linha in cursor.fetchall():
        print("\nId: " + str(linha[0]))
        print("Curso: " + linha[1])
        print("Semestres: " + str(linha[2]))
    print("\n")