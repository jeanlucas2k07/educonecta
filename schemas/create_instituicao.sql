CREATE TABLE IF NOT EXISTS instituicao (
    id_inst SERIAL PRIMARY KEY,
    tipo TEXT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    endereco TEXT NOT NULL,
    responsavel TEXT NOT NULL,
    identificador TEXT UNIQUE NOT NULL
)