# Projeto: Perseu

## Descrição
Este projeto é uma aplicação desenvolvida para cumprir o desafio proposto pela Tributo devido. 
Consiste em uma api + render de template html que cadastre, faça login e consulte informações sobre os usuários. 
Utilizei Python, HTML, CSS, JS e SQlite.

## Estrutura do Projeto
- **/**: Contém o código-fonte da aplicação.
    - **db/**: Banco de dados.
    - **templates/**: Arquivos HTML.
    - **static/**: Arquivos CSS e JS.

## Instalação
1. Clone o repositório:
     ```sh
     git clone https://github.com/LastHasagi/Perseu.git
     ```
2. Navegue até o diretório do projeto:
     ```sh
     cd Perseu
     ```
3. Ative o venv
    ```sh
    Python -m venv venv
    ./venv/Scripts/Activate
    ```
4. Instale as dependências:
     ```sh
     pip install -r requirements.txt
     ```

## Uso
Para iniciar a aplicação, execute:
```sh
python servidor.py
```
Você vai poder acessar (http://127.0.0.1:5001) para interagir com a aplicação. 

Para testar a api separadamente, baixe o Postman e execute da seguinte forma:

- GET: http://127.0.0.1:5001/api/users --> Envie uma solicitação GET com o parâmetro "None" para retornar um JSON com todos os usuários que temos salvos no DB.

- POST: http://127.0.0.1:5001/api/register --> Envie um JSON no "Body" para registrar seu usuário.
```json
{
    "username": "new_user",
    "password": "new_password"
}
```

- POST: http://127.0.0.1:5001/api/login --> Envie um JSON no "Body" para efetuar o login.
```json
{
    "username": "my_user",
    "password": "my_password"
}
```