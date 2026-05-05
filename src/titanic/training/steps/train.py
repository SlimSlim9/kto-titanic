import logging
from pathlib import Path
import tempfile # Nouvel import pour gérer les fichiers temporaires

import joblib
import mlflow # Nouvel import pour mlflow
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

client = mlflow.MlflowClient() # Client mlflow pour interagir avec le server de tracking

ARTIFACT_PATH = "model_trained"


def train(x_train_path: str, y_train_path: str, n_estimators: int, max_depth: int, random_state: int) -> str:
    logging.warning(f"train {x_train_path} {y_train_path}")
    x_train = pd.read_csv(
        client.download_artifacts(run_id=mlflow.active_run().info.run_id, path=x_train_path), index_col=False # Téléchargement des données depuis mlflow
    )
    y_train = pd.read_csv(
        client.download_artifacts(run_id=mlflow.active_run().info.run_id, path=y_train_path), index_col=False # Téléchargement des données depuis mlflow
    )

    x_train = pd.get_dummies(x_train)

    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)
    model.fit(x_train, y_train)

    model_filename = "model.joblib"
    with tempfile.TemporaryDirectory() as tmp_dir: # Utilisation d'un dossier temporaire
        model_path = Path(tmp_dir, model_filename)
        joblib.dump(model, model_path)
        mlflow.log_artifact(str(model_path), ARTIFACT_PATH) # Log du modèle dans mlflow

    return f"{ARTIFACT_PATH}/{model_filename}" # Retourne le chemin du modèle dans mlflow
