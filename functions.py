import sqlite3
from flask import Flask, redirect, render_template, request, flash



#cria tabela caso nao exista
def cria_tabela() :
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contas ([nome] TEXT NOT NULL,[dre] TEXT PRIMARY KEY,[senha] TEXT NOT NULL);
    ''')

    db.commit()

class aluno():
    def __init__(self, nome, dre, senha):
        self.nome = nome
        self.dre = dre
        self.senha = senha



def checa_existe(dre) :
        db = sqlite3.connect('database.sqlite')
        cursor = db.cursor()
        cadastro = cursor.execute("SELECT * FROM contas where dre = '"+dre+"'").fetchall()
        if len(cadastro)>0 :
                return True
        else:
                
                return False       

#checa se ja existe e se nao existir ele cria
def cadastrar(nome, dre, senha):
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()
    if checa_existe(dre) == False:
        cursor.execute("INSERT INTO contas VALUES ('"+nome+"','"+dre+"','"+senha+"')")
        db.commit()
        flash("Cadastro efetuado com sucesso!")
        return redirect("/")
    else:
        flash("Erro! DRE já cadastrado!")
        return render_template("cadastro.html") 



def autentica_dre(dre):
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()
    acha_dre = cursor.execute("SELECT * FROM contas where dre = '"+dre+"'").fetchall()
    if len(acha_dre) >0:
        return True
    else:
        return False

def autentica_senha(senha):
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()
    acha_senha = cursor.execute("SELECT * FROM contas where senha = '"+senha+"'").fetchall()
    if len(acha_senha) >0:
        return True
    else:
        return False

def autentica_tudo(dre,senha):
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()
    acha_coisa = cursor.execute("SELECT * FROM contas where senha = '"+senha+"'").fetchall()
    if len(acha_coisa) >0:
        senha_valida = True
    acha_coisa = cursor.execute("SELECT * FROM contas where dre = '"+dre+"'").fetchall()
    if len(acha_coisa)>0:
        dre_valido = True
    if dre_valido == True and senha_valida == True:
        return True
    else:
        return False

def autenticado():
    global logado 
    logado = True


def login(dre,senha):
    db = sqlite3.connect('database.sqlite')
    cursor = db.cursor()
    if autentica_tudo(dre, senha) == True :
        global logado
        logado = True
        return redirect("/home"), logado
    elif autentica_dre(dre) == True and autentica_senha(senha) == False:
        flash("Senha errada!")
        return redirect("/login"), None
    elif autentica_dre(dre) == False and autentica_senha(senha) == True:
        flash("DRE errado")
        return redirect("/login"), None
    else:
        flash("DRE não cadastrado, por favor cadastre-se!")
        return redirect("/login"), None


global user 
user = aluno("","","")



