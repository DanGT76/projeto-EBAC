from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="API de livros",
    description="API para gerenciar livros",
    version="1.0.0",
    contact={
        "name": "Daniel de Oliveira",
        "email": "ti.daniel76@gmail.com"
    }
)

meu_livrozinho = {}

class Livro(BaseModel):
    nome_livro: str
    autor_livro: str
    ano_livro: int

@app.get("/livros")
def get_livros():
    if not meu_livrozinho:
        return {"message": "Não existe nenhum livro"}
    else:
        return {"Livros": meu_livrozinho}
    
@app.post("/adiciona")
def post_livros(id_livro: int, livro: Livro):
    if id_livro in meu_livrozinho:
        raise HTTPException(status_code=400, detail="Esse livro já existe")
    else:
        meu_livrozinho[id_livro] = livro.dict()
        return {"message": "O livro foi criado com sucesso!"}
    
@app.put("/atualizar/{id_livro}")
def put_livro(id_livro: int, livro: Livro):
    meu_livro = meu_livrozinho.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=400, detail="Livro não encontrado")
    else:
        meu_livrozinho[id_livro] = livro.dict()
        return {"message": "Livro atualizado com sucesso!"}
    
@app.delete("/deletar/{id_livro}")
def delete_livro(id_livro: int):
    if id_livro not in meu_livrozinho:
        raise HTTPException(status_code=400, detail="Livro não encontrado")
    else:
        del meu_livrozinho[id_livro]
        return {"message": "Livro deletado com sucesso!"}
