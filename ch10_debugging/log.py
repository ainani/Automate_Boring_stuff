#!/usr/bin/python


import logging

def logger(file_name):
    logging.basicConfig(filename=file_name, level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.disable(logging.CRITICAL)

def test_logging():
    logging.debug("Debug message")
    logging.info("INFO message")
    logging.warning("WARNING message")
    logging.error("ERROR message")
    logging.critical("CRITICAL message")

if __name__ == "__main__":
    logger('MyLog.txt')
    test_logging()
