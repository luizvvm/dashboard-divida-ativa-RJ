# callbacks_resumo.py
import plotly.express as px
import pandas as pd
from dash import callback, Output, Input
import requests
from app import app
import plotly.graph_objects as go

@callback(
    Output('store-dados-principais', 'data'),
    Input('url', 'pathname')
)
def carregar_dados_principais(pathname):
    dados_completos = {}
    
    endpoints = {
        "search": "http://127.0.0.1:8000/cda/search",
        "quantidade_cdas": "http://127.0.0.1:8000/resumo/quantidade_cdas",
        "saldo_cdas": "http://127.0.0.1:8000/resumo/saldo_cdas",
        "inscricoes": "http://127.0.0.1:8000/resumo/inscricoes",
        "inscricoes_canceladas": "http://127.0.0.1:8000/resumo/inscricoes_canceladas",
        "inscricoes_quitadas": "http://127.0.0.1:8000/resumo/inscricoes_quitadas",
        "distribuicao_cdas": "http://127.0.0.1:8000/resumo/distribuicao_cdas",
        "montante_acumulado": "http://127.0.0.1:8000/resumo/montante_acumulado"
    }
    
    for nome, url in endpoints.items():
        try:
            response = requests.get(url, timeout=10) #Não tira o timeout nunca plmds, é mto importante, demorei mto pra descobrir, sem ele pode dar um monte de erro. Ele pede para tentar se conectar por 10 segundos a API
            response.raise_for_status()
            dados_completos[nome] = response.json()
        except requests.exceptions.RequestException:
            dados_completos[nome] = []
            print("AVISO: Falha ao carregar os dados de um dos endpoints")

    return dados_completos


@callback(
    Output("grafico-distribuicao-dos-valores-das-dividas-histograma","figure"),
    Input("store-dados-principais","data")
)
    
def histograma_dvdh(dados_do_store):
    if not dados_do_store or not dados_do_store.get('search'):
        return go.Figure()
    
    dados_temporario = dados_do_store['search']
    

    df = pd.DataFrame(dados_temporario)
        
    fig = px.histogram(
        df, 
        x="valor_saldo_atualizado", 
        nbins=50,
        title='<b>Distribuição dos valores das Dívidas</b>',
        marginal="rug",
        labels={'valor_saldo_atualizado': 'Valor do Saldo da Dívida (R$)'}
)
    fig.update_layout(title_x=0.5, yaxis_title="Contagem de Dívidas")
    
    return fig


@callback(
    Output("grafico-distribuicao-dos-valores-das-dividas-box-plot", "figure"),
    Input("store-dados-principais", "data")
)

def box_plot_dvdh(dados_do_store):
    if not dados_do_store or not dados_do_store.get('search'):
        return go.Figure()
    
    dados_temporario = dados_do_store['search']
    
    df = pd.DataFrame(dados_temporario)
    df_positivo = df[df['valor_saldo_atualizado'] > 0]
            
    fig = px.box(
        df_positivo, 
        x="natureza",               
        y="valor_saldo_atualizado", 
        color="natureza",               
        log_y=True,
        title='<b>Distribuição de Valores por Natureza da Dívida</b>',
        labels={
            'valor_saldo_atualizado': 'Valor do Saldo',
            'natureza': 'Natureza'
            }
        )
    
    fig.update_layout(title_x=0.5)
    
    #NÃO usar fig.show() que vimos nos exemplos do plotly
    return fig


@callback(
    Output("grafico-distribuicao-dos-scores-histograma", "figure"),
    Input("store-dados-principais", "data")
)
def histograma_gds(dados_do_store):
    if not dados_do_store or not dados_do_store.get('search'):
        return go.Figure()
    
    dados_temporario = dados_do_store['search']

    df = pd.DataFrame(dados_temporario)
        
    fig = px.histogram(
    df, 
    x="score", 
    color="natureza",               
    log_y=True,
    title='<b>Distribuição dos Scores das Dívidas</b>',
    labels={
        'score': 'Faixa de Score',
        "natureza":"Natureza"
        }
    )
    
    fig.update_layout(title_x=0.5, yaxis_title="Contagem de Dívidas")
    
    return fig 


