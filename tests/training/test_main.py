from unittest.mock import patch, Mock
from titanic.training.main import workflow


def test_workflow_runs_all_steps():
    with (
        patch("titanic.training.main.load_data") as mock_load,
        patch("titanic.training.main.split_train_test") as mock_split,
        patch("titanic.training.main.train") as mock_train,
        patch("titanic.training.main.validate"),
    ):

        mock_load.return_value = "data.csv"
        mock_split.return_value = ("x_train.csv", "x_test.csv", "y_train.csv", "y_test.csv")
        mock_train.return_value = "model.joblib"

        workflow("input.csv", n_estimators=10, max_depth=5, random_state=42)

        mock_load.assert_called_once()
        mock_split.assert_called_once()
        mock_train.assert_called_once()
