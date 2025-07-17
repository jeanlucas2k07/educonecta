CREATE TABLE IF NOT EXISTS instituicao (
    id_inst SERIAL PRIMARY KEY,
    tipo TEXT NOT NULL,
    endereco TEXT NOT NULL,
    nome_respnsAvel TEXT NOT NULL,
    identificador TEXT UNIQUE NOT NULL

)