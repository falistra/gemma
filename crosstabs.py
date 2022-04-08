from etl import getData
import pandas as pd
import labels

def label_values(d,labels):
    return {labels[k] : v for k,v in sorted(d.items())}

df = getData()

D6_X_D7 = pd.crosstab(df['D6'], df['D7'],margins=True,margins_name='Totale')
print(D6_X_D7)
print()
D6_X_D7_pct = pd.crosstab(df['D6'], df['D7'], normalize='all',margins=True, margins_name='Totale').round(4)*100
print(D6_X_D7_pct.rename(columns=labels.risposte['D7']))
print()
D6_X_D7_pct = pd.crosstab(df['D6'], df['D7'], normalize='columns',margins=True, margins_name='%% riga').round(4)*100
print(D6_X_D7_pct.rename(columns=labels.risposte['D7']))
print()
D6_X_D7_pct = pd.crosstab(df['D6'], df['D7'], normalize='index',margins=True, margins_name='%% colonna').round(4)*100
print(D6_X_D7_pct.rename(columns=labels.risposte['D7']))