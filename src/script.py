# Script ETL para extrair, transformar e carregar dados no banco de dados PostgreSQL

import psycopg2
import pandas as pd

# Configurações do banco de dados
DB_CONFIG = {
    "dbname": "sistema_gestao_energetica",
    "user": "postgres",
    "password": "senha123",  # Atualize para sua senha real
    "host": "localhost",
    "port": 5432
}

# Função para conectar ao banco de dados
def connect_to_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

# Função para criar tabelas no banco
def create_tables():
    queries = [
        """
        CREATE TABLE IF NOT EXISTS energia_consumo (
            id SERIAL PRIMARY KEY,
            ano INT NOT NULL,
            mes INT NOT NULL,
            regiao VARCHAR(50),
            setor VARCHAR(50),
            consumo_kwh FLOAT,
            consumo_per_capita FLOAT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS energia_tarifas (
            id SERIAL PRIMARY KEY,
            distribuidora VARCHAR(100),
            ano INT NOT NULL,
            mes INT NOT NULL,
            tarifa_kwh FLOAT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS energia_demanda (
            id SERIAL PRIMARY KEY,
            ano INT NOT NULL,
            mes INT NOT NULL,
            demanda_maxima FLOAT,
            demanda_minima FLOAT,
            previsao_demanda FLOAT
        );
        """
    ]
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        for query in queries:
            cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Tabelas criadas com sucesso!")

# Função para carregar dados no banco
def load_data_to_db(table_name, data):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        for _, row in data.iterrows():
            if table_name == "energia_consumo":
                query = """
                INSERT INTO energia_consumo (ano, mes, regiao, setor, consumo_kwh, consumo_per_capita)
                VALUES (%s, %s, %s, %s, %s, %s);
                """
                cursor.execute(query, tuple(row))
            elif table_name == "energia_tarifas":
                query = """
                INSERT INTO energia_tarifas (distribuidora, ano, mes, tarifa_kwh)
                VALUES (%s, %s, %s, %s);
                """
                cursor.execute(query, tuple(row))
            elif table_name == "energia_demanda":
                query = """
                INSERT INTO energia_demanda (ano, mes, demanda_maxima, demanda_minima, previsao_demanda)
                VALUES (%s, %s, %s, %s, %s);
                """
                cursor.execute(query, tuple(row))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Dados carregados com sucesso na tabela {table_name}!")

# Função para executar consultas específicas
def execute_query(query):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results

# Exemplo de consultas para análise
def analyze_data():
    # Tendências de consumo por setor
    query_trends = """
    SELECT setor, ano, SUM(consumo_kwh) AS total_consumo
    FROM energia_consumo
    GROUP BY setor, ano
    ORDER BY setor, ano;
    """
    trends = execute_query(query_trends)
    print("Tendências de consumo por setor:")
    for row in trends:
        print(row)

    # Variação de consumo per capita ao longo do tempo
    query_variation = """
    SELECT ano, mes, AVG(consumo_per_capita) AS media_per_capita
    FROM energia_consumo
    GROUP BY ano, mes
    ORDER BY ano, mes;
    """
    variation = execute_query(query_variation)
    print("\nVariação de consumo per capita ao longo do tempo:")
    for row in variation:
        print(row)

# Executando o pipeline ETL
if __name__ == "__main__":
    # Criar tabelas
    create_tables()

    # Exemplo de carregamento de dados (substitua pelos seus datasets)
    sample_data_consumo = pd.DataFrame([
        [2023, 11, "Sudeste", "Residencial", 5000.0, 150.0],
        [2023, 11, "Nordeste", "Comercial", 3000.0, 100.0]
    ], columns=["ano", "mes", "regiao", "setor", "consumo_kwh", "consumo_per_capita"])
    load_data_to_db("energia_consumo", sample_data_consumo)

    # Realizar análises
    analyze_data()
