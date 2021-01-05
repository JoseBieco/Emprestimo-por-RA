"""
    v -> Validation
"""

def vString(str):
    """
        Probably will be used to validate RA and Name 
    """
    return str.isspace()

def vInteger(num):
    """
         Probably will be used to validate the Semestre
    """
    return num >= 0

# TODO: Melhorar
def vAluno(nome, Ra, IdCurso):
    return vString(nome) and vString(Ra) and vInteger(IdCurso)

# TODO: Melhorar
def vCurso(nome, semestres):
    return vString(nome) and vInteger(semestres)
    