@callback(
    Output("grafico-distribuicao-da-idade-das-dividas-barras", "figure"),
    Input("store-dados-principais", "data")
)

def barras_gdid(dados_do_store):
    if not dados_do_store or not dados_do_store.get('search'):
        return go.Figure()
    
    dados_temporario = dados_do_store['search']

    df = pd.DataFrame(dados_temporario)
        
    fig = px.histogram(
        df,
        x="qtde_anos_idade_cda", 
        nbins=30,
        title='<b>Distribuição da Idade das Dívidas</b>',
        labels={
            'qtde_anos_idade_cda': 'Idade da Dívida (Anos)', 
        }
    )
    
    fig.update_layout(title_x=0.5, yaxis_title="Contagem de Dívidas")
    
    return fig


@callback(
    Output("grafico-composicao-da-carteira-por-natureza-tree-map", "figure"),
    Input("store-dados-principais", "data")
)

def tree_map_gccn(dados_do_store):
    if not dados_do_store or not dados_do_store.get('quantidade_cdas'):
        return go.Figure()
    
    dados_temporario = dados_do_store['quantidade_cdas']
 
        
    df_resumo = pd.DataFrame(dados_temporario)
            
    fig = px.treemap(
        df_resumo, 
        path=[px.Constant("Todas as Dívidas"), 'name'],
        values='Quantidade',
        color='Quantidade',
        color_continuous_scale='Blues',
        title='<b>Composição da Dívida por Quantidade de CDAs</b>',
        labels={
            'name': 'Natureza',
            'Quantidade': 'Nº de Dívidas'
        }
    )
        
    fig.update_layout(title_x=0.5)
         
    return fig
        


@callback(
    Output("grafico-composicao-da-carteira-por-situacao-funnel", "figure"),
    Input("store-dados-principais", "data")
)

def funnel_gccs(dados_do_store):
    if not dados_do_store or not dados_do_store.get('search'):
        return go.Figure()
    
    dados_temporario = dados_do_store['search']

    df = pd.DataFrame(dados_temporario)
            
    data = dict(  
    number=[df.shape[0], len(df[df["agrupamento_situacao"] == 0]), len(df[df["agrupamento_situacao"] == 1])], #importante usar len pq se não retorna um dataframa, e não um número
    stage=["Total de Dívidas", "Em Cobrança", "Quitadas"])
            
    fig = px.funnel(data,
                    x='number',
                    y='stage',
                    title='<b>Composição da Carteira por Situação</b>',
                    labels={
                        "stage":""    
                    }
                    )

    fig.update_layout(title_x=0.5)
    
    return fig


@callback(
    Output("grafico-valor-da-divida-vs-score-contour", "figure"),
    Input("store-dados-principais", "data")
)

def contour_gvds(dados_do_store):
    if not dados_do_store or not dados_do_store.get('search'):
        return go.Figure()
    
    dados_temporario = dados_do_store['search']

    df = pd.DataFrame(dados_temporario)
    df_filtrado = df[df["valor_saldo_atualizado"] <= 300000]

    fig = px.density_contour(
        df_filtrado,
        x="score",
        y="valor_saldo_atualizado",
        title='<b>Densidade da Dívida por Valor e Score</b>',
        labels={
            "score":"Score",
            "valor_saldo_atualizado":"Valor da Dívida"
        }
        )
            
    fig.update_traces(contours_coloring="fill", contours_showlabels = True)

    fig.update_layout(
    title_x=0.5
    )

    return fig


@callback(
    Output("grafico-valor-da-divida-vs-natureza-violin", "figure"),
    Input("store-dados-principais", "data")
)

