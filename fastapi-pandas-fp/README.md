# 🚀 FastAPI + Pandas + Programação Funcional (FP)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688.svg)](https://fastapi.tiangolo.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Finalizado-success.svg)]()

> Projeto integrador da disciplina de **Linguagem Python** — unindo **Pandas**, **Programação Funcional (FP)** e **FastAPI** em um sistema completo de análise e exposição de dados via API.

---

## 📁 Estrutura do Projeto


```
fastapi-pandas-fp/
├── data/
│ └── dados.csv
├── src/
│ ├── core/
│ │ └── metrics.py
│ ├── app.py
│ └── make_stats.py
├── stats.json
├── requirements.txt
├── README.md
└── prints/
├── docs.png
└── stats.png
```

## ⚙️ Instalação

## 🧩 Pré-requisitos: Python 3.9+ instalado

Clone o repositório e entre na pasta:
```
git clone https://github.com/CaioSarti/fastapi-pandas-fp.git
cd fastapi-pandas-fp
```
Crie e ative um ambiente virtual:
```
python -m venv venv
venv\Scripts\activate
```
Instale as dependências:
```
pip install -r requirements.txt
```
## 🧮 Geração de Dados e Estatísticas

O script make_stats.py gera o dataset dados.csv e o arquivo stats.json com estatísticas resumidas.
```
python src/make_stats.py
```
## 📄 Saída esperada:
```
data/dados.csv
stats.json
```
## 🌐 Subindo a API (FastAPI)

Execute o servidor local com Uvicorn:
```
uvicorn src.app:app --reload
```
## 🔗 Acesse no navegador:

http://127.0.0.1:8000

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/stats

## 🧠 Endpoints Principais
```
Método     Rota         Descrição
GET         /           Mensagem inicial de boas-vindas
GET	        /health	    Verifica se a API está online
GET	        /stats	    Retorna o conteúdo de stats.json
POST        /soma       Recebe { "x": float, "y": float } e retorna a soma
```
## 🧩 Mini Desafio FP — map(), filter(), reduce()

Função analisar(lista, limite) aplica conceitos de programação funcional:
```
1.Filtra números pares maiores que limite. 
2.Eleva ao quadrado (map).
3.Usa reduce para somar e contar.
4.Calcula média inteira (soma // contagem).
```
Exemplo de retorno:
```
{
  "soma_quadrados": 32456,
  "contagem": 58,
  "media_inteira": 559
}
```
## 🧱 Orientação a Objetos (POO)

O projeto utiliza classes para modularizar a lógica:

DataLoader → lê e valida o CSV

StatsService → calcula estatísticas usando Pandas

APIService → expõe as informações via FastAPI

Essas classes ficam organizadas dentro de src/core/.

## 💻 Interface Streamlit (opcional)

Se desejar rodar a interface visual:
```
streamlit run ui/app.py
```
Recursos:

Exibe estatísticas da API
Gráficos de colunas com Pandas
Formulário de teste para o endpoint /soma

## 🖼️ Prints Obrigatórios

## 📸 Página /docs

<img width="1237" height="547" alt="docs png" src="https://github.com/user-attachments/assets/06dea7d9-d7b0-4599-9c19-1aca38770ff2" />
<img width="1242" height="588" alt="docs2 png" src="https://github.com/user-attachments/assets/7b78f90b-0029-48d3-897c-4ce7a1e95952" />



## 📸 Retorno /stats


<img width="354" height="291" alt="stats png" src="https://github.com/user-attachments/assets/206e852d-4ead-49d4-a405-88a645614933" />


## ✅ Execução Completa

Verifique que o projeto roda sem erros:
```
pip install -r requirements.txt
python src/make_stats.py
uvicorn src.app:app --reload
```
## 🧩 Tecnologias Utilizadas
| Tecnologia | Função |
|-------------|--------|
| **Python 3.9+** | Linguagem principal |
| **Pandas** | Manipulação de dados |
| **FastAPI** | Criação da API |
| **Uvicorn** | Servidor ASGI |
| **Streamlit** | Interface (opcional) |
| **Pydantic** | Validação de modelos |
## 📊 Exemplo de stats.json
```
{
  "qtd_total": 100,
  "receita_total": 25432.9,
  "preco_medio": 25.4,
  "desafio_fp": {
    "soma_quadrados": 32456,
    "contagem": 58,
    "media_inteira": 559
  }
}
```
## 👨‍💻 Autor
Caio Sarti | 📍 Projeto acadêmico — Disciplina: Linguagem Python | 📅 Outubro / 2025
