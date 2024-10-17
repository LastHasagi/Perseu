from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
    
# Página de login
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Adicione a lógica de login aqui
        pass
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)