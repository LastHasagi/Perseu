from flask import Flask, render_template, request, redirect, url_for, abort, flash, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

DATABASE = 'db/users.db'
app.secret_key = 'teste_processo_tributodevido'

# Garantir exisência do banco de dados antes de iniciar o servidor
def init_db():

    if not os.path.exists('db'):
        os.makedirs('db')
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL)''')
            conn.commit()  
                 
init_db()

# <----- Páginas do sistema ----->

# Página de login/registro
@app.route('/')
def home():
    return render_template('home.html') 

# Página de visualização de usuários
@app.route('/users', methods=['GET'])
def users():
    return render_template('users.html')

# <----- Lógica do sistema ----->	

# Registro de usuário
@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    password_hash = generate_password_hash(password)
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password_hash))
        conn.commit()
    
    return jsonify({'message': 'Usuário registrado com sucesso'}), 201

# Login de usuário
@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
    
    if user and check_password_hash(user[2], password):
        return jsonify({'message': 'Login bem-sucedido', 'redirect': url_for('users')}), 200
    
    return jsonify({'message': 'Usuário ou senha inválidos'}), 401

# Retornar todos os usuários
@app.route('/api/users', methods=['GET'])
def api_users():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT username, password FROM users')
        users = cursor.fetchall()
    
    users_list = [{'username': user[0], 'password': user[1]} for user in users]
    return jsonify(users_list)

if __name__ == '__main__':
    app.run(debug=True, port=5001)