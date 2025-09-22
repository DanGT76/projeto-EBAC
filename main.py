from fastapi import FastAPI, HTTPException

app = FastAPI()

livros = {}

@app.get("/livros")
def get_livros():
    if not livros:
        return {"message": "Não existe nenhum livro"}
    else:
        return {"Livros": livros}
    
@app.post("/adiciona")
def post_livros(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: int):
    if id_livro in livros:
        raise HTTPException(status_code=400, detail="Esse livro já existe")
    else:
        livros[id_livro] = {"nome_livro": nome_livro, "autor_livro": autor_livro, "ano_livro": ano_livro}
        return {"message": "O livro foi criado com sucesso!"}
    
@app.put("/atualizar/{id_livro}")
def put_livro(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: int):
    meu_livro = livros.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=400, detail="Livro não encontrado")
    else:
        if nome_livro:
            meu_livro["nome_livro"] = nome_livro
        if autor_livro:
            meu_livro["autor_livro"] = autor_livro
        if ano_livro:
            meu_livro["ano_livro"] = ano_livro

        return {"message": "Livro atualizado com sucesso!"}
    
@app.delete("/deletar/{id_livro}")
def delete_livro(id_livro: int):
    if id_livro not in livros:
        raise HTTPException(status_code=400, detail="Livro não encontrado")
    else:
        del livros[id_livro]
        return {"message": "Livro deletado com sucesso!"}