def violin_gvds(dados_do_store):
    if not dados_do_store or not dados_do_store.get('search'):
        return go.Figure()
    
    dados_temporario = dados_do_store['search']

    df = pd.DataFrame(dados_temporario)

    fig = px.violin(df, y="valor_saldo_atualizado",
                    color="natureza",
                    violinmode='overlay',
                    hover_data=df.columns,
                    title='<b>Distribuição do Valor da Dívida por Natureza</b>',
                    labels={
                        "valor_saldo_atualizado":"Valor da Dívida",
                        "natureza":"Natureza"
                    }
                    ) 
    
    fig.update_layout(title_x=0.5)
    
    return fig


@callback(
    Output("grafico-evolucao-da-inscricao-de-dividas-line", "figure"),
    Input("store-dados-principais", "data")
)

def line_geid(dados_do_store):
    if not dados_do_store or not dados_do_store.get('search'):
        return go.Figure()
    
    dados_temporario = dados_do_store['search']

    df = pd.DataFrame(dados_temporario)

    df_agrupado = df.groupby('ano')['valor_saldo_atualizado'].sum().reset_index()

    df_agrupado = df_agrupado.sort_values('ano')
    
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=list(df_agrupado.ano), y=list(df_agrupado.valor_saldo_atualizado)))

    fig.update_layout(
        title_text="<b>Evolução do Valor Total Inscrito por Ano</b>"
    )

    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=12*5,
                        label="5y",
                        step="month",
                        stepmode="backward"),
                    dict(count=10*12,
                        label="10y",
                        step="month",
                        stepmode="backward"),
                    dict(count=15*12,
                        label="15y",
                        step="month",
                        stepmode="todate"),
                    dict(count=20*12,
                        label="20y",
                        step="month",
                        stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        ) 
    )
    
    fig.update_layout(title_x=0.5)

    return fig


@callback(
    Output("grafico-evolucao-por-natureza-soma-dividas-line", "figure"),
    Input("store-dados-principais", "data")
)

def line_gensd(dados_do_store):
    if not dados_do_store or not dados_do_store.get('search'):
        return go.Figure()
    
    dados_temporario = dados_do_store['search']

    df = pd.DataFrame(dados_temporario)

    df_agrupado = df.groupby(['ano', 'natureza'])['valor_saldo_atualizado'].sum().reset_index()

    df_agrupado = df_agrupado.sort_values('ano')

    fig = px.line(
        df_agrupado, 
        x='ano', 
        y='valor_saldo_atualizado', 
        color='natureza', 
        title='<b>Evolução do Valor da Dívida por Natureza</b>',
        labels={
            "ano":"Ano",
            "valor_saldo_atualizado":"Valor da Dívida"
        }
    )

    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(title_x=0.5)

    return fig


@callback(
    Output("grafico-matriz-de-priorizacao-estrategica-bubble", "figure"),
    Input("store-dados-principais", "data")
)

def line_gmpe(dados_do_store):
    if not dados_do_store or not dados_do_store.get('search'):
        return go.Figure()
    
    dados_temporario = dados_do_store['search']

    df = pd.DataFrame(dados_temporario)

    fig = px.scatter(df, x="score", y="valor_saldo_atualizado",
                size="qtde_anos_idade_cda",
                color="natureza",
                hover_name="numCDA",
                log_x=True,
                size_max=60,
                title='<b>Matriz de Priorização Estratégica</b>',
                labels={
                    "score":"Score",
                    "valor_saldo_atualizado":"Valor da Dívida", 
                    "natureza":"Natureza",
                    "qtde_anos_idade_cda":"Quantidade de Anos da Idade da CDA"
                }
                )

    fig.update_layout(title_x=0.5)

    return fig

#Mexa aqui 
@callback(
    Output("grafico-quantidade_cdas-bar", "figure"),
    Input("store-dados-principais", "data")
)

def line_quantidade_cdas_bar(dados_do_store):
    if not dados_do_store or not dados_do_store.get('quantidade_cdas'):
        return go.Figure()
    
    dados_temporario = dados_do_store['quantidade_cdas']
        
    df_resumo = pd.DataFrame(dados_temporario)
        
    fig = px.bar(
        df_resumo,
        x='name',
        y='Quantidade',
        title='<b>Quantidade de Dívidas por Natureza</b>',
        labels={
            "Quantidade":"Número de Dívidas",
            "name":"Natureza"
        }
        )

    fig.update_layout(title_x=0.5)
        
    return fig
    


