import pandas as pd

# Definición diccionario:
#diccionario = {'pares': [0, 2, 4, 6], 'impares': [1, 3, 5, 7]}

# Creación DataFrame:
#df_numeros = pd.DataFrame(diccionario)
df_numeros = pd.read_csv('numeros.csv',";")
# Guarda datos en CSV:
#df_numeros.to_csv('numeros.csv', header=True, index=False, sep=';')
print(df_numeros)