from etl import getData
import pandas as pd
import labels

import matplotlib.pyplot as plt
import seaborn as sns

import collections

def ff(x):
    return ' {:<8.2%}'.format(x)


df = getData()

def wrangling(D,words):
    print(f"Domanda {D} - {labels.domande[D]}")
    data = []

    if words:
        for (text,desc) in words:
            df_text = df.loc[df[D].str.contains(text) == True]
            data.append((desc,len(df_text)))

    stat = pd.DataFrame(data, columns =['Risposta', '#'],index=[d for (_,d) in words])
    stat['percent'] = (stat['#'] / stat['#'].sum()) #  * 100
    stat.sort_values(by=['#'], inplace=True, ascending=False)
    table = stat.to_html(index=False,float_format=ff)

    img_file = f'{D}.jpg'

    try:
        plt.figure()
        stat.plot.pie(y='#', textprops={'size': 'smaller'},autopct='%1.1f%%', shadow=True)
        plt.ylabel("")
        plt.savefig(f'./public/domande aperte/{img_file}')
        plt.close()
    except:
        pass

    df_validi = df[D].dropna()
    freqs = df_validi.value_counts()
    freqs.sort_values(inplace=True, ascending=False)
    stat_freq = pd.DataFrame({'#': freqs})
    stat_freq.index.name='Testo risposta data'
    table_freq = stat_freq.to_html(float_format=ff)

#    print(collections.Counter(df_validi).most_common())
#    print(f"Numero di risposte valide: {len(df_validi)}")


    table_html = f'''
        <DIV class="testo_domanda">{labels.domande[D]}
        </DIV>
        <DIV style="float:left; display:block;">
           {table}
        </DIV>
        <DIV style="float:left;" > <IMG src='{img_file}'> </DIV>
        <div style="clear:both;"></div> 
    '''
    return (table_html,table_freq)

words = {
    'D14': [
        ('riscal',"Riscaldamento globale"),
        ('covid',"Covid"),
        ('clima',"Clima"),
        ('onfin',"Confini"),
        ("monte","Monte Bianco")
    ],
    'D15': [
        ('tropoc',"Antropocene"),
        ('onfin',"Confini"),
        ('obil',"Mobilità"),
        ("ovid","Covid"),
        ('lima',"Clima"),
        ('rtic','Artico'),
        ('imit','Limite'),
        ('atura','Natura'),
        ('arola','Parola')
    ],
    'D16': [

    ]}

for D in ['D14','D15','D16']: # ,'D15','D16']:
    with open(f'./public/domande aperte/{labels.domande[D]}.html','w') as f:
        
        (table_html,table_freq) = wrangling(D,words[D])
        
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
            <title>{D} </title>
            <style>
            {styles}
            </style>

        </head>
        <body>
            {table_html}
            <HR>
            {table_freq}
        </body>
        </html>
        '''
    
        f.write(html_string)


