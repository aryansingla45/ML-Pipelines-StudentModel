import logging
import os
from datetime import datetime

log_file = f"{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), 'logs', log_file)
os.makedirs(logs_path, exist_ok=True)


log_file_path = os.path.join(logs_path, log_file)

logging.basicConfig(filename=log_file_path,
     level=logging.INFO,
     format=' [%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)

if __name__ == '__main__':
    logging.info("logging is started")
    