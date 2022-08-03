from etl import getData
import pandas as pd
import labels

import matplotlib.pyplot as plt

from scipy.stats import chi2_contingency
import seaborn as sns

def label_values(d,labels):
    return {labels[k] : v for k,v in sorted(d.items())}

df = getData()

def ff(x):
    return '{}%'.format(round(x,2))

analytics = open('./public/analytics.html','w',encoding='utf-8')
analytics.write("""
<meta charset="UTF-8">
Fra le seguenti coppie di domande <B>può essere rifiutata l'ipotesi di indipendenza H0</B> <BR/>
A favore dell'ipotesi alternativa di un legame, <BR/>
con una probabilità  di commettere errore minore di...
<HR>
""")

#for var_riga in ['D5','D6','D7','D8']:
#    for var_col in ['D2a','D3','D4a','D9','D10','D11','D12','D13']:

for var_riga in ['D5','D6','D7','D8','D2a','D3','D4a','D9','D10','D11','D12','D13']:
    for var_col in ['D5','D6','D7','D8','D2a','D3','D4a','D9','D10','D11','D12','D13']:
        if var_col == var_riga:
            continue

        tables_html = []

        valori_assoluti = pd.crosstab(df[var_riga], df[var_col],margins=True,margins_name='Totale')
        valori_assoluti.rename(columns=labels.risposte[var_col], index=labels.risposte[var_riga], inplace = True)
        #print(valori_assoluti)
        #print()
        table_valori_assoluti = valori_assoluti.to_html(float_format=ff)

        pct_totale = pd.crosstab(df[var_riga], df[var_col], normalize='all',margins=True, margins_name='Totale').round(4)*100
        pct_totale.rename(columns=labels.risposte[var_col], index=labels.risposte[var_riga], inplace = True)
        table_pct_totale = pct_totale.to_html(float_format=ff)

        pct_colonna = pd.crosstab(df[var_riga], df[var_col], normalize='columns',margins=True, margins_name='%% riga').round(4)*100
        pct_colonna.rename(columns=labels.risposte[var_col], index=labels.risposte[var_riga], inplace = True)
        table_pct_colonna = pct_colonna.to_html(float_format=ff)

        pct_riga = pd.crosstab(df[var_riga], df[var_col], normalize='index',margins=True, margins_name='%% colonna').round(4)*100
        pct_riga.rename(columns=labels.risposte[var_col], index=labels.risposte[var_riga], inplace = True)
        table_pct_riga = pct_riga.to_html(float_format=ff)
        
        img_file = f'{var_riga}_X_{var_col}.png'
        plt.figure(figsize=(6,4)) 
        valori_assoluti_graph = pd.crosstab(df[var_riga], df[var_col])
        valori_assoluti_graph.rename(columns=labels.risposte_short[var_col], index=labels.risposte_short[var_riga], inplace = True)
        sns.heatmap(valori_assoluti_graph, annot=True, cmap="YlGnBu")
        plt.savefig(f'./public/incroci/{img_file}')
        plt.close()

        # Chi-square test of independence. 
        c, p, dof, expected = chi2_contingency(valori_assoluti_graph)
        if p < 0.10:
            non = ''
            msg = f'''
            {p:0.2} - "{labels.domande[var_riga]} ({var_riga})" <=> "{labels.domande[var_col]} ({var_col})"
            <BR/>
            '''
            analytics.write(msg)

        else:
            non = 'non'
        giudizio = f'{non} può essere rifiutata' 
        # Print the p-value
        # print(p)

               
        tables_html.append(f'''
            Frequenze incrociate tra domande:<BR/>
            <DIV class="testo_domanda">
            "{labels.domande[var_riga]} ({var_riga})" ❌ "{labels.domande[var_col]} ({var_col})"
            </DIV>
            <div class="caption_table"> Valori assoluti </div>
            <div>{table_valori_assoluti}</DIV>
            <DIV> <IMG src="{img_file}"> </DIV>
            <div class="caption_table"> Percentuali sul totale </div>
            <div>{table_pct_totale}</DIV>
            <div class="caption_table"> Percentuali di colonna </div>
            <div>{table_pct_colonna}</DIV>
            <div class="caption_table"> Percentuali di riga </div>
            <div>{table_pct_riga}</DIV>
            <div id="chiquadro">
            Test di indipendenza 𝛘².<BR/>
            Probabilitá di ipotesi di indipendenza tra le due variabili (H0):  {p:0.2}.<BR/>
            "{labels.domande[var_riga]} ({var_riga})" ❌ "{labels.domande[var_col]} ({var_col})": <BR/>
            L'ipotesi (H0) <span id="non">{giudizio}</span>.</BR>:
            <span id="non">{non}</span> si può sostenere una legame di dipendenza fra loro.
            </div>
        ''')

        with open(f'./public/incroci/{labels.domande[var_riga]}_X_{labels.domande[var_col]}.html','w') as f:
            styles = '''
            table.dataframe > tbody > tr > th {
                text-align: left;
            }

            table.dataframe > tbody > tr > td {
                text-align: right;
            }

            .caption_table {
                margin-top: 15px;
                font-family: verdana;
                font-weight: bold;
            }

            .testo_domanda {
                margin-top: 20px;
                margin-bottom: 10px;
                color: blue;
                font-family: sans-serif;
                font-style: normal;
                font-variant: normal;
                font-weight: bold;
                font-size: x-large;
                line-height: 100%;
                word-spacing: normal;
                letter-spacing: normal;
                text-decoration: none;
                text-transform: none;
                text-align: left;
                text-indent: 0ex;
            }

            div#chiquadro {
                width: 700px;
                margin-top: 20px;
                border: solid 2px red;
                color: black;
                font-family: verdana;
                font-style: normal;
                font-variant: normal;
                font-weight: normal;
            }

            span#non {
                color: red;
                font-variant: large;
            }

            '''

            html_string = f'''
            <html>
            <head>
                <meta charset="UTF-8">
                <title>{var_riga} X {var_col} </title>
                <style>
                {styles}
                </style>

            </head>
            <body>
                {'<HR>'.join(tables_html)}
            </body>
            </html>
            '''
        
            f.write(html_string)