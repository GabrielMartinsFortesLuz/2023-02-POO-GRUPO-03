class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def inscrever_curso(self, curso):
        print(f"{self.nome} se inscreveu no curso de {curso.titulo}")

    def __str__(self):
        return f"{self.nome} ({self.email})"