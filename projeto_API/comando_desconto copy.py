import pandas as pd
import requests
import json

url_cod = 'ProjetoETL/Tabelas_de_precificacao/Precificacao_antes _do_desconto.csv'

df_product = pd.read_csv(url_cod, sep=';')
print(df_product)

df_dict = df_product.to_dict('records')
# print(df_dict)
print('')

df_dict = df_product.to_dict('index')
# print(df_dict)

for indice in df_dict:
    print(indice, df_dict[indice])

print(df_dict)
