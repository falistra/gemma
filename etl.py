# -*- coding: utf-8 -*-
import pandas as pd
import labels

def getData():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSe8__fQMlVJUIHbq0ZhmFRRKPciwpyn2143rwuVfQLAunZxw1JnAweUB9_j2xhPNGCDyLnZ9GOcQh6/pub?gid=0&single=true&output=csv"
    df = pd.read_csv(url)
    df = df.astype({
        "D1": pd.Int16Dtype(),
        "Flag" : '|S',
        "D1a": pd.Int16Dtype(),
        "D2a": pd.Int16Dtype(),
        "D2b": pd.Int16Dtype(),
        "D2c": pd.Int16Dtype(),
        "D3": pd.Int16Dtype(),
        "D4a": pd.Int16Dtype(),
        "D4b": pd.Int16Dtype(),
        "D4c": pd.Int16Dtype(),
        "D5": pd.Int16Dtype(),
        "D6": pd.Int16Dtype(),
        "D7": pd.Int16Dtype(),
        "D8": pd.Int16Dtype(),
        "D9": pd.Int16Dtype(),
        "D10": pd.Int16Dtype(),
        "D11": pd.Int16Dtype(),
        "D12": pd.Int16Dtype(),
        "D13": pd.Int16Dtype()
        })

#    df.rename(columns = labels.domande, 
#        inplace = True)

    # print(df.info())
    return df

if __name__ == "__main__":
    df = getData()