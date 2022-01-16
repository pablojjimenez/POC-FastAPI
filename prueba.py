"""
DATOs:
https://datos.gob.es/es/catalogo/ea0010587-defunciones-por-causas-capitulos-sexo-y-grupos-de-edad-ecm-identificador-api-49075

"""
import pandas as pd
import json

# json string

# read json to data frame
df = pd.read_json('data/49075.json')
nombres = df['Nombre']
_s = set()
for row in nombres.values:
    _s.add(row.split('.')[7])

for l in _s:
    print(l)

