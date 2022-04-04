import pandas as pd
domande = {
    'D1':   'È la prima volta che visita il Museo Universitario Gemma?', 
    'D2a':  'Come ne è venuto a conoscenza?',
    'D6':   'Sesso',
    'D7':   'Età'
}

risposte = {
    'D1':   {1:"1.Sì",2:"2.No","All":'Totale', pd.NA:"Non risponde"},
    'D6':   {1:"1.Maschio",2:"2.Femmina",3:"2.Femmina","All":'Totale', pd.NA:"Non risponde"},
    'D7':   {1:"1.Meno di 18",2:"2.Tra 18 e 30",3:"3.Tra 31 e 45",4:"4.Tra 46 e 65",5:"5.Più di 65","All":'Totale',pd.NA:"Non risponde"} 
}