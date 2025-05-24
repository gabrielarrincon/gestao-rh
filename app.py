# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import db, Funcionario
from security import encrypt_data
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
Bootstrap(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    funcionarios = Funcionario.query.all()
    return render_template("index.html", funcionarios=funcionarios)

@app.route('/add', methods=['GET', 'POST'])
def add_funcionario():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = encrypt_data(request.form['cpf'])
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = encrypt_data(request.form['endereco'])
        nascimento = encrypt_data(request.form['nascimento'])

        novo = Funcionario(nome=nome, cpf=cpf, email=email,
                           telefone=telefone, endereco=endereco,
                           nascimento=nascimento)
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("form.html")
