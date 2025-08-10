# layout.py

from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc


layout_inicio = html.Div(
    [
        #div pro Banner 
        html.Div(
            [
                html.H2("Análise da Dívida Ativa", className="display-5 fw-bold"),
            ],
            className="banner-container mb-5",
        ),
        #dbc.Card é para moldura
        dbc.Card(
            #dbc.CardBody é a parte de dentro, o espaço interno
            dbc.CardBody(
                [
                    html.H3(
                        "Introdução", className="text-2xl font-bold dark:text-white"
                    ),
                    html.P(
                        """Este dash-board tem como objetivo apresentar e levantar insights valiosos acerda da Dívida Ativa da Procuradoria Geral do Município do Rio de Janeiro (PGM-Rio),
                para isso utilizaremos mais de 6000 dados disponibilizados pelo LAMDEC, Laboratório de Métodos de Suporte à Tomada de Decisão,
                caracterizado como Grupo de Pesquisa, Desenvolvimento e Inovação (PD&I) do Instituto de Matemática (IM) da Universidade Federal do Rio de Janeiro (UFRJ).""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Para tal, esse dashboard foi organizado da seguinte forma:""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.Div(
                        [
                            #Isso já é mais comum então não vou comentar, é a mesma estrutura de lista do html.
                            html.Ul(
                                [
                                    html.Li(
                                        [
                                            html.Span(
                                                "Início: ",
                                                className="font-semibold text-gray-900 dark:text-white",
                                            ),
                                            html.Span(
                                                "Contém análises com gráficos acerca da Dívida Ativa da PGM-Rio.",
                                                className="max-w-md space-y-1 text-gray-500 list-decimal list-inside dark:text-gray-400",
                                            ),
                                        ]
                                    ),
                                    html.Li(
                                        [
                                            html.Span(
                                                "Resumo: ",
                                                className="font-semibold text-gray-900 dark:text-white",
                                            ),
                                            html.Span(
                                                "Contém uma análise resumida com dados pré-processados acerca da Dívida Ativa da PGM-Rio",
                                                className="max-w-md space-y-1 text-gray-500 list-decimal list-inside dark:text-gray-400",
                                            ),
                                        ]
                                    ),
                                    html.Li(
                                        [
                                            html.Span(
                                                "Painel Geral: ",
                                                className="font-semibold text-gray-900 dark:text-white",
                                            ),
                                            html.Span(
                                                "Reune todos os gráficos desenvolvidos com os dados da Dívida Ativa",
                                                className="max-w-md space-y-1 text-gray-500 list-decimal list-inside dark:text-gray-400",
                                            ),
                                        ]
                                    ),
                                    html.Li(
                                        [
                                            html.Span(
                                                "Ferramenta de Busca: ",
                                                className="font-semibold text-gray-900 dark:text-white",
                                            ),
                                            html.Span(
                                                "Fornece a possibilidade de filtrar e visualizar os dados.",
                                                className="max-w-md space-y-1 text-gray-500 list-decimal list-inside dark:text-gray-400",
                                            ),
                                        ]
                                    ),
                                ]
                            ),
                        ],
                        className="mb-3",
                    ),
                    #Troca de tópico
                    html.H3(
                        "O que é a Dívida Ativa?",
                        className="text-2xl font-bold dark:text-white",
                    ),
                    html.P(
                        """A Dívida Ativa é, essencialmente, um cadastro de inadimplentes do município. É a formalização de todas as dívidas que pessoas físicas ou jurídicas,
                têm com a Prefeitura e que já estão com o prazo de pagamento vencido.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Troca de tópico
                    html.H3(
                        "Análise Descritiva",
                        className="text-2xl font-bold dark:text-white",
                    ),
                    html.P(
                        """Observando o histograma, é perceptivel para o leitor que a maioria das dívidas são de baixo valor, 
            isto é, ficam abaixo de R$ 700.000,00. Observe também o Rug Plot na parte superior,
            cada tracinho é uma dívida, note como eles formam uma linha grossa e quase contínua na extrema esquerda e,
            como vão se dispersando e se tornando mais isolados à medida que o valor aumenta.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico da distribuição dos valores das dívidas (histograma)
                    dcc.Graph(
                        id="grafico-distribuicao-dos-valores-das-dividas-histograma"
                    ),
                    html.P(
                        """Observando o histograma, é perceptivel para o leitor que a maioria das dívidas são de baixo valor, 
                isto é, ficam abaixo de R$ 700.000,00. Observe também o Rug Plot na parte superior,
                cada tracinho é uma dívida, note como eles formam uma linha grossa e quase contínua na extrema esquerda e,
                como vão se dispersando e se tornando mais isolados à medida que o valor aumenta.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico da distribuição de valores por natureza da dívida (box-plot)
                    dcc.Graph(
                        id="grafico-distribuicao-dos-valores-das-dividas-box-plot"
                    ),
                    html.P(
                        """Agora, com este segundo gráfico da distribuição de valores por natureza da dívida, podemos perceber que a ideia de 
                valor baixo e valor alto dependem muito do tipo da dívida.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Começando pelo IPTU e pelo ITBI, possuem a menor mediana de todas as categorias,
                além de terem caixas mais compactas, indicando que essas dívidas de IPTU e ITBI são bem parecidas entre si e de valor baixo.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Já as dívidas do ISS, Taxas e Multas, formam um grupo intermediário, isto é, possuem mediana mais altas que as do IPTU e ITBI,
                    além de também possuírem as caixas mais esticadas, o que mostra uma clara variação maior nos valores.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Por fim e a que mais se destaca, temos as dívidas de natureza "Outros", que é a que mais se destaca. Isso porque, possui a mediana mais alta e a caixa mais longa de todas elas, portanto,
                possui alta variabilidade e alto valor, as dívidas são muito diferentes uma das outras aqui e, em geral, representam valores bem maiores também.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Grafico da distribuição dos scores das dívidas (histograma)
                    dcc.Graph(id="grafico-distribuicao-dos-scores-histograma"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Grafico da idade das dívidas (barras)
                    dcc.Graph(id="grafico-distribuicao-da-idade-das-dividas-barras"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico da composição da carteira por quantidade de CDAs (Tree-map)
                    dcc.Graph(
                        id="grafico-composicao-da-carteira-por-natureza-tree-map"
                    ),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico da composição da carteira por situação (Funnil)
                    dcc.Graph(id="grafico-composicao-da-carteira-por-situacao-funnel"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Troca de tópico
                    html.H3(
                        "Análise de Correlações",
                        className="text-2xl font-bold dark:text-white",
                    ),  
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico da Densidade da Dívida por valor e score (contorno)
                    dcc.Graph(id="grafico-valor-da-divida-vs-score-contour"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico do valor da dívida por natureza (violin)
                    dcc.Graph(id="grafico-valor-da-divida-vs-natureza-violin"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Troca de tópico
                    html.H3(
                        "Análise Temporal",
                        className="text-2xl font-bold dark:text-white",
                    ),  
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico da evolução da inscrição da dívida (linha)
                    dcc.Graph(id="grafico-evolucao-da-inscricao-de-dividas-line"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico da evolução do valor da dívida por natureza (linha)
                    dcc.Graph(id="grafico-evolucao-por-natureza-soma-dividas-line"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico da matriz de priozição estratégia (bubble)
                    dcc.Graph(id="grafico-matriz-de-priorizacao-estrategica-bubble"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                ]
            )
        ),
    ]
)


#Layout da página (resumo)
layout_resumo = html.Div(
    [
        #Div pro banner
        html.Div(
            [
                html.H2("Resumo da Dívida Ativa", className="display-5 fw-bold"),
            ],
            className="banner-container-pag2 mb-5",
        ),
        #dbc.Card é para moldura
        dbc.Card(
            #dbc.CardBody é a parte de dentro, o espaço interno
            dbc.CardBody(
                [
                    html.H3(
                        "Resumo Gerencial da Carteira de Dívida Ativa",
                        className="text-2xl font-bold dark:text-white",
                    ),
                    html.P(
                        """ As visualizações a seguir foram desenvolvidas utilizando os dados dos endpoints de resumo.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer non vehicula tellus, eu pellentesque diam. Phasellus convallis orci dictum nisi commodo""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.H3(
                        "Lorem ipsum dolor sit",
                        className="text-2xl font-bold dark:text-white",
                    ),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer non vehicula tellus, eu pellentesque diam. Phasellus convallis orci dictum nisi commodo""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    # Evolução das inscrições, cancelamentos e quitações por ano (linha)
                    dcc.Graph(id="grafico-inscricoes_cdas-line"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico quantidade de dívidas por natureza (barras)
                    dcc.Graph(id="grafico-quantidade_cdas-bar"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico valor total da dívida por natureza (barras)
                    dcc.Graph(id="grafico-saldo_cdas-bar"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico composição da carteira por quantidade de títulos (pizza)
                    dcc.Graph(id="grafico-quantidade_cdas-pie"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico composição da carteira por valor (pizza)
                    dcc.Graph(id="grafico-saldo_cdas-pie"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico comparativo de situação das dívidas por tipo (barras)
                    dcc.Graph(id="grafico-distribuicao_cdas-parallel"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico superfície de concentração da dívida (3D)
                    dcc.Graph(id="grafico-montante_acumulado_cdas-3d"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico curva de concentração de valor por natureza (line)
                    dcc.Graph(id="grafico-montante_acumulado_cdas-line"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    #Gráfico mapa de calor da concentração de valor (heatmap)
                    dcc.Graph(id="grafico-montante_acumulado_cdas-heatmap"),
                    html.P(
                        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget iaculis lectus. Nunc in leo arcu. Donec nec lobortis ipsum. Sed ornare pretium quam eget dignissim. Suspendisse vitae tortor suscipit elit posuere ornare at a leo. Maecenas vestibulum ante a nibh pellentesque, nec tristique lorem convallis.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                    html.P(
                        """Proin dapibus, turpis non sagittis dignissim, lorem augue aliquam ante, porttitor viverra ligula mauris sed dui. Proin tempus ex lorem, id lobortis dui pretium quis. Cras bibendum ullamcorper enim, eget suscipit libero facilisis non. Quisque elementum rhoncus lacus, et semper sapien ultricies vel. Aenean finibus sodales risus id cursus.""",
                        className="mb-3 text-gray-500 dark:text-gray-400",
                    ),
                ]
            )
        ),
    ]
)

#layout pro painel geral com todos os gráficos
layout_geral = html.Div(
    [
        html.H2("Painel Geral", className="display-5 fw-bold mb-4"),
        html.P("Apresentação de todos os gráficos feitos.", className="lead mb-5"),
        
        #Row é para deixar uns itens do lado do outro, organizando em filas. Tudo que tiver aqui em baixo vai para a "fila/linha 1"
        #Tudo que tiver aqui dentro vai tentar ser posicionado um do lado do outro
        #linh 1
        dbc.Row(
            [
                #Col é como se fosse uma "coluna" de dentro do row, então cada Col pode ser um gráfico diferente.
                #linha 1 coluna 1
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico da distribuição dos valores das dívidas (histograma)
                            dcc.Graph(
                                id="grafico-distribuicao-dos-valores-das-dividas-histograma"
                            )
                        ],
                    ),
                    width=6,
                ),
                #linha 1 coluna 2
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico da distribuição de valores por natureza da dívida (box-plot)
                            dcc.Graph(
                                id="grafico-distribuicao-dos-valores-das-dividas-box-plot"
                            )
                        ],
                    ),
                    width=6,
                ),
            ]
        ),
        #linha 2
        dbc.Row(
            [
                #linha 2 coluna 1
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Grafico da distribuição dos scores das dívidas (histograma)
                            dcc.Graph(
                                id="grafico-distribuicao-dos-scores-histograma"
                                )
                        ],
                    ),
                    width=6,
                ),
                #linha 2 coluna 2
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Grafico da idade das dívidas (barras)
                            dcc.Graph(
                                id="grafico-distribuicao-da-idade-das-dividas-barras"
                            )
                        ],
                    ),
                    width=6,
                ),
            ]
        ),
        #linha 3
        dbc.Row(
            [
                #linha 3 coluna 1
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico da composição da carteira por quantidade de CDAs (Tree-map)
                            dcc.Graph(
                                id="grafico-composicao-da-carteira-por-natureza-tree-map"
                            )
                        ],
                    ),
                    width=6,
                ),
                #linha 3 coluna 2
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico da composição da carteira por situação (Funnil)
                            dcc.Graph(
                                id="grafico-composicao-da-carteira-por-situacao-funnel"
                            )
                        ],
                    ),
                    width=6,
                ),
            ]
        ),
        #linha 4
        dbc.Row(
            [
                #linha 4 coluna 1
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico da Densidade da Dívida por valor e score (contorno)
                            dcc.Graph(
                                id="grafico-valor-da-divida-vs-score-contour"
                                )
                        ],
                    ),
                    width=6,
                ),
                #linha 4 coluna 2
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico do valor da dívida por natureza (violin)
                            dcc.Graph(
                                id="grafico-valor-da-divida-vs-natureza-violin"
                                )
                        ],
                    ),
                    width=6,
                ),
            ]
        ),
        #linha 5
        dbc.Row(
            [
                #linha 5 coluna 1
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico da evolução da inscrição da dívida (linha)
                            dcc.Graph(
                                id="grafico-evolucao-da-inscricao-de-dividas-line"
                            )
                        ],
                    ),
                    width=6,
                ),
                #linha 5 coluna 2
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico da evolução do valor da dívida por natureza (linha)
                            dcc.Graph(
                                id="grafico-evolucao-por-natureza-soma-dividas-line"
                                )
                        ],
                    ),
                    width=6,
                ),
            ]
        ),
        #linha 6
        dbc.Row(
            [
                #linha 6 coluna 1
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico da matriz de priozição estratégia (bubble)
                            dcc.Graph(
                                id="grafico-matriz-de-priorizacao-estrategica-bubble"
                            )
                        ],
                    ),
                    width=6,
                ),
                #linha 6 coluna 2
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        # Evolução das inscrições, cancelamentos e quitações por ano (linha)
                        children=[
                            dcc.Graph(
                                id="grafico-inscricoes_cdas-line"
                                )
                            ],
                    ),
                    width=6,
                ),
            ]
        ),
        #linha 7
        dbc.Row(
            [
                #linha 7 coluna 1
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico quantidade de dívidas por natureza (barras)
                            dcc.Graph(
                                id="grafico-quantidade_cdas-bar"
                                )
                            ],
                    ),
                    width=6,
                ),
                #linha 7 coluna 2
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico valor total da dívida por natureza (barras)
                            dcc.Graph(
                                id="grafico-saldo_cdas-bar"
                                )
                            ],
                    ),
                    width=6,
                ),
            ]
        ),
        #linha 8
        dbc.Row(
            [
                #linha 8 coluna 1
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico composição da carteira por quantidade de títulos (pizza)
                            dcc.Graph(
                                id="grafico-quantidade_cdas-pie"
                                )
                            ],
                    ),
                    width=6,
                ),
                #linha 8 coluna 2
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico composição da carteira por valor (pizza)
                            dcc.Graph(
                                id="grafico-saldo_cdas-pie"
                                )
                            ],
                    ),
                    width=6,
                ),
            ]
        ),
        #linha 9
        dbc.Row(
            [
                #linha 9 coluna 1
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        #Gráfico comparativo de situação das dívidas por tipo (barras)
                        children=[
                            dcc.Graph(
                                id="grafico-distribuicao_cdas-parallel"
                                )
                            ],
                    ),
                    width=6,
                ),
                #linha 9 coluna 2
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        #Gráfico superfície de concentração da dívida (3D)
                        children=[
                            dcc.Graph(
                                id="grafico-montante_acumulado_cdas-3d"
                                )
                            ],
                    ),
                    width=6,
                ),
            ]
        ),
        #linha 10
        dbc.Row(
            [
                #linha 10 coluna 1
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico curva de concentração de valor por natureza (line)
                            dcc.Graph(
                                id="grafico-montante_acumulado_cdas-line"
                                )
                            ],
                    ),
                    width=6,
                ),
                #linha 10 coluna 2
                dbc.Col(
                    html.Div(
                        className="chart-card",
                        children=[
                            #Gráfico mapa de calor da concentração de valor (heatmap)
                            dcc.Graph(
                                id="grafico-montante_acumulado_cdas-heatmap"
                                )
                        ],
                    ),
                    width=6,
                ),
            ]
        ),
    ]
)

