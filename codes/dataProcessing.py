'''
collect data from PCR source

compares to local database
    - time of situacao PENDENTE, PREPARACAO, EXECUCAO, CADASTRADA, ATENDIDA, SITUACAO 
    - TIME IN 15 MINUTES
    - FLOW OF SITUATIONS
    - date on data X date captured
'''

# FALAR COM PESSOAL DO IFPE PRA GERAR UM COLETOR E ARMAZENAR 

# GENERATE KEY FOR SITUATIONS

df = pd.read_csv('data/156diario.csv', sep = ';', header = 0, encoding = 'utf-8', error_bad_lines=False)
df = pd.read_csv('data/sedecsolicitadfcoes.csv', sep = ';', header = 0, encoding = 'utf-8', error_bad_lines=False)

df['solicitacao_date']  =  pd.to_datetime(df['solicitacao_data'], format='%Y-%m-%d')

sol_dt = df.groupby('solicitacao_date').count()
