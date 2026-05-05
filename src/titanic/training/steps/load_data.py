import logging
import os
from pathlib import Path
import tempfile # Nouvel import pour gérer les fichiers temporaires

import boto3
import mlflow # Nouvel import pour mlflow
import pandas as pd
#from ydata_profiling import ProfileReport


ARTIFACT_PATH = "path_output"
PROFILING_PATH = "profiling_reports"


def load_data(path: str) -> str:
  logging.warning(f"load_data on path : {path}")

  with tempfile.TemporaryDirectory() as tmp_dir: # Utilisation d'un dossier temporaire
    local_path = Path(tmp_dir, "data.csv") # Fichier temporaire pour stocker les données
    logging.warning(f"to path : {local_path}")

    s3_client = boto3.client(
      "s3",
      endpoint_url=os.environ.get("MLFLOW_S3_ENDPOINT_URL"),
      aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
      aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    )

    s3_client.download_file("kto-titanic", path, local_path)
    df = pd.read_csv(local_path)

    #profile = ProfileReport(df, title=f"Profiling Report - {local_path.stem}")
    #with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as tmp_file: # Fichier temporaire pour le rapport de profiling
    #  profile.to_file(tmp_file.name)
    #  mlflow.log_artifact(tmp_file.name, PROFILING_PATH) # Log du rapport de profiling dans mlflow

    mlflow.log_artifact(str(local_path), ARTIFACT_PATH) # Log du fichier de données dans mlflow

  return f"{ARTIFACT_PATH}/{local_path.name}" # Retourne le chemin dans mlflow
