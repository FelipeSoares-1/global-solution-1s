-- Criação do Banco de Dados
CREATE DATABASE sistema_gestao_energetica;

-- Selecionando o banco de dados
\\c sistema_gestao_energetica;

-- Tabela: energia_consumo
CREATE TABLE energia_consumo (
    id SERIAL PRIMARY KEY,
    ano INT NOT NULL,
    mes INT NOT NULL,
    regiao VARCHAR(50),
    setor VARCHAR(50),
    consumo_kwh FLOAT,
    consumo_per_capita FLOAT
);

-- Tabela: energia_tarifas
CREATE TABLE energia_tarifas (
    id SERIAL PRIMARY KEY,
    distribuidora VARCHAR(100),
    ano INT NOT NULL,
    mes INT NOT NULL,
    tarifa_kwh FLOAT
);

-- Tabela: energia_demanda
CREATE TABLE energia_demanda (
    id SERIAL PRIMARY KEY,
    ano INT NOT NULL,
    mes INT NOT NULL,
    demanda_maxima FLOAT,
    demanda_minima FLOAT,
    previsao_demanda FLOAT
);

