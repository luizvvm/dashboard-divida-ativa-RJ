# callbacks_analise.py
import plotly.express as px
import pandas as pd
from dash import callback, Output, Input, State
import requests
from app import app
import plotly.graph_objects as go


@callback(
    Output("tabela-resultados-busca", "data"),
    Input("botao-buscar", "n_clicks"), #inicia a função abaixo quando clicarem lá no botão que está no layout
    [
        #quando o input é acionado e somente quando é acionado, o state serve para trazer cada um dos componentes (o valor deles)
        #se fosse varios inputs em vez de state a função seria acionada toda vez que mexessemos nesses inputs, oq não queremos
        #se ainda não ficou claro, recomendo ler essa documentação:
        State("filtro-ano", "value"),
        State("filtro-natureza", "value"),
        State("filtro-agrupamento_situacao", "value"),
        State("ordenar-por", "value"),
        State("ordem", "value"),
    ],
)
#função para atualizar as tabelas
def atualizar_tabela_busca(n_clicks, ano, natureza, agrupamento_situacao, ordenar_por, ordem):
    if n_clicks is None:
        return []

    # Estamos colocando em um dicionario porque o usuario não selecione um dos valores ele não salva
    params = {}
    if ano:
        params["ano"] = ano
    if natureza:
        params["natureza"] = natureza
    #Necessário porque se não considera o 0 como false e não executa
    if agrupamento_situacao is not None:
        params["situacao"] = agrupamento_situacao
    if ordenar_por:
        params["ordenar_por"] = ordenar_por
    if ordem:
        params["ordem"] = ordem

    try:
        api_url = "http://127.0.0.1:8000/cda/search"
        #monta a busca lá pro backend (olhe lá no código main.py) e espera a resposta
        response = requests.get(api_url, params=params, timeout=30)
        response.raise_for_status()
        dados = response.json()

        # Pós processamento pra gente não mostrar "0, 1 ou -1 lá na tabela"
        situacao_map = {-1: "Cancelada", 0: "Em cobrança", 1: "Quitada"}
        for linha in dados:

            codigo_situacao = linha.get("agrupamento_situacao")
            texto_situacao = situacao_map.get(codigo_situacao, "Desconhecida")
            linha["agrupamento_situacao"] = texto_situacao

        return dados

    except requests.exceptions.RequestException as e:
        print(f"Erro ao chamar a API: {e}")
        return []
