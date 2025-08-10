import json
from typing import List, Dict, Optional

import pandas as pd
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Carregando os DADOS
try:
    df_cdas = pd.read_json("data/cdas.json")
    df_cdas["numCDA"] = df_cdas["numCDA"].astype(str)
    df_cdas["ano"] = df_cdas["numCDA"].str[:4].astype(int)
except FileNotFoundError:
    print('ERRO: O arquivo "data/cdas.json" não foi encontrado.')
    # necessário criar um dataframe vazio pq se não pode dar ruim se iniciar
    df_cdas = pd.DataFrame()


# Endpoints


@app.get("/")
def read_root():
    return {"message": "API para o Desafio Técnico LAMDEC - Backend"}


@app.get("/resumo/{file_name}", response_model=List[Dict])
def get_resumo(file_name: str):
    file_path = f"data/{file_name}.json"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        # Retorna um erro HTTP 404 se o arquivo não for encontrado.
        raise HTTPException(
            status_code=404, detail=f"Arquivo '{file_name}.json' não encontrado."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar o arquivo: {e}")


@app.get("/cda/search", response_model=List[Dict])
def search_cdas(
    ano: Optional[int] = None,
    natureza: Optional[str] = None,
    situacao: Optional[str] = None,
    score_min: Optional[float] = None,
    saldo_min: Optional[float] = None,
    ordenar_por: Optional[str] = "valor_saldo_atualizado",
    ordem: Optional[str] = "desc",
):

    if df_cdas.empty:
        raise HTTPException(
            status_code=503, detail="Dados de CDAs não disponíveis no momento."
        )

    # Cópia do DataFrame completo
    df_filtered = df_cdas.copy()

    # Aplica os filtros se eles forem fornecidos
    if ano:
        df_filtered = df_filtered[df_filtered["ano"] == ano]
    if natureza:
        # Ignora maiusculo e minusculo
        df_filtered = df_filtered[
            df_filtered["natureza"].str.lower() == natureza.lower()
        ]
    if score_min:
        df_filtered = df_filtered[df_filtered["score"] >= score_min]
    if saldo_min:
        df_filtered = df_filtered[df_filtered["valor_saldo_atualizado"] >= saldo_min]
    if situacao:
        # Mapeia a string da situação para o código numérico correspondente
        situacao_map = {"cancelada": -1, "em cobrança": 0, "quitada": 1}
        situacao_code = situacao_map.get(situacao.lower())
        if situacao_code is not None:
            df_filtered = df_filtered[
                df_filtered["agrupamento_situacao"] == situacao_code
            ]

    # Aplica a ordenação
    ascending = ordem.lower() == "asc"
    if ordenar_por in df_filtered.columns:
        df_filtered = df_filtered.sort_values(by=ordenar_por, ascending=ascending)

    # Retorna os dados filtrados e ordenados no formato JSON
    return df_filtered.to_dict("records")
