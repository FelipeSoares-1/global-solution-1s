
# Guia de Instalação e Execução

## 1. Pré-requisitos

### 1.1 Instalar o Python
- Baixe e instale o Python (versão 3.x) a partir do site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/).
- Durante a instalação, marque a opção **Add Python to PATH**.

### 1.2 Instalar PostgreSQL
- Baixe e instale o PostgreSQL a partir do site oficial: [https://www.postgresql.org/download/](https://www.postgresql.org/download/).
- Anote as informações do banco de dados:
  - **Usuário**: geralmente `postgres`.
  - **Senha**: definida durante a instalação.
  - **Porta**: geralmente `5432`.

### 1.3 Criar o Banco de Dados
- Após instalar o PostgreSQL:
  - Abra o `pgAdmin` ou use o terminal para criar um banco de dados chamado `sistema_gestao_energetica`.
  - Comando SQL para criar o banco:
    ```sql
    CREATE DATABASE sistema_gestao_energetica;
    ```

---

## 2. Instalar Bibliotecas Python

### 2.1 Usando pip
1. Abra o terminal ou prompt de comando.
2. Instale as dependências:
   ```bash
   pip install psycopg2 pandas
   ```

### 2.2 Bibliotecas Utilizadas
- **psycopg2**: Para conectar e interagir com o PostgreSQL.
- **pandas**: Para manipulação de dados tabulares.

---

## 3. Configurar a Aplicação

### 3.1 Configurar as Credenciais do Banco
- No script, localize a seção `DB_CONFIG` e substitua as informações conforme sua instalação do PostgreSQL:
    ```python
    DB_CONFIG = {
        "dbname": "sistema_gestao_energetica",
        "user": "seu_usuario",
        "password": "sua_senha",
        "host": "localhost",
        "port": 5432
    }
    ```

### 3.2 Carregar Dados para Teste
- Substitua os exemplos de dados de `sample_data_consumo` no script Python pelos dados que você deseja importar.

Exemplo:
```python
sample_data_consumo = pd.DataFrame([
    [2023, 11, "Sudeste", "Residencial", 5000.0, 150.0],
    [2023, 11, "Nordeste", "Comercial", 3000.0, 100.0]
], columns=["ano", "mes", "regiao", "setor", "consumo_kwh", "consumo_per_capita"])
```

---

## 4. Executar a Aplicação

### 4.1 Executar no Terminal
1. Salve o script Python em um arquivo chamado `etl_energia.py`.
2. Execute o script:
   ```bash
   python etl_energia.py
   ```

### 4.2 Saída Esperada
- Criação das tabelas no banco de dados.
- Inserção dos dados de exemplo.
- Exibição das análises no terminal:
  - **Tendências de consumo por setor**.
  - **Variação de consumo per capita ao longo do tempo**.

---

## 5. Solução de Problemas

### Erro: "psycopg2 não encontrado"
- Verifique se o `pip` está configurado corretamente.
- Reinstale a biblioteca:
   ```bash
   pip install psycopg2
   ```

### Erro de Conexão com o Banco
- Certifique-se de que o PostgreSQL está em execução.
- Verifique as credenciais (usuário, senha, porta).

### Problema com Dados
- Certifique-se de que os dados estão no formato correto (DataFrame do Pandas).
