import logging
from pathlib import Path

import pandas as pd
import sklearn.model_selection

# TODO : Dans une second temps, récupérer le client mlflow nous permettant de télécharger les artifacts enregistrés à l'étape précédente

FEATURES = ["Pclass", "Sex", "SibSp", "Parch"]

TARGET = "Survived"


def split_train_test(data_path: str) -> tuple[str, str, str, str]:
  logging.warning(f"split on {data_path}")

  df = pd.read_csv(data_path, index_col=False)

  y = df[TARGET]
  x = df[FEATURES]
  x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.3, random_state=42)

  datasets = [
    (x_train, "xtrain", "xtrain.csv"),
    (x_test, "xtest", "xtest.csv"),
    (y_train, "ytrain", "ytrain.csv"),
    (y_test, "ytest", "ytest.csv"),
  ]

  artifact_paths = []
  for data, artifact_path, filename in datasets:
    file_path = Path("./dist/", filename)
    data.to_csv(file_path, index=False)
    artifact_paths.append(file_path)

  return tuple(artifact_paths)
  # TODO : Dans un second temps, télécharger les artifacts depuis mlflow
  # TODO : Dans un second temps, ajouter les logs mlflow pour enregistrer les artifacts utiles pour la suite
