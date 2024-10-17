from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
DATABASE = 'db/users.db'

# Garantir exisência do banco de dados
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL)''')
        conn.commit()
        
# <----- Páginas do sistema ----->

# Página de login/registro
@app.route('/')
def home():
    return render_template('home.html') 

# Página de visualização de usuários
@app.route('/users')
def users():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
    return render_template('users.html', users=users)

# <----- Lógica do sistema ----->	

# Registro de usuário
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    password_hash = generate_password_hash(password)
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password_hash))
        conn.commit()
    return redirect(url_for('home'))

# Login de usuário
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
    if user and check_password_hash(user[2], password):
        return redirect(url_for('users'))
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)