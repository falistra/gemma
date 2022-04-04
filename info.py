import pandas as pd
import numpy as np
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSe8__fQMlVJUIHbq0ZhmFRRKPciwpyn2143rwuVfQLAunZxw1JnAweUB9_j2xhPNGCDyLnZ9GOcQh6/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url)
print(df.shape)
print(df.info())
print(df.head(10))