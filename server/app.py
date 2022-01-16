from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

app = FastAPI()


# app.include_router(VegetableRouter, tags=["vegetables"], prefix="/vegetables")

class ItemTest:
    def __init__(self, a, b):
        self.ping = a
        self.otro = b


@app.get("/ping", tags=["Test Connection"], response_model=ItemTest, description='abcderf')
async def read_root():
    return ItemTest('png', 8)


@app.get("/casuas", tags=["defunciones-por-causas-capitulos-sexo-y-grupos-de-edad-ecm-identificador"])
async def obtener_causas():
    import pandas as pd
    import json

    # json string

    # read json to data frame
    df = pd.read_json('data/49075.json')
    nombres = df['Nombre']
    _s = set()
    for row in nombres.values:
        _s.add(row.split('.')[1])
    return {
        'data': _s
    }


@app.get("/edades", tags=["defunciones-por-causas-capitulos-sexo-y-grupos-de-edad-ecm-identificador"])
async def obtener_edades():
    """
    Is it documentation?
    ----
    Cosas de implementación

    :return: un json feo
    """
    import pandas as pd
    import json

    # json string

    # read json to data frame
    df = pd.read_json('data/49075.json')
    nombres = df['Nombre']
    _s = set()
    for row in nombres.values:
        _s.add(row.split('.')[3].strip())
    return {
        'data': sorted(_s)
    }
