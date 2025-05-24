# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    nascimento = db.Column(db.String(255), nullable=False)
