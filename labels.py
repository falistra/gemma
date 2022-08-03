import pandas as pd
domande = {
    'D1':   'È la prima volta che visita il Museo Universitario Gemma?', 
    'D2a' : 'Come ne è venuto a conoscenza? (I risposta)',
    'D2b':  'Come ne è venuto a conoscenza? (II risposta)',
    'D2c':  'Come ne è venuto a conoscenza? (III risposta)',
    'D2Altro':  'Come ne è venuto a conoscenza? (Altro)',
    'D3' : 'Con chi ha visitato il Museo?',
    'D4a' : 'Per quale motivo ha visitato il Museo? (I risposta)',
    'D4b' : 'Per quale motivo ha visitato il Museo? (II risposta)',
    'D4c' : 'Per quale motivo ha visitato il Museo? (III risposta)',
    'D5' : 'Dove abita?',
    'D6':   'Sesso',
    'D7':   'Età',
    'D8' : 'Qual è il suo titolo di studio?',
    'D9' : 'Quanto tempo è durata la visita alla mostra CONFINI?',
    'D10' : 'In generale è soddisfatto della visita?',
    'D11' : 'Se ha avuto modo di seguire una visita guidata alla mostra, come si ritiene soddisfatto del percorso mostra ?',
    'D12' : 'Se ha avuto modo di seguire una visita guidata alla mostra, come si ritiene soddisfatto della visita guidata ?',
    'D13' : 'Se ha avuto modo di seguire una visita guidata alla mostra, come si ritiene soddisfatto della cortesia e competenza del personale ?',
    'D14' : 'Quale è il tema della mostra CONFINI che ha trovato di maggior interesse',
    'D15' : 'Quale è il tema parola chiave della mostra CONFINI che è rimasto più impresso',
    'D16' : 'Altre osservazioni e suggerimenti'
    }

risposte = {
    'D1':   {1:"Sì",2:"No","All":'Totale', pd.NA:"Non risponde"},
    'D2a' : {
        1:'Da mio figlio/a, nipote',
        2: 'Da amici/parenti',
        3: 'Attraverso Internet',
        4: 'Da un pieghevole/locandina',
        5: 'Da un articolo su una rivista/giornale',
        6: 'Dalla radio/TV ',
        7: 'Casualmente, passando davanti al Museo',
        8: 'Conoscevo già il Museo',
        9: 'Altro ',
        pd.NA:"Non risponde"
        },
    'D2b' : {
        1:'Da mio figlio/a, nipote',
        2: 'Da amici/parenti',
        3: 'Attraverso Internet',
        4: 'Da un pieghevole/locandina',
        5: 'Da un articolo su una rivista/giornale',
        6: 'Dalla radio/TV ',
        7: 'Casualmente, passando davanti al Museo',
        8: 'Conoscevo già il Museo',
        9: 'Altro ',
        pd.NA:"Non risponde"
        },
    'D2c' : {
        1:'Da mio figlio/a, nipote',
        2: 'Da amici/parenti',
        3: 'Attraverso Internet',
        4: 'Da un pieghevole/locandina',
        5: 'Da un articolo su una rivista/giornale',
        6: 'Dalla radio/TV ',
        7: 'Casualmente, passando davanti al Museo',
        8: 'Conoscevo già il Museo',
        9: 'Altro ',
        pd.NA:"Non risponde"
        },
    'D3' :  {
        1: 'In gruppo organizzato',
        2: 'Da solo',
        3: 'In coppia',
        4: 'Con figli/nipoti',
        5: 'Con parenti/amici',
        pd.NA:"Non risponde"
    },
    'D4a' :  {
        1: 'Interesse specifico sulla raccolta',
        2: 'Come parte di una visita turistica nella zona/città',
        3: 'Interesse di studio/professionale',
        4: 'Per accompagnare amici/conoscenti',
        5: 'Per visitare una mostra o partecipare ad una iniziativa in corso',
        6: 'Per trascorrere del tempo libero',
        7: 'Docente di una classe in visita',
        9: 'Altro',
        pd.NA:"Non risponde"
    },
    'D4b' :  {
        1: 'Interesse specifico sulla raccolta',
        2: 'Come parte di una visita turistica nella zona/città',
        3: 'Interesse di studio/professionale',
        4: 'Per accompagnare amici/conoscenti',
        5: 'Per visitare una mostra o partecipare ad una iniziativa in corso',
        6: 'Per trascorrere del tempo libero',
        7: 'Docente di una classe in visita',
        9: 'Altro',
        pd.NA:"Non risponde"
    },
    'D4c' :  {
        1: 'Interesse specifico sulla raccolta',
        2: 'Come parte di una visita turistica nella zona/città',
        3: 'Interesse di studio/professionale',
        4: 'Per accompagnare amici/conoscenti',
        5: 'Per visitare una mostra o partecipare ad una iniziativa in corso',
        6: 'Per trascorrere del tempo libero',
        7: 'Docente di una classe in visita',
        9: 'Altro',
        pd.NA:"Non risponde"
    },
    'D5' :  {
        1:'In questa provincia',
        2:'In Italia (indicare la provincia)',
        3:'All’estero',
        pd.NA:"Non risponde"
    },
    'D6':   {
        1:"Maschio",
        2:"Femmina",
        3:"Femmina",
        "All":'Totale', 
        pd.NA:"Non risponde"
    },
    'D7':   {
        1:"Meno di 18",
        2:"Tra 18 e 30",
        3:"Tra 31 e 45",
        4:"Tra 46 e 65",
        5:"Più di 65",
        "All":'Totale',
        pd.NA:"Non risponde"
    }, 
    'D8' : {
    1: 'Elementare',
    2: 'Medie inferiori',
    3: 'Diploma medie superiori',
    4: 'Laurea o titoli post-laurea',
    5: 'Nessuno',
    pd.NA:"Non risponde"
    },
    'D9' : {
    1:'Meno di 30 minuti',
    2:'Da 30 minuti a 1 ora',
    3:'Da 1 a 2 ore',
    4:'Più di 2 ore',
    pd.NA:"Non risponde"  
    },
    'D10' : {
    1:'Per niente',
    2:'Poco',
    3:'Abbastanza',
    4:'Molto',
    pd.NA:"Non risponde"
    },
    'D11': {
    1:'Per niente',
    2:'Poco',
    3:'Abbastanza',
    4:'Molto',
    pd.NA:"Non risponde"
    },
    'D12': {
    1:'Per niente',
    2:'Poco',
    3:'Abbastanza',
    4:'Molto',
    pd.NA:"Non risponde"
    },
    'D13': {
    1:'Per niente',
    2:'Poco',
    3:'Abbastanza',
    4:'Molto',
    pd.NA:"Non risponde"
    }
}

