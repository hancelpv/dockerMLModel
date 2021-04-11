import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib


def main():
    logger.info("Test...")

    data = pd.read_csv("train.csv")
    data["Age"] = data["Age"].fillna(data["Age"].median())
    logger.info(data.columns)

    x = data[["Age"]]
    y = data[["Survived"]]

    model = LogisticRegression()

    model.fit(x, y)

    joblib.dump(model, "model.pkl")

    logger.info("Training complete ...")

    return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(e)
