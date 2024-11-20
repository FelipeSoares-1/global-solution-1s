# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Global Solution - 1º Semestre
##- Cognitive Data Science (CDS) 

##- Computational Thinking with Python (CTWP)

## Grupo 11

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/caiorcastro/">Caio Rodrigues Castro</a> 
- <a href="https://www.linkedin.com/in/ederson-badeca/">Ederson Luiz Badeca dos Santos</a> 
- <a href="https://www.linkedin.com/in/digitalmanagerfelipesoares/">Felipe Soares Nascimento</a>
- <a href="https://www.linkedin.com/in/lfhillesheim/">Lucas Ferreira Hillesheim</a>



## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a/">Lucas Gomes</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi Chiovato</a>

## 📜 Descrição

Este projeto visa criar uma solução integrada para monitoramento, análise e otimização do consumo energético, utilizando técnicas de ciência de dados, programação em Python e integração com bases de dados relacionais. O sistema é projetado para atender às necessidades de eficiência energética, sustentabilidade e facilidade de uso em ambientes residenciais e empresariais.



## Funcionalidades Principais

1. **Monitoramento e Controle em Tempo Real**
   - Ajuste automático do consumo energético com base nas tarifas vigentes e demanda.
   - Integração de fontes de energia renovável (solar e eólica).

2. **Previsão Energética com IA**
   - Análise de dados históricos para identificar tendências de consumo e demanda.
   - Algoritmos preditivos para otimizar a eficiência energética.

3. **Interface Gráfica em Python**
   - Relatórios detalhados de eficiência energética.
   - Visualização de dados e recomendações em tempo real.

4. **Análise de Dados Avançada**
   - Banco de dados relacional com informações históricas de consumo.
   - Pipeline de ETL para manipulação e análise de grandes volumes de dados.

---

## Tecnologias Utilizadas

- **Python**: Para desenvolvimento do sistema e interface gráfica.
- **PostgreSQL**: Banco de dados relacional para armazenar e consultar dados históricos.
- **R**: Análises estatísticas avançadas e geração de relatórios preditivos.
- **Dash/Tkinter**: Construção de interfaces gráficas interativas.
- **Wokwi**: Simulação de sensores de consumo energético.

---

## Estrutura do Banco de Dados (CDS)

### Tabelas:
1. **energia_consumo**
   - Armazena dados históricos de consumo energético.
   - **Colunas**:
     - `id`: Identificador único.
     - `ano`: Ano de referência.
     - `mes`: Mês de referência.
     - `regiao`: Região geográfica.
     - `setor`: Setor de consumo.
     - `consumo_kwh`: Consumo em kWh.
     - `consumo_per_capita`: Consumo per capita.

2. **energia_tarifas**
   - Histórico de tarifas por distribuidoras.
   - **Colunas**:
     - `id`: Identificador único.
     - `distribuidora`: Nome da distribuidora.
     - `ano`: Ano de referência.
     - `mes`: Mês de referência.
     - `tarifa_kwh`: Tarifa por kWh.

3. **energia_demanda**
   - Dados sobre demanda máxima/mínima e previsões.
   - **Colunas**:
     - `id`: Identificador único.
     - `ano`: Ano de referência.
     - `mes`: Mês de referência.
     - `demanda_maxima`: Demanda máxima em kW.
     - `demanda_minima`: Demanda mínima em kW.
     - `previsao_demanda`: Previsão de demanda para o próximo período.

---

## Funcionalidades em Python (CTWP)

### Sistema Automatizado
- Monitoramento do consumo energético interno.
- Algoritmo para seleção da fonte de energia mais econômica e sustentável.

### Interface Gráfica
- Desenvolvida com **Tkinter** ou **Dash**.
- Relatórios de consumo diário/semanal.
- Gráficos interativos para visualização de tendências.


## 🔧 Como executar o código

Para executar o código, siga os passos abaixo:

1. **Pré-requisitos**: Certifique-se de ter o R e as bibliotecas `psycopg2`, `pandas`, `matplotlib` e `dash` (opcional) instaladas.
Banco de dados PostgreSQL configurado.
2. **Instalação** e **Execução**:
   - Seguir Guia de Instalação e Execução [Guia de Instalação e Execução](./document/documentação.md) em Document.

## 🗃 Histórico

* 19/10/2024
    * Entrega final do projeto com análise completa.
    * Teste de Banco de dados PostgreSQL
    * Teste de configuração do Banco de dados PostgreSQL


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
