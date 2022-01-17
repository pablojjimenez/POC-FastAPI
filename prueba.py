"""
DATOs:
https://datos.gob.es/es/catalogo/ea0010587-defunciones-por-causas-capitulos-sexo-y-grupos-de-edad-ecm-identificador-api-49075
https://www.ine.es/jaxiT3/Tabla.htm?t=7036&L=0
"""
import pandas as pd
import json

# json string

# read json to data frame
from pandas.core.window import expanding

df = pd.DataFrame(
    [{
        "Nombre": "II.Tumores. Hombres. De 85 a 89 años. Total Nacional. Personas. ",
        "Data": [
            {
                "Anyo": 2020,
                "Valor": 9087.0
            },
            {
                "Anyo": 2020,
                "Valor": 9087.0
            }
        ]
    },
        {
            "Nombre": "I-XXII.Todas las causas. Ambos sexos. Menos de 1 año. Total Nacional. Personas. ",
            "Data": [
                {
                    "Anyo": 2020,
                    "Valor": 9087.0
                },
                {
                    "Anyo": 2020,
                    "Valor": 9087.0
                }
            ]
        },
        {
            "Nombre": "I-XXII.Todas las causas. Mujeres. De 1 a 4 años. Total Nacional. Personas. ",
            "Data": [
                {
                    "Anyo": 2020,
                    "Valor": 9087.0
                },
                {
                    "Anyo": 2020,
                    "Valor": 9087.0
                }
            ]
        },
    ]
)
df = pd.read_json('data/49075.json')
new = df['Nombre'].str.split('.', expand=False)
df['Nombre'].str.strip()
df[['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6']] = df['Nombre'].str.split('.', expand=True)

tumores = df[(df['C1'] == 'Todas las causas') & (df['C2'] == ' Mujeres') & (df['C3']==' Todas las edades')]

for i in tumores['Data']:
    for j in i:
        print(j.get('Anyo'), j.get('Valor'))
print(df[df['C4']!=' Total Nacional'])