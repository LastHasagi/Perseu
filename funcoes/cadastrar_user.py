from flask import redirect, url_for, render_template, flash, session
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from flask import redirect, url_for, render_template, flash, session
from functools import wraps
from datetime import datetime

load_dotenv()

def get_cursor(connection):
    return connection.cursor(dictionary=True)

# <<---- Conectar ao banco de dados ---->> #
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        
        if connection.is_connected():
            print("Connection established")
            return connection
    
    except Error as e:
        print(f"Error: '{e}'")
        return None

# <<---- Registrar usuário ---->> 
def register_user(cursor, connection,nome, senha, email, nivel_acesso, telefone, ativo):
    try:
        cursor.execute("INSERT INTO usuarios (nome, senha, email, nivel_acesso, telefone, ativo) VALUES (%s, %s, %s, %s, %s, %s)", (nome, senha, email, nivel_acesso, telefone, ativo))
        connection.commit() 
    except Exception as e:
        flash('Ocorreu um erro ao tentar cadastrar o usuário.', 'error')
        print(f"Erro: {e}")
