import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib


def main():
    logger.info("Inside predictions ...")

    data = pd.read_csv("data/test.csv")
    data["Age"] = data["Age"].fillna(data["Age"].median())

    x = data[["Age"]]

    model = joblib.load("model.pkl")

    pred = model.predict(x)

    logger.info("Predictions : ")
    logger.info(pred)

    logger.info("Prediction complete ...")

    return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(e)
