import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup comprehensive logging
logging.basicConfig(level=logging.INFO, filename="foresight.log")
logger = logging.getLogger("foresight")

class AuditLogger:
    @staticmethod
    def log(action, user, obj, details):
        logger.info(f"USER:{user} ACTION:{action} OBJ:{obj} DETAILS:{details}")