#Layout para a página de busca
layout_busca = html.Div(
    [
        html.H2("Ferramenta de Busca de Dívidas", className="display-5 fw-bold mb-4"),
        dbc.Card(
            dbc.CardBody(
                [
                    #Linha 1 
                    dbc.Row(
                        [
                            #Coluna 1
                            dbc.Col(
                                [
                                    html.H5(
                                        "Filtros",
                                        className="mb-4 text-2xl font-extrabold leading-none tracking-tight text-gray-900 md:text-2xl lg:text-2xl dark:text-white",
                                    ),
                                    # Filtro por Natureza
                                    html.Div(
                                        [
                                            dbc.Label("Natureza da Dívida:"),
                                            dcc.Dropdown(
                                                #ID que salva o valor que será enviado para o callback_busca
                                                #Dependendo da opção selecionada, um valor diferente é passado
                                                id="filtro-natureza",
                                                options=[
                                                    {
                                                        "label": "IPTU",
                                                        "value": "IPTU"
                                                    },
                                                    {
                                                        "label": "ISS",
                                                        "value": "ISS"
                                                    },
                                                    {
                                                        "label": "ITBI",
                                                        "value": "ITBI"
                                                    },
                                                    {
                                                        "label": "Taxas",
                                                        "value": "Taxas",
                                                    },
                                                    {
                                                        "label": "Multas",
                                                        "value": "Multas",
                                                    },
                                                ],
                                                placeholder="Selecione uma natureza",
                                            ),
                                        ],
                                        className="mt-3 text-base text-gray-900 dark:text-white font-bold",
                                    ),
                                    # Filtro por Situação
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    dbc.Label("Situação da Dívida:"),
                                                ],
                                                className="mt-3 text-base text-gray-900 dark:text-white font-bold",
                                            ),
                                            dcc.Dropdown(
                                                #ID que salva o valor que será enviado para o callback_busca
                                                #Dependendo da opção selecionada, um valor diferente é passado
                                                id="filtro-agrupamento_situacao",
                                                options=[
                                                    {
                                                        "label": "Em cobrança",
                                                        "value": "em cobrança",
                                                    },
                                                    {
                                                        "label": "Quitada",
                                                        "value": "quitada",
                                                    },
                                                    {
                                                        "label": "Cancelada",
                                                        "value": "cancelada",
                                                    },
                                                ],
                                                placeholder="Selecione uma situação",
                                                className="text-base text-gray-900 dark:text-white font-bold",
                                            ),
                                        ]
                                    ),
                                    #Filtro por ano
                                    html.Div(
                                        [
                                            dbc.Label("Ano da Inscrição:"),
                                            dcc.Input(
                                                #ID que salva o valor que será enviado para o callback_busca
                                                # Quanto ao valor, ele depende, pq é um input e não um dropdown, então o usuario escreve em vez de selecionar
                                                id="filtro-ano",
                                                type="number",
                                                className="form-control mb-2",
                                            ),
                                        ],
                                        className="mt-3 text-base text-gray-900 dark:text-white font-bold",
                                    ),
                                ],
                                width=6,
                            ),
                            # Coluna 2
                            dbc.Col(
                                [
                                    html.H5(
                                        "Ordenação",
                                        className="mb-4 text-2xl font-extrabold leading-none tracking-tight text-gray-900 md:text-2xl lg:text-2xl dark:text-white",
                                    ),
                                    # Ordenar por
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    dbc.Label("Ordenar por:"),
                                                ],
                                                className="mt-3 text-base text-gray-900 dark:text-white font-bold",
                                            ),
                                            dcc.Dropdown(
                                                #ID que salva o valor que será enviado para o callback_busca
                                                #Dependendo da opção selecionada, um valor diferente é passado
                                                id="ordenar-por",
                                                options=[
                                                    {
                                                        "label": "Saldo da Dívida",
                                                        "value": "valor_saldo_atualizado",
                                                    },
                                                    {
                                                        "label": "Ano da Inscrição",
                                                        "value": "ano",
                                                    },
                                                    {
                                                        "label": "Score",
                                                        "value": "score",
                                                    },
                                                ],
                                                value="valor_saldo_atualizado",  # Valor padrão
                                                clearable=False,
                                            ),
                                        ]
                                    ),
                                    # Ordem
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    dbc.Label("Ordem:"),
                                                ],
                                                className="mt-3 text-base text-gray-900 dark:text-white font-bold",
                                            ),
                                            dcc.RadioItems(
                                                id="ordem",
                                                #ID que salva o valor que será enviado para o callback_busca
                                                #dependendo doq o usuário selecionar, um valor diferente é enviado
                                                options=[
                                                    {
                                                        "label": "Descendente",
                                                        "value": "desc",
                                                    },
                                                    {
                                                        "label": "Ascendente",
                                                        "value": "asc",
                                                    },
                                                ],
                                                value="desc",  # Valor padrão
                                                inline=True,
                                                labelStyle={"margin-right": "20px"},
                                            ),
                                        ]
                                    ),
                                ],
                                width=6,
                            ),
                        ]
                    ),
                    #linha 2
                    dbc.Row(
                        #coluna 1 e única
                        dbc.Col(
                            dbc.Button(
                                "Buscar",
                                #ID que salva o valor que será enviado para o callback_busca. O valor é n_clicks
                                id="botao-buscar",
                                color="primary",
                                className="mt-3",
                            ),
                            width={
                                "size": 6,
                                "offset": 3
                                },
                        ),
                        className="text-center",
                    ),
                ]
            ),
        ),
        # Div para a Tabela de Resultados
        html.Div(
            [
                html.H4("Resultados da Busca"),
                #Spinner é para a animação, aparece um simbolo loading
                dbc.Spinner(
                    #Componente dash para criar tabelas
                    dash_table.DataTable(
                        id="tabela-resultados-busca",
                        columns=[
                            {
                                "name": "CDA",
                                "id": "numCDA"
                            },
                            {
                                "name": "Ano",
                                "id": "ano"
                            },
                            {
                                "name": "Natureza",
                                "id": "natureza"
                            },
                            {
                                "name": "Valor (R$)",
                                "id": "valor_saldo_atualizado",
                                "type": "numeric",
                                "format": {"specifier": ",.2f"},
                            },
                            {
                                "name": "Score",
                                "id": "score",
                                "type": "numeric",
                                "format": {"specifier": ".2f"},
                            },
                            {
                                "name": "Situação",
                                "id": "agrupamento_situacao"
                            },
                        ],
                        #Quantidade de elementos em cada página
                        page_size=15,
                        #Personalização com css:
                        style_table={"overflowX": "auto"},
                        style_cell={"textAlign": "center"},
                        style_header={
                            "backgroundColor": "rgb(230, 230, 230)",
                            "fontWeight": "bold",
                        },
                    )
                ),
            ]
        ),
    ]
)


