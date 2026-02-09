import logging
# TODO : Intégrer les imports manquants

# TODO : Dans une second temps, récupérer le client mlflow nous permettant de télécharger les artifacts enregistrés à l'étape précédente

FEATURES = ["Pclass", "Sex", "SibSp", "Parch"]

TARGET = "Survived"


def split_train_test(data_path: str) -> tuple[str, str, str, str]:
    logging.warning(f"split on {data_path}")

    # TODO : Implémenter le corps de la fonction avec les éléments du notebook
    # TODO : Dans un second temps, télécharger les artifacts depuis mlflow
    # TODO : Dans un second temps, ajouter les logs mlflow pour enregistrer les artifacts utiles pour la suite

