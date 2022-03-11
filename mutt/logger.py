from distutils.log import INFO
import logging

logging.basicConfig(format='%(asctime)s - [%(levelname)s] %(message)s', 
datefmt='%m/%d/%Y %I:%M:%S %p',
level=INFO)

def log(message):
    logging.info(message)