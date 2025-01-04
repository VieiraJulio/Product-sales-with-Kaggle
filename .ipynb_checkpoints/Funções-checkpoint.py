#Autoria de Julio Vieira, caso ultilize dê os créditos. 

import pandas as pd

def reset_index_from_one(df, drop=False):
    """
    Redefine o índice do DataFrame começando a partir de 1.
    
    Parâmetros:
        df (pd.DataFrame): O DataFrame a ser ajustado.
        drop (bool): Se True, descarta o índice antigo. 
                     Se False, mantém o índice antigo como uma coluna.
                     
    Retorna:
        pd.DataFrame: O DataFrame com índice reiniciado a partir de 1.
    """
    df_reset = df.reset_index(drop=drop)
    df_reset.index = range(1, (len(df_reset) + 1))
    return df_reset

# Exemplo de uso
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['x', 'y', 'z'])

# Aplicando a função
df_adjusted = reset_index_from_one(df, drop=True)
print(df_adjusted)
