# layout.py

from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc


layout_inicio = html.Div([
    html.Div(
        [
            # O título fica DENTROOOOOOOOOOOOO do banner
            html.H2("Análise da Dívida Ativa", className="display-5 fw-bold"),
        ],
        className="banner-container mb-5"
    ),
    dbc.Card(dbc.CardBody([
        html.H3("Introdução", className="text-2xl font-bold dark:text-white"),
        
            html.P("""Este dash-board tem como objetivo apresentar e levantar insights valiosos acerda da Dívida Ativa da Procuradoria Geral do Município do Rio de Janeiro (PGM-Rio),
                para isso utilizaremos mais de 6000 dados disponibilizados pelo LAMDEC, Laboratório de Métodos de Suporte à Tomada de Decisão,
                caracterizado como Grupo de Pesquisa, Desenvolvimento e Inovação (PD&I) do Instituto de Matemática (IM) da Universidade Federal do Rio de Janeiro (UFRJ).""", className="mb-3 text-gray-500 dark:text-gray-400"),
        
        
        html.H3("O que é a Dívida Ativa?", className="text-2xl font-bold dark:text-white"),
        
            html.P("""A Dívida Ativa é, essencialmente, um cadastro de inadimplentes do município. É a formalização de todas as dívidas que pessoas físicas ou jurídicas,
                têm com a Prefeitura e que já estão com o prazo de pagamento vencido.""", className="mb-3 text-gray-500 dark:text-gray-400",),
        
        
        html.H3("Análise Descritiva", className="text-2xl font-bold dark:text-white"),
        
            dcc.Graph(id='grafico-distribuicao-dos-valores-das-dividas-histograma'),
            
            html.P("""Observando o histograma, é perceptivel para o leitor que a maioria das dívidas são de baixo valor, 
                isto é, ficam abaixo de R$ 700.000,00. Observe também o Rug Plot na parte superior,
                cada tracinho é uma dívida, note como eles formam uma linha grossa e quase contínua na extrema esquerda e,
                como vão se dispersando e se tornando mais isolados à medida que o valor aumenta.""", className="mb-3 text-gray-500 dark:text-gray-400",),
            
            dcc.Graph(id='grafico-distribuicao-dos-valores-das-dividas-box-plot'),
            
            html.P("""Agora, com este segundo gráfico da distribuição de valores por natureza da dívida, podemos perceber que a ideia de 
                valor baixo e valor alto dependem muito do tipo da dívida.""", className="mb-3 text-gray-500 dark:text-gray-400",),
            html.P("""Começando pelo IPTU e pelo ITBI, possuem a menor mediana de todas as categorias,
                além de terem caixas mais compactas, indicando que essas dívidas de IPTU e ITBI são bem parecidas entre si e de valor baixo.""", className="mb-3 text-gray-500 dark:text-gray-400",),
            html.P("""Já as dívidas do ISS, Taxas e Multas, formam um grupo intermediário, isto é, possuem mediana mais altas que as do IPTU e ITBI,
                    além de também possuírem as caixas mais esticadas, o que mostra uma clara variação maior nos valores.""", className="mb-3 text-gray-500 dark:text-gray-400",),
            html.P("""Por fim e a que mais se destaca, temos as dívidas de natureza "Outros", que é a que mais se destaca. Isso porque, possui a mediana mais alta e a caixa mais longa de todas elas, portanto,
                possui alta variabilidade e alto valor, as dívidas são muito diferentes uma das outras aqui e, em geral, representam valores bem maiores também.""", className="mb-3 text-gray-500 dark:text-gray-400",),
            
            dcc.Graph(id='grafico-distribuicao-dos-scores-histograma'),
            
            html.P("""Não sei interpretar essa merda ainda, então aqui vai um monte de texto exto exteot texto texto texto texto texto texto texto texto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            html.P("""texto texto texto texto texto textotexto texto textotexto texto textotexto texto textotexto texto texto
                   texto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            
            dcc.Graph(id='grafico-distribuicao-da-idade-das-dividas-barras'),
            
            html.P("""Não sei interpretar essa merda ainda, então aqui vai um monte de texto exto exteot texto texto texto texto texto texto texto texto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            html.P("""texto texto texto texto texto textotexto texto textotexto texto textotexto texto textotexto texto texto
                   texto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            
            
            dcc.Graph(id='grafico-composicao-da-carteira-por-natureza-tree-map'),
            
            html.P("""Não sei interpretar essa merda ainda, então aqui vai um monte de texto exto exteot texto texto texto texto texto texto texto texto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            html.P("""texto texto texto texto texto textotexto texto textotexto texto textotexto texto textotexto texto texto
                   texto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            
            dcc.Graph(id='grafico-composicao-da-carteira-por-situacao-funnel'),
            
            html.P("""Não sei interpretar essa merda ainda, então aqui vai um monte de texto exto exteot texto texto texto texto texto texto texto texto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            html.P("""texto texto texto texto texto textotexto texto textotexto texto textotexto texto textotexto texto texto
                   texto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
        
        html.H3("Análise de Correlações", className="text-2xl font-bold dark:text-white"),

            html.P("""texto texto texto texto texto textotexto texto textotexto texto textotexto texto textotexto texto texto
                   texto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            
            dcc.Graph(id='grafico-valor-da-divida-vs-score-contour'),
            
            html.P("""Não sei interpretar essa merda ainda, então aqui vai um monte de texto exto exteot texto texto texto texto texto texto texto texto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            html.P("""texto texto texto texto texto textotexto texto textotexto texto textotexto texto textotexto texto texto
                   texto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),

            dcc.Graph(id='grafico-valor-da-divida-vs-natureza-violin'),
            
            html.P("""Não sei interpretar essa merda ainda, então aqui vai um monte de texto exto exteot texto texto texto texto texto texto texto texto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            html.P("""texto texto texto texto texto textotexto texto textotexto texto textotexto texto textotexto texto texto
                   texto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            
        html.H3("Análise Temporal", className="text-2xl font-bold dark:text-white"),

            html.P("""texto texto texto texto texto textotexto texto textotexto texto textotexto texto textotexto texto texto
                   texto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            
            dcc.Graph(id='grafico-evolucao-da-inscricao-de-dividas-line'),
            
            html.P("""Não sei interpretar essa merda ainda, então aqui vai um monte de texto exto exteot texto texto texto texto texto texto texto texto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            html.P("""texto texto texto texto texto textotexto texto textotexto texto textotexto texto textotexto texto texto
                   texto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            
            dcc.Graph(id='grafico-evolucao-por-natureza-soma-dividas-line'),
            
            html.P("""Não sei interpretar essa merda ainda, então aqui vai um monte de texto exto exteot texto texto texto texto texto texto texto texto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            html.P("""texto texto texto texto texto textotexto texto textotexto texto textotexto texto textotexto texto texto
                   texto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            
            dcc.Graph(id='grafico-matriz-de-priorizacao-estrategica-bubble'),
            
            html.P("""Não sei interpretar essa merda ainda, então aqui vai um monte de texto exto exteot texto texto texto texto texto texto texto texto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",),
            html.P("""texto texto texto texto texto textotexto texto textotexto texto textotexto texto textotexto texto texto
                   texto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto textotexto texto texto""", className="mb-3 text-gray-500 dark:text-gray-400",)

    ]))
])

#jaja mexo nisso, por enquanto é só um template
layout_resumo = html.Div([
    html.H2("Painel de Resumo", className="display-5 fw-bold mb-4"),
    html.P("Apresentação dos insights mais importantes de forma rápida, clara e direta.", className="lead mb-5"),
    dbc.Row([
        dbc.Col(html.Div(className="chart-card", children=[
            html.H5("Saldo Total por Tipo de Dívida", className="fw-semibold mb-4"),
            dcc.Graph(id='grafico-saldo-por-natureza')
        ]), width=6),
        dbc.Col(html.Div(className="chart-card", children=[
            html.H5("Composição da Dívida por Quantidade", className="fw-semibold mb-4"),
            dcc.Graph(id='grafico-qtde-por-natureza')
        ]), width=6),
    ]),
    html.Div(className="chart-card", children=[
        html.H5("Evolução Anual: Inscrições, Quitações e Cancelamentos", className="fw-semibold mb-4"),
        dcc.Graph(id='grafico-evolucao-temporal'),
        dcc.RangeSlider(id='slider-ano', min=1980, max=2024, step=1, value=[2010, 2024],
                        marks={str(ano): str(ano) for ano in range(1980, 2025, 5)})
    ])
])

layout_analise = html.Div([ html.H2("Página de Análise Estratégica (Implementar)") ])
layout_busca = html.Div([ html.H2("Página da Ferramenta de Busca (Implementar)") ])


def create_layout():
    #Cria a estrutura completa da página, com a sidebar e o conteúdo.
    sidebar = html.Div(className="sidebar", children=[
        html.Div(className="sidebar-header", children=[
            html.Div(
                style={
                    'background-color': 'white',
                    'height': '70px',
                    'width': '70px',
                    'border-radius': '50%',
                    'margin-bottom': '10px',
                    
                    
                    'display': 'inline-flex', 
                    'justify-content': 'center',
                    'align-items': 'center'
                },
                children=[
                html.Img(
                    src='/assets/lamdec.png', style={'height': '60%'}
                )
            ]
        ),
            html.H1("Dívida Ativa", className="h3 fw-bold"),
            html.P("Análise de Dados", className="small text-white-50 mt-1")
        ]),
        
        dbc.Nav(
            [
                dbc.NavLink([html.I(className="bi bi-house-door fs-5"), html.Span("Início", className="ms-3")], href="/", active="exact"),
                dbc.NavLink([html.I(className="bi bi-pie-chart fs-5"), html.Span("Painel de Resumo", className="ms-3")], href="/resumo", active="exact"),
                dbc.NavLink([html.I(className="bi bi-bar-chart-line fs-5"), html.Span("Análise Estratégica", className="ms-3")], href="/analise", active="exact"),
                dbc.NavLink([html.I(className="bi bi-search fs-5"), html.Span("Ferramenta de Busca", className="ms-3")], href="/busca", active="exact"),
            ],
            vertical=True,
            pills=False, # Pills está adicionando um fundo azul horrivel, vou arrumar com CSS
            className="sidebar-nav"
        ),
        html.Div(className="sidebar-footer", children=[
            html.P("Desafio Técnico LAMDEC/UFRJ", className="small text-white-50")
        ])
    ])

    content = html.Main(id="page-content", className="content")
    
    # refresh=False deixa a pagina com navegação sem "bug" de loading, se não fica atualizando e fica estranho
    return html.Div([dcc.Location(id="url", refresh=False), dcc.Store(id='store-dados-principais'), sidebar, content])