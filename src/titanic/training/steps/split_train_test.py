import logging
from pathlib import Path
import tempfile # Nouvel import pour gérer les fichiers temporaires

import mlflow # Nouvel import pour mlflow
import pandas as pd
import sklearn.model_selection

client = mlflow.MlflowClient() # Client mlflow pour interagir avec le server de tracking

FEATURES = ["Pclass", "Sex", "SibSp", "Parch"]

TARGET = "Survived"


def split_train_test(data_path: str) -> tuple[str, str, str, str]:
    logging.warning(f"split on {data_path}")
    # Téléchargement des données brutes depuis mlflow
    df = pd.read_csv(client.download_artifacts(run_id=mlflow.active_run().info.run_id, path=data_path), index_col=False) 

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
    with tempfile.TemporaryDirectory() as tmp_dir: # Utilisation d'un dossier temporaire
        for data, artifact_path, filename in datasets:
            file_path = Path(tmp_dir, filename)
            data.to_csv(file_path, index=False)
            mlflow.log_artifact(str(file_path), artifact_path) # Log du fichier de split dans mlflow
            artifact_paths.append(f"{artifact_path}/{filename}") # Stockage du chemin dans mlflow

    return tuple(artifact_paths)