risposte_short = {
    'D1':   {1:"Sì",2:"No","All":'Totale', pd.NA:"Non risponde"},
    'D2a' : {
        1:'figli',
        2: 'amici/parenti',
        3: 'Internet',
        4: 'pieghevole',
        5: 'giornale',
        6: 'radio/TV ',
        7: 'casualmente',
        8: 'conoscevo',
        9: 'altro ',
        pd.NA:"Non risponde"
        },
    'D2b' : {
        1:'Da mio figlio/a, nipote',
        2: 'Da amici/parenti',
        3: 'Attraverso Internet',
        4: 'Da un pieghevole/locandina',
        5: 'Da un articolo su una rivista/giornale',
        6: 'Dalla radio/TV ',
        7: 'Casualmente, passando davanti al Museo',
        8: 'Conoscevo già il Museo',
        9: 'Altro ',
        pd.NA:"Non risponde"
        },
    'D2c' : {
        1:'Da mio figlio/a, nipote',
        2: 'Da amici/parenti',
        3: 'Attraverso Internet',
        4: 'Da un pieghevole/locandina',
        5: 'Da un articolo su una rivista/giornale',
        6: 'Dalla radio/TV ',
        7: 'Casualmente, passando davanti al Museo',
        8: 'Conoscevo già il Museo',
        9: 'Altro ',
        pd.NA:"Non risponde"
        },
    'D3' :  {
        1: 'gruppo',
        2: 'solo',
        3: 'coppia',
        4: 'figli',
        5: 'amici',
        pd.NA:"Non risponde"
    },
    'D4a' :  {
        1: 'raccolta',
        2: 'turistica',
        3: 'studio',
        4: 'accompagnare',
        5: 'mostra',
        6: 'tempo libero',
        7: 'docente',
        9: 'altro',
        pd.NA:"Non risponde"
    },
    'D4b' :  {
        1: 'Interesse specifico sulla raccolta',
        2: 'Come parte di una visita turistica nella zona/città',
        3: 'Interesse di studio/professionale',
        4: 'Per accompagnare amici/conoscenti',
        5: 'Per visitare una mostra o partecipare ad una iniziativa in corso',
        6: 'Per trascorrere del tempo libero',
        7: 'Docente di una classe in visita',
        9: 'Altro',
        pd.NA:"Non risponde"
    },
    'D4c' :  {
        1: 'Interesse specifico sulla raccolta',
        2: 'Come parte di una visita turistica nella zona/città',
        3: 'Interesse di studio/professionale',
        4: 'Per accompagnare amici/conoscenti',
        5: 'Per visitare una mostra o partecipare ad una iniziativa in corso',
        6: 'Per trascorrere del tempo libero',
        7: 'Docente di una classe in visita',
        9: 'Altro',
        pd.NA:"Non risponde"
    },
    'D5' :  {
        1:'provincia',
        2:'Italia',
        3:'estero',
        pd.NA:"Non risponde"
    },
    'D6':   {
        1:"Maschio",
        2:"Femmina",
        "All":'Totale', 
        pd.NA:"Non risponde"
    },
    'D7':   {
        1:"Meno di 18",
        2:"Tra 18 e 30",
        3:"Tra 31 e 45",
        4:"Tra 46 e 65",
        5:"Più di 65",
        "All":'Totale',
        pd.NA:"Non risponde"
    }, 
    'D8' : {
    1: 'Elementare',
    2: 'Medie inferiori',
    3: 'Diploma medie superiori',
    4: 'Laurea o titoli post-laurea',
    5: 'Nessuno',
    pd.NA:"Non risponde"
    },
    'D9' : {
    1:'< 30mm',
    2:'30mm-1ora',
    3:'1-2ore',
    4:'+2ore',
    pd.NA:"Non risponde"  
    },
    'D10' : {
    1:'Per niente',
    2:'Poco',
    3:'Abbastanza',
    4:'Molto',
    pd.NA:"Non risponde"
    },
    'D11': {
    1:'Per niente',
    2:'Poco',
    3:'Abbastanza',
    4:'Molto',
    pd.NA:"Non risponde"
    },
    'D12': {
    1:'Per niente',
    2:'Poco',
    3:'Abbastanza',
    4:'Molto',
    pd.NA:"Non risponde"
    },
    'D13': {
    1:'Per niente',
    2:'Poco',
    3:'Abbastanza',
    4:'Molto',
    pd.NA:"Non risponde"
    }
}