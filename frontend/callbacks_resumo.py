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
    try:
        api_url = "http://127.0.0.1:8000/cda/search"
        response = requests.get(api_url)
        response.raise_for_status()
        dados = response.json()
        return dados
    except requests.exceptions.RequestException:
        return [] 


@callback(
    Output("grafico-distribuicao-dos-valores-das-dividas-histograma","figure"),
    Input("store-dados-principais","data")
)
    
def histograma_dvdh(dados):
    if not dados:
        return go.Figure()

    df = pd.DataFrame(dados)
        
    fig = px.histogram(
        df, 
        x="valor_saldo_atualizado", 
        nbins=50,
        title="Distribuição dos Valores das Dívidas",
        marginal="rug",
        labels={'valor_saldo_atualizado': 'Valor do Saldo da Dívida (R$)'}
)
    return fig

@callback(
    Output("grafico-distribuicao-dos-valores-das-dividas-box-plot", "figure"),
    Input("store-dados-principais", "data")
)

def box_plot_dvdh(dados):
    if not dados:
        return go.Figure()
    
    df = pd.DataFrame(dados)
    df_positivo = df[df['valor_saldo_atualizado'] > 0]
            
    fig = px.box(
        df_positivo, 
        x="natureza",               
        y="valor_saldo_atualizado", 
        color="natureza",               
        log_y=True,
        title="Distribuição de Valores por Natureza da Dívida",
        labels={
            'valor_saldo_atualizado': 'Valor do Saldo (R$ - Escala Log)',
            'natureza': 'Natureza da Dívida'
            }
        )
            
    #NÃO usar fig.show() que vimos nos exemplos do plotly
    return fig

@callback(
    Output("grafico-distribuicao-dos-scores-histograma", "figure"),
    Input("store-dados-principais", "data")
)
def histograma_gds(dados):
    if not dados:
        return go.Figure()

    df = pd.DataFrame(dados)
        
        
    fig = px.histogram(
    df, 
    x="score", 
    #nbins=30,
    color="natureza",               
    log_y=True,
    title="Distribuição dos Scores das Dívidas",
    labels={
        'score': 'Faixa de Score', 'count': 'Contagem de Dívidas', "natureza":"Natureza da Dívida"
        }
    )
    return fig 



@callback(
    Output("grafico-distribuicao-da-idade-das-dividas-barras", "figure"),
    Input("store-dados-principais", "data")
)

def barras_gdid(dados):
    if not dados:
        # Se os dados estiverem vazios (ex: erro na API), não faz nada
        return go.Figure()

    # Não precisa mais de try...except para a API aqui
    df = pd.DataFrame(dados)
        
    fig = px.histogram(
        df,
        x="qtde_anos_idade_cda", 
        nbins=30,
        title="Distribuição da Idade das Dívidas",
        labels={
            'qtde_anos_idade_cda': 'Idade da Dívida (Anos)', 
            'count': 'Contagem de Dívidas'
        }
    )
    return fig

    

@callback(
    Output("grafico-composicao-da-carteira-por-natureza-tree-map", "figure"),
    Input("store-dados-principais", "data")
)

def tree_map_gccn(trigger_id):
    try:
        api_url = "http://127.0.0.1:8000/resumo/quantidade_cdas"
        response = requests.get(api_url)
        response.raise_for_status()
        dados = response.json()
        
        df_resumo = pd.DataFrame(dados)
            
        fig = px.treemap(
            df_resumo, 
            path=[px.Constant("Todas as Dívidas"), 'name'],
                
            values='Quantidade',
                
            color='Quantidade',
            color_continuous_scale='Blues',
            title="Composição da Dívida por Quantidade de CDAs (Treemap)"
        )
            
        return fig
        
    except requests.exceptions.RequestException as e:
    # Em caso de erro, retorna um box plot vazio com a mensagem
        return px.box().update_layout(title_text=f"Erro ao conectar à API: {e}")

