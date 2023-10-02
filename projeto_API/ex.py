import pandas as pd
import requests
import json

url_cod = 'C:\Repositórios Git\python-dio\projeto_API\produts.csv'

df = pd.read_csv(url_cod, sep=';')
print(df)

df.loc[
    [' Categoria'] == " Secos",' Valor_Kg'] -= df.loc[df[' Categoria'] == " Secos",' Valor_Kg'
    ] * 0.5

print(df)

# df.to_csv('AiPapai.csv', index=False)

