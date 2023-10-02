import pandas as pd
import requests
import json

url_cod = 'C:\Repositórios Git\python-dio\projeto_API\produts.csv'

df = pd.read_csv(url_cod, sep=';')
# print(df)
cod_prod = df[' Produto'].tolist()
print(cod_prod)
