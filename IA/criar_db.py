from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

PASTA_PDFS = "base"
PASTA_DB = "db"


def criar_db():
    documentos = carregar_docs()
    print(f"{len(documentos)} páginas carregadas")

    chunks = dividir_chunks(documentos)
    print(f"{len(chunks)} chunks criados")

    gerar_embeddings(chunks)


def carregar_docs():
    loader = PyPDFDirectoryLoader(PASTA_PDFS, glob="*.pdf")
    return loader.load()


def dividir_chunks(documentos):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return splitter.split_documents(documentos)


def gerar_embeddings(chunks):
    Chroma.from_documents(
        chunks,
        OpenAIEmbeddings(),
        persist_directory=PASTA_DB
    )
    print("Banco de dados criado com sucesso!")


if __name__ == "__main__":
    criar_db()
