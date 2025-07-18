CREATE TABLE IF NOT EXISTS escola (
    id_inst INT PRIMARY KEY REFERENCES instituicao(id_inst),
    inep TEXT UNIQUE NOT NULL -- garante que é INEP válido
);
