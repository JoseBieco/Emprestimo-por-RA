class Curso:
    def __init__(self) -> None:
        super().__init__()

    def __init__(self, Id, nome, semestres):
        self.Id = Id
        self.nome = nome
        self.semestres = semestres

    # Getters and Setters
    def setId(self, Id):
        self.Id = Id

    def setNome(self, nome):
        self.nome = nome

    def setSemestres(self, semestres):
        self.semestres = semestres


    def getId(self):
        return self.Id

    def getNome(self):
        return self.nome
    
    def getSemestres(self):
        return self.semestres
