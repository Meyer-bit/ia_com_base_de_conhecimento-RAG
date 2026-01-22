# IA com Base de Conhecimento (RAG)

## 📌 Visão Geral

Este projeto foi desenvolvido com o objetivo de **aprender na prática os fundamentos necessários para um estágio em Inteligência Artificial**, principalmente na construção de aplicações que utilizam **IA generativa integrada a uma base de conhecimento própria**.

A aplicação implementa um fluxo simples de **RAG (Retrieval-Augmented Generation)**, onde documentos em PDF são transformados em embeddings, armazenados em um banco vetorial e utilizados para responder perguntas do usuário de forma contextualizada.

---

## 🎯 Objetivos do Projeto

- Entender como funciona uma aplicação real de IA baseada em documentos  
- Aprender a criar e consultar **bancos de dados vetoriais**  
- Aplicar conceitos de **Python**, **APIs**, **IA Generativa** e **engenharia de prompts**  
- Consolidar conhecimentos básicos de **Git/GitHub**, **Docker**, **APIs REST** e **SQL**

---

## 🧠 O que essa IA faz?

- Lê arquivos PDF que servem como **base de conhecimento**
- Converte o conteúdo dos PDFs em **embeddings**
- Armazena esses embeddings em um **banco vetorial (ChromaDB)**
- Permite que o usuário faça perguntas pelo terminal
- Busca os trechos mais relevantes e gera respostas baseadas **exclusivamente nos documentos**

Caso a resposta não esteja presente na base de conhecimento, a aplicação informa que não possui essa informação.

---

## 📚 Base de Conhecimento

A pasta `base/` contém PDFs com conteúdos introdutórios sobre:

- 🐍 **Python básico**
- 🌱 **Git e GitHub**
- 🐳 **Docker (conceitos iniciais)**
- 🌐 **APIs REST**
- 🗄️ **SQL básico**

Esses temas foram escolhidos por serem fundamentais para desenvolvimento backend e aplicações de IA.

---

## ⚙️ Funcionamento Técnico

### 1️⃣ Criação do Banco Vetorial (`criar_db.py`)

- Carrega todos os PDFs da pasta `base`
- Divide os textos em pequenos blocos (*chunks*)
- Gera embeddings utilizando a API da OpenAI
- Armazena os embeddings no **ChromaDB**

Esse processo simula como bases de conhecimento são criadas em sistemas reais de IA.

---

### 2️⃣ Consulta à IA (`central.py`)

- O usuário digita uma pergunta
- A aplicação realiza uma **busca semântica** no banco vetorial
- Os trechos mais relevantes são enviados ao modelo de linguagem
- A resposta é gerada com base **somente no contexto recuperado**

Esse padrão reduz respostas genéricas e evita alucinações do modelo.

---

## 🧩 Tecnologias Utilizadas

- **Python**
- **LangChain**
- **OpenAI API**
- **ChromaDB (Vector Store)**
- **dotenv**
- **Conceitos de RAG (Retrieval-Augmented Generation)**

