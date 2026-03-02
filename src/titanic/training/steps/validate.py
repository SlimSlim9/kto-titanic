import logging

import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, median_absolute_error

# TODO : Dans une second temps, récupérer le client mlflow nous permettant de télécharger les artifacts enregistrés à l'étape précédente



def validate(model_path: str, x_test_path: str, y_test_path: str) -> None:
  logging.warning(f"validate {model_path}")
  model = joblib.load(model_path)

  x_test = pd.read_csv(x_test_path, index_col=False)
  y_test = pd.read_csv(y_test_path, index_col=False)

  x_test = pd.get_dummies(x_test)

  if y_test.shape[1] == 1:
    y_test = y_test.iloc[:, 0]

  y_pred = model.predict(x_test)

  mse = mean_squared_error(y_test, y_pred)
  mae = mean_absolute_error(y_test, y_pred)
  r2 = r2_score(y_test, y_pred)
  medae = median_absolute_error(y_test, y_pred)

  feature_names = x_test.columns.tolist()

  if hasattr(model, "feature_importances_"):
    importances = model.feature_importances_
    feature_importance = {
      name: float(importance) for name, importance in zip(feature_names, importances, strict=False)
    }
  elif hasattr(model, "coef_"):
    coefs = model.coef_
    if hasattr(coefs, "shape") and len(coefs.shape) > 1:
      coefs = coefs[0]
    feature_importance = {name: float(coef) for name, coef in zip(feature_names, coefs, strict=False)}
  else:
    feature_importance = {name: 0.0 for name in feature_names}
    logging.warning("Model does not have feature importance attributes")

  logging.warning(f"mse : {mse}")
  logging.warning(f"mae : {mae}")
  logging.warning(f"r2 : {r2}")
  logging.warning(f"medae : {medae}")
  logging.warning(f"feature importance : {feature_importance}")
  # TODO : Dans un second temps, récupérer le model depuis mlflow
  # TODO : Dans un second temps, récupérer les données depuis mlflow
  # TODO : Dans un second temps, loggez vos métriques dans mlflow
  # TODO : Dans un second temps, enregistrer le model dans mlflow


