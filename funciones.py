import pandas as pd
import numpy as np
import os
import requests
import re

def hash_function(cod,key):
    a = cod
    b = str(abs(hash(key)))[0:4:1]

    c = f'{a}{b}'
    return c

def arreglar_neuquen(elemento_df, reemplazo='Neuquén'):
    if re.findall('Neuqu.n', elemento_df):
        elemento_df = reemplazo
    return elemento_df

def cine_redux(dataframe):
    
    df = {
        'provincia': [],
        'butacas': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'pantallas': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'espacio_INCAA': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    }

    for i in dataframe.index:

        if dataframe['provincia'][i] not in df['provincia']:
            df['provincia'].append(dataframe['provincia'][i])
            
        df['butacas'][df['provincia'].index(dataframe['provincia'][i])] += dataframe['Butacas'][i]
        df['pantallas'][df['provincia'].index(dataframe['provincia'][i])] += dataframe['Pantallas'][i]
        df['espacio_INCAA'][df['provincia'].index(dataframe['provincia'][i])] += dataframe['espacio_INCAA'][i]
    

    return pd.DataFrame(df)