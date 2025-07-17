CREATE TABLE IF NOT EXISTS ongs (
    id_inst INT PRIMARY KEY REFERENCES instituicao(id_inst),
    nome_ong TEXT,
    cnpj TEXT UNIQUE
)