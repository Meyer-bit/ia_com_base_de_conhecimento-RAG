from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from typer import prompt
from langchain_prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
CD_DB = "db"

prompt_template = """
Responda a pergunta do usuário da melhor forma possível:
{pergunta}

Utilize os seguintes trechos de documentos para encontrar a resposta:
{contexto}

Se a resposta não estiver nos documentos, responda que não sabe.
"""

def perguntar():
    pergunta = input("Digite sua pergunta: ")

    funcao_embeddings = OpenAIEmbeddings()
    db = Chroma(persist_directory=CD_DB, embedding_function=funcao_embeddings)
    
    
    resultados = db.similarity_search_with_relevance_scores(pergunta, k=3)
    if len(resultados) == 0 or resultados[0][1] < 0.7:
            print("Desculpe, não consegui encontrar informações relevantes.")
            return
    
    textos_resultados = []
    for resultado in resultados:
        texto = resultado.page_content
        textos_resultados.append(texto)

    contexto = "\n".join(textos_resultados)
    prompt = ChatPromptTemplate.from_template(prompt_template)
    prompt = prompt.invoke({"pergunta": pergunta, "contexto": contexto})

modelo = ChatOpenAI()
texto_resposta = modelo.invoke(prompt)
print("Resposta:", texto_resposta)

perguntar()