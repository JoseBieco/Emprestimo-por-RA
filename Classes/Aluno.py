# from Classes import Curso

class Aluno:
    def __init__(self) -> None:
        super().__init__()


    def __init__(self, Id, nome, Ra, IdCurso):
        self.Id = Id
        self.nome = nome
        self.Ra = Ra
        self.IdCurso = IdCurso
        # self.Curso = Curso(Curso.Id, Curso.nome, Curso.semestres)

    # Getters and Setters
    def setNome(self, nome):
        self.nome = nome
    
    def setRa(self, Ra):
        self.Ra = Ra

    def setIdCurso(self, IdCurso):
        self.IdCurso = IdCurso
    

    def getId(self):
        return self.Id

    def getNome(self):
        return self.nome
    
    def getRa(self):
        return self.Ra
    
    def getIdCurso(self):
        return self.IdCurso