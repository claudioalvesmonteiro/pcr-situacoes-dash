import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

import datetime 

# DROPDOWN: https://pbpython.com/plotly-dash-intro.html

'''
df = pd.read_csv('http://dados.recife.pe.gov.br/dataset/99eea78a-1bd9-4b87-95b8-7e7bae8f64d4/resource/9afa68cf-7fd9-4735-b157-e23da873fef7/download/156diario.csv',
                sep = ';',
                header = 0,
                encoding = 'utf-8',
                error_bad_lines=False)
'''

df = pd.read_csv('https://raw.githubusercontent.com/claudioalvesmonteiro/pcr-situacoes-dash/master/data/sedecsolicitacoes.csv', sep = ';', header = 0, encoding = 'utf-8', error_bad_lines=False)

df['solicitacao_date']  =  pd.to_datetime(df['solicitacao_data'], format='%Y-%m-%d')

# count 'solicitacao' by date
dt = pd.DataFrame(df['solicitacao_date'].value_counts())

# reset index and rename columns
dt.reset_index(inplace=True)
dt.columns = ['date', 'n_solicitacao']

# order by date
dt.sort_values(by='date', inplace=True, ascending=False)

#==========================#
# APPLICATION
#========================#

tipo = 'Número Total de Solicitações por dia'

app = dash.Dash()

# type of solicitation
sol = ['teste1', 'teste2']


'''
html.Div(children='symbol do graph:'),
dcc.Input(id='input', value='', type='text'),
html.Div(id='output-graph')
'''

#----------- BODY
app.layout = html.Div([
    html.H2("Solicitações na Prefeitura do Recife"),
    html.Div([
            dcc.Dropdown(
                id="input",
                options=[{
                    'label': i,
                    'value': i
                } for i in sol],
                value='All Managers'), ],

        style={'width': '25%',
               'display': 'inline-block'}),
    html.Div(id='output-graph')
])


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)

def update_graph(input_data):

        return dcc.Graph(id='example-graph',
                figure={
                    'data': [
                        {'x': dt.date, 'y': dt.n_solicitacao, 'type': 'line', 'name': tipo},
                    ],
                    'layout': {
                        'title': tipo,
                        'type': 'date',
                        'tickformat': '%M:%Y'
                    }
                }
    )
    


if __name__ == '__main__':
    app.run_server(debug=True)


