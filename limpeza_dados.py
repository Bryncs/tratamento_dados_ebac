import pandas as pd

df = pd.read_csv('clientes.csv')

pd.set_option('display.width', None)
print(df.head())

# Remover dados
df.drop('pais', axis=1, inplace=True) # coluna
df.drop(2, axis=0, inplace=True)

# Normalizar campos de texto
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()

# Converter tipos de dados
df['idade'] = df['idade'].astype(int)

# Tratar valores nulos (ausentes)
df_fillna = df.fillna(0) # Substituir valores nulos por 0
df_dropna = df.dropna() # Remover registros com valores nulos
df_dropna4 = df.dropna(thresh=4) # Manter registros com no minimo 4 valores não nulos
df = df.dropna(subset=['cpf'])

print('Valores nulos:\n', df.isnull().sum())
print('Qtd de registros nulos com fillna:', df_fillna.isnull().sum().sum())
print('Qtd de registros nulos com dropna:', df_dropna.isnull().sum().sum())
print('Qtd de registros nulos com dropna4:', df_dropna4.isnull().sum().sum())
print('Qtd de registros nulos com cpf:', df.isnull().sum().sum())

df.fillna({'estado': 'Desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('Endereço não informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

# Tratar formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

# Tratar dados duplicados
print('Qtd registros atual:', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print('Qtd registros removendo as duplicadas:', len(df))

print('Dados Limpos:\n', df)

# Salvar dataframe
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('Novo Dataframe: \n', pd.read_csv('clientes_limpeza.csv'))