@callback(
    Output("grafico-saldo_cdas-bar", "figure"),
    Input("store-dados-principais", "data")
)

def line_saldo_cdas_bar(dados_do_store):
    if not dados_do_store or not dados_do_store.get('saldo_cdas'):
        return go.Figure()
    
    dados_temporario = dados_do_store['saldo_cdas']
        
    df_resumo = pd.DataFrame(dados_temporario)

    fig = px.bar(df_resumo,
            x='name',
            y='Saldo',
            title='<b>Valor Total da Dívida por Natureza</b>',
            labels={
            "name":"Natureza",
            "Saldo":"Valor Total"    
            }
            )

    fig.update_layout(title_x=0.5)

    return fig


@callback(
    Output("grafico-quantidade_cdas-pie", "figure"),
    Input("store-dados-principais", "data")
)

def line_quantidade_cdas(dados_do_store):
    if not dados_do_store or not dados_do_store.get('quantidade_cdas'):
        return go.Figure()
    
    dados_temporario = dados_do_store['quantidade_cdas']
        
    df_resumo = pd.DataFrame(dados_temporario)
        
    fig = px.pie(df_resumo,
                values='Quantidade',
                names='name',
                title='<b>Composição da Carteira por Quantidade de Títulos</b>',
                labels={
                "name":"Natureza"    
                }
                )

    fig.update_layout(title_x=0.5)

    return fig

    
@callback(
    Output("grafico-saldo_cdas-pie", "figure"),
    Input("store-dados-principais", "data")
)

def line_saldo_cdas(dados_do_store):
    if not dados_do_store or not dados_do_store.get('saldo_cdas'):
        return go.Figure()
    
    dados_temporario = dados_do_store['saldo_cdas']
        
    df_resumo = pd.DataFrame(dados_temporario)

    fig = px.pie(df_resumo,
            values='Saldo',
            names='name',
            title='<b>Composição da Carteira por Valor</b>',
            labels={
            "name":"Natureza",
            "Saldo":"Valor Total"    
            }
            )

    fig.update_layout(title_x=0.5)

    return fig


@callback(
    Output("grafico-inscricoes_cdas-line", "figure"),
    Input("store-dados-principais", "data")
)

def line_inscricoes_cdas_line(dados_do_store):
    if not dados_do_store or not dados_do_store.get('inscricoes') or not dados_do_store.get("inscricoes_canceladas") or not dados_do_store.get("inscricoes_quitadas"):
        return go.Figure()
    
    dados_temporario1 = dados_do_store['inscricoes']
    dados_temporario2 = dados_do_store['inscricoes_canceladas']
    dados_temporario3 = dados_do_store['inscricoes_quitadas']
    
        
    df_resumo1 = pd.DataFrame(dados_temporario1)
    df_resumo1['natureza'] = 'Total de Inscrições'
        
        
    df_resumo2 = pd.DataFrame(dados_temporario2)
    df_resumo2['natureza'] = 'Inscrições Canceladas'
        
    df_resumo3 = pd.DataFrame(dados_temporario3)
    df_resumo3['natureza'] = 'Inscrições Quitadas'

    df_agrupado = pd.concat([df_resumo1, df_resumo2, df_resumo3], ignore_index=True)

    df_agrupado = df_agrupado.sort_values('ano')

    fig = px.line(
        df_agrupado, 
        x='ano', 
        y='Quantidade', 
        color='natureza', 
        title='<b>Evolução das Inscrições, Cancelamentos e Quitações por Ano</b>',
        labels={
            "ano": "Ano",
            "Quantidade": "Número de CDAs",
            "natureza": "Status da Inscrição"
        },
        markers=True 
        )
    fig.update_layout(title_x=0.5)

    fig.update_xaxes(rangeslider_visible=True)

    return fig
    
    
