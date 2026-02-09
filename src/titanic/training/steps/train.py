import logging
# TODO : Intégrer les imports manquants

# TODO : Dans une second temps, récupérer le client mlflow nous permettant de télécharger les artifacts enregistrés à l'étape précédente

ARTIFACT_PATH = "model_trained"


def train(x_train_path: str, y_train_path: str, n_estimators: int, max_depth: int, random_state: int) -> str:
    logging.warning(f"train {x_train_path} {y_train_path}")

    # TODO : Implémenter la fonction avec les expérimentations du notebook
    # TODO : Dans un second temps, récupérer les données depuis mlflow

    # TODO : Dans un second temps, stocker le model en tant qu'artifact dans mlflow
