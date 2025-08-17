import os
import sys
import logging

log_dir = 'logs'
log_file = 'logging.log'
log_filepath = os.path.join(log_dir,log_file)

os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_filepath),logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger('datasciencelogger')