@callback(
    Output("grafico-composicao-da-carteira-por-situacao-funnel", "figure"),
    Input("store-dados-principais", "data")
)

def tree_map_gccn(dados):
    if not dados:
        # Se os dados estiverem vazios (ex: erro na API), não faz nada
        return go.Figure()

    # Não precisa mais de try...except para a API aqui
    df = pd.DataFrame(dados)
            
    data = dict(
                
    number=[df.shape[0], len(df[df["agrupamento_situacao"] == 0]), len(df[df["agrupamento_situacao"] == 1])], #importante usar len pq se não retorna um dataframa, e não um número
    stage=["Total de Dívidas", "Dívidas em Negociação", "Dívidas Quitadas"])
            
    fig = px.funnel(data, x='number', y='stage', title="Composição da Carteira por Situação")
            
    return fig

@callback(
    Output("grafico-valor-da-divida-vs-score-contour", "figure"),
    Input("store-dados-principais", "data")
)

def contour_gvds(dados):
    if not dados:
        # Se os dados estiverem vazios (ex: erro na API), não faz nada
        return go.Figure()

    # Não precisa mais de try...except para a API aqui
    df = pd.DataFrame(dados)
    df_filtrado = df[df["valor_saldo_atualizado"] <= 300000]

    fig = px.density_contour(
        df_filtrado, x="score", y="valor_saldo_atualizado", title="Distribuição do Valor da Dívida por score"
        )
            
    fig.update_traces(contours_coloring="fill", contours_showlabels = True)
            
    return fig

@callback(
    Output("grafico-valor-da-divida-vs-natureza-violin", "figure"),
    Input("store-dados-principais", "data")
)


def violin_gvds(data):
    if not data:
        return go.Figure() 

    df = pd.DataFrame(data)

    fig = px.violin(df, y="valor_saldo_atualizado", color="natureza",
                    violinmode='overlay',
                    hover_data=df.columns,
                    title="Distribuição do Valor da Dívida por Natureza") 

    return fig

@callback(
    Output("grafico-evolucao-da-inscricao-de-dividas-line", "figure"),
    Input("store-dados-principais", "data")
)


def line_geid(data):
    if not data:
        return go.Figure() 

    df = pd.DataFrame(data)

    df.columns = [col.replace("AAPL.", "") for col in df.columns]

    df_agrupado = df.groupby('ano')['valor_saldo_atualizado'].sum().reset_index()

    df_agrupado = df_agrupado.sort_values('ano')
    
    # Create figure
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=list(df_agrupado.ano), y=list(df_agrupado.valor_saldo_atualizado)))

    # Set title
    fig.update_layout(
        title_text="Evolução da Inscrição de Dívidas"
    )

    # Add range slider
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


    return fig


@callback(
    Output("grafico-evolucao-por-natureza-soma-dividas-line", "figure"),
    Input("store-dados-principais", "data")
)


def line_geid(data):
    if not data:
        return go.Figure() 

    df = pd.DataFrame(data)

    df_agrupado = df.groupby(['ano', 'natureza'])['valor_saldo_atualizado'].sum().reset_index()

    df_agrupado = df_agrupado.sort_values('ano')

    fig = px.line(
        df_agrupado, 
        x='ano', 
        y='valor_saldo_atualizado', 
        color='natureza', 
        title="Evolução da Inscrição de Dívidas por Natureza"
    )

    fig.update_xaxes(rangeslider_visible=True)

    return fig


@callback(
    Output("grafico-matriz-de-priorizacao-estrategica-bubble", "figure"),
    Input("store-dados-principais", "data")
)

def line_geid(data):
    if not data:
        return go.Figure() 

    df = pd.DataFrame(data)

    fig = px.scatter(df, x="score", y="valor_saldo_atualizado",
                size="qtde_anos_idade_cda", color="natureza",
                    hover_name="numCDA", log_x=True, size_max=60, title="Como a composição percentual mudou ao longo do tempo?")

    return fig
