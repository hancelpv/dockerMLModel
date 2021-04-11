import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib


def main():
    logger.info("Test...")

    data = pd.read_csv("test.csv")
    data["Age"] = data["Age"].fillna(data["Age"].median())

    x = data[["Age"]]

    model = joblib.load("model.pkl")

    pred = model.predict(x)

    logger.info("Predictions : ")
    logger.info(pred)

    logger.info("Run complete ...")

    return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(e)
