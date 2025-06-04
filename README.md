# ☕ Sistema de Gestão para Cafeteria - Cafeteria Voyage

📌 **Versão atual:** 2.0.0

🔗 **Acesse o sistema:** [cafeteria-voyage.onrender.com](https://cafeteria-voyage.onrender.com/)  

🏷️ **Versão anterior disponível:** [v1.0.0](https://github.com/seu-usuario/projeto-cafeteria/releases/tag/v1.0.0)

🗓️ **Última atualização:** Junho de 2025

Sistema desenvolvido em Python com Flask, com o objetivo de gerenciar de forma moderna e interativa as operações internas de uma cafeteria. Inclui controle completo de cardápio, pedidos e mesas, além de interface web com front-end responsivo.

---

## 🚀 Novidades da Versão 2.0.0

- 💻 Interface Web com **Flask + HTML + CSS + JS**
- 🖼️ Exibição visual do cardápio com imagens e categorias
- 🔄 Integração total com banco de dados relacional (SQLite)
- 🛠️ Refatoração completa do projeto em Flask + SQLAlchemy
- 🎯 Padronização de nomes e imagens usando filtros personalizados no Jinja

---

## ✅ Funcionalidades por Versão

### 🧩 **Versão 1.0.0** (disponível na tag `v1.0.0`)

- CRUD completo com dados em JSON:
    - 📦 **Pedidos**
    - 🧾 **Cardápio**
    - 🪑 **Mesas**
- Monitoramento automático com `threading`:
    - Atualização do status dos pedidos a cada 15 segundos
    - Liberação automática da mesa ao finalizar o pedido
- Estrutura modular em múltiplas camadas:
    - `main.py`, `servicos/`, `repositorios/`, `interface/`, `utils/`, `dados_json/`

---

### ✨ **Versão 2.0.0** (versão atual)

- Utilização de banco de dados relacional com **SQLAlchemy**
- Rotas organizadas com **Blueprints**
- Organização baseada em arquitetura **MVC**:
    - **Model** → `app/models/`
    - **View** → `templates/`, `static/`
    - **Controller** → `app/views/`
- Front-end moderno e responsivo para:
    - Navegar por subcategorias do cardápio
    - Visualizar detalhes dos itens e opcionais
    - Adicionar itens ao pedido
- Novo fluxo de entrada via `index.html` (login)

---

## 🗂️ Estrutura do Projeto (2.0.0)

```
📁 app/
├── 📁 config/           # Configurações do Flask (ex: ConfigDev)
├── 📁 models/           # Modelos do banco de dados (Cardápio, Pedido, Mesa)
├── 📁 views/            # Blueprints e rotas (cardápio, pedidos, etc.)
├── 📁 static/           # Arquivos estáticos (CSS, JS, imagens)
│   ├── 📁 css/          # Estilos personalizados
│   ├── 📁 js/           # Scripts JavaScript
│   └── 📁 img/          # Imagens usadas no sistema
├── 📁 templates/        # Páginas HTML renderizadas (Jinja2)

📁 instance/
└── cafeteria.db         # Banco de dados SQLite gerado pelo SQLAlchemy

📁 dados_json/           # Arquivos JSON para popular o banco (dados antigos)

run.py                  # Ponto de entrada da aplicação Flask
main.py                 # Função create_app e configuração do banco
requirements.txt        # Dependências do projeto
.gitignore              # Arquivos/pastas ignoradas no versionamento
venv/                   # Ambiente virtual (não versionado)
README.md               # Documentação do projeto

```

---

## ⚙️ Tecnologias Utilizadas

- Python 3.11+
- Flask
- SQLAlchemy
- HTML, CSS, JS
- Bootstrap Icons
- SQLite
    
    (v1.0.0: JSON, threading)
  
---
## ⚠️ Observação sobre o Banco de Dados

Esse projeto foi desenvolvido como parte de um trabalho acadêmico e, por isso, utilizamos o SQLite como banco de dados — uma solução mais simples e prática para projetos locais e de pequeno porte.

- Atualmente, o sistema está hospedado no Render, e vale lembrar que plataformas como essa não mantêm o banco SQLite após reinicializações do servidor. Por isso, os dados cadastrados no site são temporários e podem ser apagados após algum tempo.
---

## 📂 Como Executar

Clone o repositório:

```bash
git clone https://github.com/vbluuiza/cafeteria-voyage
cd projeto-cafeteria
```

Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o sistema:

```bash
python run.py
```

---

### 👥 Autores

Projeto desenvolvido por estudantes do curso de Análise e Desenvolvimento de Sistemas – **Cesar School**:

- **Luiza Vieira** · [LinkedIn](https://www.linkedin.com/in/vbluuiza)
- **Marcello Augusto** · [LinkedIn](https://www.linkedin.com/in/marcelloaugustosv/)
- **Gabriel Duarte** · [LinkedIn](https://www.linkedin.com/in/gabrieltduart/)
- **Lucca Spinelli** · [LinkedIn](https://www.linkedin.com/in/lucca-spinelli-a65672240/)
- **Eliziane Mota** · [LinkedIn](https://www.linkedin.com/in/eliziane-mota/)
- **Laíza Freitas** · [LinkedIn](https://www.linkedin.com/in/laizafreitas/)

🎓 Projeto acadêmico para a disciplina Fundamentos da Programação (FP) — Professora Aeda Souza.
