# Falando sobre o DB escolhido

Para esse projeto, estou usando o MySQL como banco de dados para armazenar todas as informações que vem das interfaces.
Por motivos de segurança, todos os arquivos que contenham informações sigilosas só poderão ser acessador por usuários específicos.

## SQL para criar a tabela usuario
```sql
CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    nivel_acesso INT CHECK(nivel_acesso BETWEEN 0 AND 3) NOT NULL,
    ativo ENUM('sim', 'não') NOT NULL,
    logado ENUM('sim', 'não') NOT NULL
);
```

## SQL para criar a tabela log_admin

```sql
CREATE TABLE log_admin (
    id INT PRIMARY KEY AUTO_INCREMENT,
    acao TEXT NOT NULL,
    quem_fez VARCHAR(255) NOT NULL,
    usuario_afetado VARCHAR(255),
    itens_afetados INT NOT NULL,
    data_hora DATETIME NOT NULL
);
```