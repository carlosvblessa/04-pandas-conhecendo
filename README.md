# Pandas: Conhecendo a Biblioteca

> Projeto criado para explorar e preparar dados imobiliários do Rio de Janeiro utilizando a biblioteca Pandas.

## 🎯 Objetivo

Este projeto tem como objetivo atender às demandas do time de Desenvolvimento e de Machine Learning, trabalhando com uma base de dados real sobre imóveis no Rio de Janeiro. As etapas incluem:

- Importação e análise inicial dos dados
- Limpeza e tratamento de dados nulos
- Criação de novas colunas categóricas
- Aplicação de filtros
- Salvamento dos dados tratados

## 🧩 Estrutura do Projeto

| Pasta | Descrição |
|-------|-----------|
| `/data` | Armazena os datasets brutos e processados |
| `/src` | Scripts principais para ETL e análise |
| `/notebooks` | Notebooks Jupyter para exploração interativa |
| `/docs` | Documentação adicional |

## 📌 Tarefas

As tarefas foram importadas automaticamente do Trello como Issues no GitHub.

## 🚀 Setup Inicial

Veja as instruções abaixo para configurar o repositório localmente.
```

---

## 3. 🛠️ Setup Inicial do Repositório

### Passo a passo:

1. **No GitHub:**
   - Crie um novo repositório chamado `04-pandas-conhecendo`

2. **Clone localmente:**

   ```bash
   git clone https://github.com/carlosvblessa/04-pandas-conhecendo.git
   cd pandas-projeto-exploratorio
   ```

3. **Estrutura inicial recomendada:**

   ```bash
   mkdir -p data src notebooks docs
   touch README.md requirements.txt .gitignore
   ```

4. **Adicione `.gitignore` básico:**

   ```bash
   echo "*.pyc\n__pycache__\n*.ipynb\n.env\n.DS_Store" > .gitignore
   ```

5. **Arquivo `requirements.txt`:**

   ```txt
   pandas
   jupyter
   matplotlib
   seaborn
   scikit-learn
   ```

6. **Commit inicial:**

   ```bash
   git add .
   git commit -m "setup inicial do projeto"
   git push origin main
   ```

---

## 🎁 Bônus: GitHub Project (opcional)

Se quiser replicar o layout do Trello no GitHub:

1. Crie um **GitHub Project (Beta)**
2. Use a API GraphQL para adicionar os cards automaticamente (posso te ajudar com isso também)

---

## ✔️ Próximos Passos Recomendados

- Suba o dataset CSV na pasta `data/`
- Crie um notebook de análise exploratória
- Divida scripts em módulos (`load_data.py`, `clean_data.py`, etc.)
- Configure CI/CD (GitHub Actions) para testes automáticos


