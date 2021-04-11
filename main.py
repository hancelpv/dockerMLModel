import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
import train
import predict


def main():
    logger.info("Running main ...")

    train.main()
    predict.main()

    logger.info("Run complete ...")

    return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(e)
