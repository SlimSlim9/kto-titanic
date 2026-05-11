"""
Ce script permet d'inférer le model de machine learning et de le mettre à disposition
dans un Webservice. Il pourra donc être utilisé par notre chatbot par exemple,
ou directement par un front. Remplir ce script une fois l'entrainement du model fonctionne
"""

import os
import pickle
from dataclasses import dataclass
from enum import Enum
import pandas as pd

from fastapi import FastAPI, Depends
# TODO : Importer les dépendances OTEL pour le monitoring

from titanic.api.auth import verify_token


JAEGER_ENDPOINT = os.getenv("JAEGER_ENDPOINT", "http://jaeger.kto-gthomas-dev.svc.cluster.local:4318/v1/traces")

# TODO : Intégrer les configurations d'OTEL et instancier le tracer. Peut être fait plus tard si le cours
# sur l'observabilité n'est pas encore donné

app = FastAPI()

with open("./src/titanic/api/resources/model.pkl", "rb") as f:
    model = pickle.load(f)

class Pclass(Enum):
    UPPER = 1
    MIDDLE = 2
    LOW = 3


class Sex(Enum):
    MALE = "male"
    FEMALE = "female"


@dataclass
class Passenger:
    pclass: Pclass
    sex: Sex
    sibSp: int
    parch: int

    def to_dict(self) -> dict:
        return {"Pclass": self.pclass.value, "Sex": self.sex.value, "SibSp": self.sibSp, "Parch": self.parch}

@app.get("/health")
def health() -> dict:
    return {"status": "OK"}


# TODO : Ajoute les paramètres de la fonction (peut se faire en deux fois avec la sécurisation via oAuth2)
@app.post("/infer")
def infer(passenger: Passenger, token = Depends(verify_token(required_scope="")) ) -> list:
    df_passenger = pd.DataFrame([passenger.to_dict()])
    df_passenger["Sex"] = pd.Categorical(df_passenger["Sex"], categories=[Sex.FEMALE.value, Sex.MALE.value])
    df_to_predict = pd.get_dummies(df_passenger)

    res = model.predict(df_to_predict)

    return res.tolist()