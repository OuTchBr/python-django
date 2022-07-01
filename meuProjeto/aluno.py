class Aluno:
    def __init__(self, aMatricula, aNome, aCurso):
        self.matricula = aMatricula
        self.nome = aNome
        self.curso = aCurso
        self.pontuacao = 0

    def __str__(self):
        return f'\nMatrícula: {self.matricula}\nNome: {self.matricula}\nCurso: {self.curso}\nPontuação: {self.pontuacao}\n'

    def adicionaPonto(self, pontos):
        self.pontuacao += pontos


aluno1 = Aluno("linf123", "Pedro", "Informática")
aluno2 = Aluno("tsan456", "Lara", "Saneamento")
aluno1.adicionaPonto(1)

print(aluno1)
print(aluno2)

# criar atributo pontos e método adicionarPonto()