@callback(
    Output("grafico-distribuicao_cdas-parallel", "figure"),
    Input("store-dados-principais", "data")
)

def line_distribuicao_cdas(dados_do_store):
    if not dados_do_store or not dados_do_store.get('distribuicao_cdas'):
        return go.Figure()
    
    dados_temporario = dados_do_store['distribuicao_cdas']

        
    df_resumo = pd.DataFrame(dados_temporario)
    fig = px.bar(
        df_resumo,
        x='name',
        y=['Em cobrança', 'Cancelada', 'Quitada'],
            
        title='<b>Comparativo de Situação das Dívidas por Tipo</b>',
        labels={
            'name': 'Tipo de Dívida',
            'value': 'Valor / Percentual',
            'variable': 'Situação'
            },
        barmode='group'
        )
    
    fig.update_layout(title_x=0.5, legend_title_text='Situação')

    return fig
    
    
@callback(
    Output("grafico-montante_acumulado_cdas-3d", "figure"),
    Input("store-dados-principais", "data")
)

def line_montante_acumulado_cdas_3d(dados_do_store):
    if not dados_do_store or not dados_do_store.get('montante_acumulado'):
        return go.Figure()
    
    dados_temporario = dados_do_store['montante_acumulado']

        
    df_resumo = pd.DataFrame(dados_temporario)
        
    z_data = df_resumo.drop(columns=['Percentual'])
    y_data = z_data.columns
        
    fig = go.Figure(data=[
        go.Surface(
            x = df_resumo["Percentual"],
            y = y_data,
            z = z_data.values,
            colorscale='Viridis'
        )
    ])

    fig.update_layout(
        title='<b>Superfície de Concentração da Dívida</b>',
        autosize=True,
        scene=dict(
            xaxis_title='Devedores (%)',
            yaxis_title='Natureza',
            zaxis_title='Valor Acumulado (%)'
        ),
        margin=dict(l=65, r=50, b=65, t=90),
    )
        
        #vamos ve se da certo, se der erro o erro é aqui
    fig.update_layout(title_x=0.5)
        
    return fig

    
@callback(
    Output("grafico-montante_acumulado_cdas-line", "figure"),
    Input("store-dados-principais", "data")
)

def line_inscricoes_cdas_line(dados_do_store):
    if not dados_do_store or not dados_do_store.get('montante_acumulado'):
        return go.Figure()
    
    dados_temporario = dados_do_store['montante_acumulado']

        
    df_resumo = pd.DataFrame(dados_temporario)
    colunas_das_linhas = ['IPTU', 'ISS', 'Taxas', 'Multas', 'ITBI']
    df_resumo = df_resumo.sort_values('Percentual')
        
    fig = px.line(
        df_resumo, 
        x='Percentual', 
        y=colunas_das_linhas, 
        title='<b>Curva de Concentração de Valor por Natureza</b>',
        labels={
            "Percentual": "Devedores Acumulados (%)",
            "value": "Dívida Acumulada (%)",
            "variable": "Natureza"
        },
        markers=True 
    )

    fig.update_layout(title_x=0.5)
    fig.update_xaxes(rangeslider_visible=True)

    return fig
    

@callback(
    Output("grafico-montante_acumulado_cdas-heatmap", "figure"),
    Input("store-dados-principais", "data")
)

def line_inscricoes_cdas_heatmap(dados_do_store):
    if not dados_do_store or not dados_do_store.get('montante_acumulado'):
        return go.Figure()
    
    dados_temporario = dados_do_store['montante_acumulado']
        
    df_resumo = pd.DataFrame(dados_temporario)
    df_resumo = df_resumo.sort_values('Percentual')
    df_heatmap = df_resumo.set_index('Percentual')
    
    fig = px.imshow(
            df_heatmap.transpose(), 
            aspect="auto", 
            color_continuous_scale='YlOrRd',
            title='<b>Mapa de Calor da Concentração de Valor</b>',
            labels=dict(x="Devedores (%)", y="Natureza", color="Valor Acumulado (%)")
        )
        
    fig.update_layout(title_x=0.5)
        
    return fig