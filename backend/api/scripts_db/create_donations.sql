CREATE TABLE IF NOT EXISTS donations (
    id SERIAL PRIMARY KEY,
    donor_id INT NOT NULL REFERENCES users(id) ,
    id_benefited INT NOT NULL REFERENCES instituicao(id_inst),
    donation DECIMAL (10, 2) NOT NULL,
    donated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
)