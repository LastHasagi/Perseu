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