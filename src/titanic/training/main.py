import logging

import fire
# TODO : Ajouter les imports manquants

def workflow(input_data_path: str, n_estimators: int, max_depth: int, random_state: int) -> None:
    logging.warning(f"workflow input path : {input_data_path}")
    # TODO : Implémenter le workflow
    # TODO : Dans un second temps, démarrer le run mlflow au début de ce workflow


if __name__ == "__main__":
    fire.Fire(workflow)
    