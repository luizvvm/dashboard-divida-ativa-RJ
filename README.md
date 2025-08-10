# Desafio Técnico LAMDEC/UFRJ: Dashboard de Análise da Dívida Ativa

Este repositório contém a solução para o Desafio Técnico proposto pelo Laboratório de Métodos de Suporte à Tomada de Decisão (LAMDEC) do Instituto de Matemática da UFRJ, como parte do processo seletivo para uma vaga de Iniciação Científica no projeto "Reconciliação de Dados".

O objetivo do desafio era construir uma aplicação web de um dashboard, consistindo em uma API para servir dados e um dashboard interativo para visualizar e analisar informações sobre a Dívida Ativa do Município do Rio de Janeiro.

## O Dashboard
O projeto aqui desenvolvido busca fornecer insights valiosos sobre a carteira de dívidas da PGM-Rio.

### Principais Funcionalidades
- **API Robusta**: Backend em FastAPI que serve dados a partir de arquivos JSON com:
  - Endpoints para dados resumidos;
  - Ferramenta de busca (`/cda/search`).
- **Páginas Modulares**:
  - **Início**: Apresentação do projeto e análises iniciais com gráficos dos dados gerais do endpoint (`search`);
  - **Resumo**: Outras análises com gráficos dos dados do endpoint (`resumo`);
  - **Painel Geral**: Todos os gráficos resumidos em um só lugar;
  - **Ferramenta de Busca**: Interface para filtrar, ordenar e consultar os dados do endpoint (`search`).

## Tecnologias Utilizadas
**Backend**:
- Python;
- FastAPI;
- Uvicorn.

**Frontend**:
- Dash;
- Plotly;
- Dash Bootstrap Components;
- Pandas.

**Análise de Dados**:
- Pandas;
- NumPy.

**Organização**
- Usei "Black" para identar o código. Se quiser as versões sem identação bonitinha, acesse o último commit do dia 09/10/2025.

### Passos de Execução:
1. **Backend**
Da pasta raiz do projeto, abra um terminal para rodar o servidor:
```bash
# Navegue até a pasta do backend
cd backend

# Crie e ative o ambiente virtual (Windows)
python -m venv venv
.\venv\Scripts\activate

# Instale os requerimentos
pip install -r requirements.txt

# Inicie o servidor
python -m uvicorn main:app --reload
```
O servidor estará rodando em algo parecido com http://127.0.0.1:8000. Mantenha este terminal aberto.

2. **Frontend**
Abra um segundo terminal enquanto o primeiro está rodando (não feche o primeiro) e volte a pasta raiz d projeto:
```bash
# Navegue até a pasta do frontend
cd frontend

# Inicie a aplicação
python app.py
```
Dai basta acessar a url indicada no terminal.

### O que eu fiz para construir o projeto:

Esse projeto foi muito enriquecedor para mim porque, durante ele, li muita documentação e aprendi muitas coisas novas. Eu iniciei o desafio lendo a documentação:
[FastAPI](https://fastapi.tiangolo.com/pt/tutorial/first-steps/)
Na qual eu aprendi sobre:

- Endpoints e Roteamento com decoradores (`@app.get(...)`)
- A diferença entre Path Parameters (`/resumo/{arquivo}`) para recursos específicos e Query Parameters (`/search?ano=2020`) para filtros flexíveis
- Como iniciar o servidor com o comando `uvicorn`

Dai eu fiz a API no primeiro dia. Já no segundo dia o foco mudou para a construção do frontend.

**Pro Layout e Estilização**: Tive que estudar mais sobre Dash Bootstrap Components para criar um layout mais profissional rapidamente. Um grande aprendizado foi a "guerra de estilos": entendi que frameworks de CSS como Bootstrap e Tailwind não se misturam por padrão, mas tinha eu estava mais acostumado a usar o Tailwind, então você verá alguns elementos estilizados com ele e outros não.

**Callbacks e Reatividade**: Esse foi o aprendizado mais importante para desenvolver esse projeto. Aprendi o conceito de Input -> Output lendo a documentação do dash e, mais crucialmente, a diferença entre Input (o gatilho que dispara o callback) e State (a informação extra que é "lida" no momento do disparo). Este conceito foi a luz para mim fazer a ferramenta de busca com um botão "Buscar" que funciona.

**Os gráficos**: Fiz todos os gráficos seguindo a risca os tutoriais do plotly, que alias são muito bons, alguns gráficos mais simples eu já tinha o costume e já sabia fazer, então foi mais tranquilo, mas alguns outros gráficos eu tive que aprender a fazer pela a documentação, o que não foi dificil sinceramente. Todos os gráficos feitos com plotly.express foram bem faceis de fazer pela documentação, já os feitos pelo Plotly Express eu confeço que tive dificuldades, pois ainda não tenho muito familiaridade com essa técnologia, mas como foi só seguir a documentação eu consegui fazer também.

**Maior desafio: Performance com dcc.Store**: Depois de ter feitos os gráficos usando plotly, percebi que eu fiz cada gráfico fazer uma chamada à API, tornando o dashboard meio lento e bem propenso a erros de carregamento. A solução foi carregar todos os dados necessários da API uma única vez na inicialização e armazená-los em um `dcc.Store` no navegador do cliente. Os callbacks dos gráficos passaram a ler deste "armazém" local. Para essa parte eu precisei recorrer a IA para entender como eu poderia otimizar o dashboard.

#### Links Úteis

- [FastAPI](https://fastapi.tiangolo.com/)
- [Documentação do Dash](https://dash.plotly.com/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
- [Gráficos Plotly](https://plotly.com/python/)
- [Estilização com bootstrap](https://getbootstrap.com/docs/5.3/content/images/)
- [Estilização com Flowbite](https://flowbite.com/docs/getting-started/introduction/)

#### Agradecimentos

Gostei muito de fazer esse projeto e agora tenho ainda mais certeza de que é essa a área que eu quero para minha carreira. Vou concentrar meus esforços em aprender cada vez mais sobre plotly e dash.
Agradeço imensamente ao LAMDEC/UFRJ pela oportunidade de participar deste desafio.