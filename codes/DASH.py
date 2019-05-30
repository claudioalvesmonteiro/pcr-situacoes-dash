import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

import datetime 


'''
df = pd.read_csv('http://dados.recife.pe.gov.br/dataset/99eea78a-1bd9-4b87-95b8-7e7bae8f64d4/resource/9afa68cf-7fd9-4735-b157-e23da873fef7/download/156diario.csv',
                sep = ';',
                header = 0,
                encoding = 'utf-8',
                error_bad_lines=False)
'''

df = pd.read_csv('data/sedecsolicitadfcoes.csv', sep = ';', header = 0, encoding = 'utf-8', error_bad_lines=False)

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

tipo = 'Numero Total de Solicitacoes por dia'

app = dash.Dash()

#----------- BODY
app.layout = html.Div(children =[

    html.Div(children='''Dash tutorials'''),

    dcc.Graph(id='example-graph',
                figure={
                    'data': [
                        {'x': dt.date, 'y': dt.n_solicitacao, 'type': 'line', 'name': tipo},
                    ],
                    'layout': {
                        'title': tipo
                    }
                }
    )


])

if __name__ == '__main__':
    app.run_server(debug=True)
