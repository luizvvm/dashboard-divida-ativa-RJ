# app.py

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, html

from layout import (
    create_layout,
    layout_inicio,
    layout_resumo,
    layout_geral,
    layout_busca,
)

#carregando alguns componentes de estilização externos
external_scripts = [{"src": "https://cdn.tailwindcss.com"}]
external_stylesheets = [
    dbc.themes.BOOTSTRAP,  # Para os componentes de grid (Row, Col) e botões
    "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
]

app = dash.Dash(
    __name__,
    external_scripts=external_scripts, 
    external_stylesheets=external_stylesheets, 
    suppress_callback_exceptions=True,  # para não causar erro ao receber callback de uma pagina que não seja a atual
)
server = app.server

#Função lá do "layout.py" que a gente usa pra criar o layout (autoexplicativo ne kkkkk)
app.layout = create_layout()

# Importa os callbacks para que sejam registrados aqui
import callbacks_graficos
import callbacks_busca


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")] #pega as mudanças na url capturadas pelo dcc.location() lá do "layout.py"
    )

#retorna a variavel do layout correspondente a pagina atual capturada pelo pathname
def render_page_content(pathname):
    if pathname == "/" or pathname == "/inicio":
        return layout_inicio
    elif pathname == "/resumo":
        return layout_resumo
    elif pathname == "/geral":
        return layout_geral
    elif pathname == "/busca":
        return layout_busca
    # Se a URL não for reconhecida, retorna uma mensagem de erro 404
    return html.Div(
        [
            html.H1("404: A página não encontrada", className="text-danger"),
            html.Hr(),
        ],
        className="p-3 bg-light rounded-3",
    )


# Bloco para rodar o servidor, segundo a documentação raramente isso muda, é um padrão no geral
if __name__ == "__main__":
    app.run(debug=True)
