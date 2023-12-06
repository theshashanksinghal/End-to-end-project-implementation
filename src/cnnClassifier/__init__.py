import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# [2023-12-05 23:36:31,709: INFO: main: Welcome to my custom log]

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok= True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    handlers= [
        logging.FileHandler(log_filepath),# creating a local log file.
        logging.StreamHandler(sys.stdout) # printing the logs as output as well.
        ]
)

logger = logging.getLogger("cnnClassifierLogger") #  giving the name to the log.