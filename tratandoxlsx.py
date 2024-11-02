import pandas as pd

arquivo_xlsx = ('original.xlsx')
df = pd.read_excel(arquivo_xlsx)

##print(df)
##print(df.info())

df_limpo = df.dropna(how='all')

df_limpo['CD_CNAE'] = df_limpo['CD_CNAE'].str.replace(r'[-/]', '', regex=True)
df_limpo['ECONOMIA VERDE'] = df_limpo['ECONOMIA VERDE'].str.replace(r'[\[\]]', '', regex=True)


print(df_limpo)

df_limpo.to_excel('tratado.xlsx', index=False)