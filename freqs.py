from etl import getData
import pandas as pd
import labels
# from pretty_html_table import build_table
import matplotlib.pyplot as plt


def label_values(d,labels):
    return {labels[k] : v for k,v in sorted(d.items())}

df = getData()

tables_html = []

for D in ['D1','D2a','D3','D4a','D5','D6','D7','D8','D9','D10','D11','D12','D13']: # ,'D3','D4a','D5','D6','D7','D8','D9','D10','D11','D12','D13']:
#for D in ['D2a']: # ,'D2a','D2b','D2c','D3','D4a','D4b','D4c','D5','D6','D7','D8','D9','D10','D11','D12','D13']: # ,'D3','D4a','D5','D6','D7','D8','D9','D10','D11','D12','D13']:
    data = df[D]
    data = data.apply(lambda x: labels.risposte[D][x])
    freqs = data.value_counts()
    percent100 = data.value_counts(normalize=True)
    stat = pd.DataFrame({'#': freqs, '100%': percent100})
    stat.sort_values(by=['#'], inplace=True, ascending=False)

    def ff(x):
        return ' {:<8.2%}'.format(x)
    
    img_file = f'{D}.jpg'
    
    table = stat.to_html(float_format=ff)
    tables_html.append(f'''
        <DIV class="testo_domanda">{labels.domande[D]}
        </DIV>
        <DIV style="float:left; display:block;">
           {table}
        </DIV>
        <DIV style="float:left;" > <IMG src='{img_file}'> </DIV>
        <div style="clear:both;"></div> 
    ''')
    labels_ = freqs.keys().tolist()
    plt.figure()

    freqs.loc[~freqs.index.isin(['Non risponde'])].plot.pie(y='#',textprops={'size': 'smaller'},autopct='%1.1f%%', shadow=True)
    plt.ylabel("")
    plt.savefig(f'./public/{img_file}')
    plt.close()

    with open(f'./public/Frequenze.html','w') as f:
        styles = '''
        table.dataframe > tbody > tr > th {
            text-align: left;
        }

        table.dataframe > tbody > tr > td {
            text-align: right;
        }


        .testo_domanda {
            margin-top: 20px;
            margin-bottom: 10px;
            color: blue;
            font-family: sans-serif;
            font-style: normal;
            font-variant: normal;
            font-weight: bold;
            font-size: large;
            line-height: 100%;
            word-spacing: normal;
            letter-spacing: normal;
            text-decoration: none;
            text-transform: none;
            text-align: left;
            text-indent: 0ex;
        }

        '''

        html_string = f'''
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Frequenze semplici risposte</title>
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