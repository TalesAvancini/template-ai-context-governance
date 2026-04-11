-- Snapshot Real da Tabela de Pedidos
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    stripe_session_id VARCHAR(255),
    status VARCHAR(50) DEFAULT 'pending', -- pending, succeeded, failed
    total_amount DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