def create_layout():
    # Cria a estrutura completa da página, com a sidebar e o conteúdo.
    # Só vou comentar o que eu julgar necessário, a maioria é html e css (com Dash claro)
    # O que for um pouco mais diferente doq o simples html e css eu vou comentar uma vez,
    # não vou comentar em todas suas repetições não porque o comentário servira para todos
    sidebar = html.Div(
        className="sidebar",
        children=[
            html.Div(
                className="sidebar-header",
                children=[
                    html.Div(
                        style={
                            "background-color": "white",
                            "height": "70px",
                            "width": "70px",
                            "border-radius": "50%",
                            "margin-bottom": "10px",
                            "display": "inline-flex",
                            "justify-content": "center",
                            "align-items": "center",
                        },
                        children=[
                            html.Img(
                                src="/assets/lamdec.png",
                                style={"height": "60%"}
                                )
                        ],
                    ),
                    html.H1("Dívida Ativa", className="h3 fw-bold"),
                    html.P("Análise de Dados", className="small text-white-50 mt-1"),
                ],
            ),
            dbc.Nav(
                [
                    dbc.NavLink(
                        [
                            html.I(className="bi bi-house-door fs-5"), #esse daqui é para por icone, mas ainda n achei um bom. Talvez eu ponha se tiver tempo
                            html.Span("Início", className="ms-3"),
                        ],
                        #href é para onde será enviado ao clica nesse link. Quem controla isso é o dcc.location
                        href="/",
                        active="exact", #aplica estilo mais escuro para mostrar ao usuario onde ele está
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="bi bi-pie-chart fs-5"),
                            html.Span("Resumo", className="ms-3"),
                        ],
                        href="/resumo",
                        active="exact",
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="bi bi-pie-chart fs-5"),
                            html.Span("Painel Geral", className="ms-3"),
                        ],
                        href="/geral",
                        active="exact",
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="bi bi-search fs-5"),
                            html.Span("Ferramenta de Busca", className="ms-3"),
                        ],
                        href="/busca",
                        active="exact",
                    ),
                ],
                vertical=True, #Importante, por padrão fica tudo na horizontal, com isso eles ficam empilhados
                pills=False,  # Pills está adicionando um fundo azul horrivel e redondo, desativei pq vou arrumar com CSS
                className="sidebar-nav",
            ),
            html.Div(
                className="sidebar-footer",
                children=[
                    html.P(
                        "Desafio Técnico LAMDEC/UFRJ", className="small text-white-50"
                    )
                ],
            ),
        ],
    )

    content = html.Main(id="page-content", className="content")

    return html.Div(
        [
            #Ele que monitora o navegador. Quando a url muda ele muda a propriedade pathname para corresponder a URL. A gente utiliza ele como input no app.py
            dcc.Location(id="url", refresh=False),     # refresh=False deixa a pagina com navegação sem "bug" de loading, se não fica atualizando e fica estranho
            #armazena dados no navegador do usuario
            dcc.Store(id="store-dados-principais"),
            sidebar,
            content,
        ]
    )
