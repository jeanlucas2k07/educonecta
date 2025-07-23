CREATE TABLE IF NOT EXISTS ong (
    id_inst INT PRIMARY KEY REFERENCES instituicao(id_inst),
    cnpj TEXT UNIQUE NOT NULL -- garante que é CNPJ válido
);
