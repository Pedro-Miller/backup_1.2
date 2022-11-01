import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from functions import cria_tabela, login, cadastrar

cria_tabela()

calendario = Flask(__name__)
calendario.secret_key = "abc"  
logado = False






@calendario.route("/")
def rota_root():
    return render_template("base.html")


@calendario.route("/cadastro")
def rota_cadastro():
    return render_template("cadastro.html")

@calendario.route("/cadastro", methods =["POST"])
def cadastrando():
    if request.method == "POST":
        n = request.form["nome"]
        d = request.form["dre"]
        s = request.form["senha"]
        return cadastrar(n, d, s)
    
@calendario.route("/login")
def rota_login():
    return render_template("login.html")
    
@calendario.route("/login", methods =["POST"])
def logando():
    if request.method == "POST":
        dre = request.form["dre"]
        senha = request.form["senha"]
        return login(dre,senha)
        
@calendario.route("/home")
def rota_home():
        return render_template("content.html")


calendario.run()

