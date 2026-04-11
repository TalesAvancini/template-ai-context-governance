-- ---------------------------------------------------------
-- Criado em: 2026-04-10
-- Ultima Atualizacao: 2026-04-10
-- Status: Ativo
-- ---------------------------------------------------------

-- Snapshot real da estrutura do banco de dados (SSOT)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
