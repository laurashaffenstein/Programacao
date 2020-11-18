import os
from models import Serie
from config import db, db_file


if __name__ == '__main__':
    if os.path.exists(db_file):
        os.remove(db_file)

    db.create_all()

    s1 = Serie(nome ='Avatar: A lenda de Aang',
                genero ='fantasia',
                numtemps ='3',
                nota ='10')
    s2 = Serie(nome ='Stranger Things',
                genero ='ficção cientifica',
                numtemps ='3',
                nota ='10')
    s3 = Serie(nome ='Brooklyn Nine-nine',
                genero ='comedia',
                numtemps ='6',
                nota ='10')
    s4 = Serie(nome ='Black Mirror',
                genero ='ficção cientifica',
                numtemps ='5',
                nota ='10')
    s5 = Serie(nome ='Teen Wolf',
                genero ='Teen',
                numtemps ='6',
                nota ='8')
    
    db.session.add(s1)
    db.session.add(s2)
    db.session.commit()
    
    print(s1)
    print(s2)
    print(s2.json())
    