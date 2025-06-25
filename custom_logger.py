import logging
import json

logging.basicConfig(filename='classification_log.txt', level=logging.INFO)

def log_event(event):
    logging.info(json.dumps(event))
