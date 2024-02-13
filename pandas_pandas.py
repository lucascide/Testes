# Conversão de um dicionario para df:

import pandas as pd

df=pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})


# Para imprimir colunas especificas:

df['a']

# Para imprimir linhas que estabelecem a uma condição:

df.iloc[("a" > 15)]  #ou
df[df["a"] > 15]


# Para alterar uma coluna específica de linhas que obedecem a uma condição:

df.iloc[("a" > 15), ["b"]] = 90


# Para achar valores unicos de uma coluna

df["a"].unique()
