CREATE TABLE IF NOT EXISTS escola (
    id_inst INT PRIMARY KEY REFERENCES instituicao(id_inst),
    nome_escola TEXT,
    inep TEXT UNIQUE
)