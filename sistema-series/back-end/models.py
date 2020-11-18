from config import *


class Diretor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    idade = db.Column(db.Integer)
    formacao = db.Column(db.String(254))

    serie = db.relationship("Serie", back_populates="diretor")


    def __str__(self):
        return f'''id: {self.id}; nome: {self.nome}; idade: {self.idade}; formacao: {self.formacao}'''


    def json(self):
        return ({
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "formacao": self.formacao
        })


class Artista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    idade = db.Column(db.Integer)
    atuacao = db.Column(db.String(254))

    serie = db.relationship("Serie", back_populates="artista")


    def __str__(self):
        return f'''id: {self.id}; nome: {self.nome}; idade: {self.idade}; atuacao: {self.atuacao}'''


    def json(self):
        return ({
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "atuacao": self.atuacao
        })


class Serie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    genero = db.Column(db.String(254))
    numtemps = db.Column(db.Integer)
    nota = db.Column(db.Integer)

    artista_id = db.Column(db.Integer, db.ForeignKey(Artista.id), nullable=False)
    artista = db.relationship("Artista", back_populates="serie")

    diretor_id = db.Column(db.Integer, db.ForeignKey(Diretor.id), nullable=False)
    diretor = db.relationship("Diretor", back_populates="serie")


    def __str__(self):
        return f"id: {self.id}; nome: {self.nome}; genero: {self.genero}; " +\
               f"numtemps: {self.numtemps}; nota: {self.nota}\n" +\
               f"Artista_id: {self.artista_id}; Artista: {self.artista}\n" +\
               f"Diretor_id: {self.diretor_id}; Diretor: {self.diretor}"


    def json(self):
        return ({
            "id": self.id,
            "nome": self.nome,
            "genero": self.genero,
            "numtemps": self.numtemps,
            "nota": self.nota,
            "artista_id": self.artista_id,
            "artista": self.artista,
            "diretor_id": self.diretor_id,
            "diretor": self.diretor
        })


if __name__ == "__main__":
    if os.path.exists(db_file):
        os.remove(db_file)

    db.create_all()

    d1 = Diretor(nome="Tarantula", idade=75, formacao="Fotografia")
    db.session.add(d1)

    a1 = Artista(nome="Jhon", idade=17, atuacao="Coadjuvante")
    db.session.add(a1)

    s1 = Serie(nome="Teen Wolf", genero="Ficção Cientifica", numtemps=6, nota=0,
               artista=a1, diretor=d1)
    db.session.add(s1)

    db.session.commit()

    print(f"Diretor: {d1} \nEm JSON: {d1.json()}\n")
    print(f"Artista: {a1} \nEm JSON: {a1.json()}\n")
    print(f"Serie: {s1} \nEm JSON: {s1.json()}")