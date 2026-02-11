import logging

# basicConfig - Setup
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

logging.debug("Hidden by default")
logging.info("Information message")
logging.warning("Something might be wrong")
logging.error("An error occurred")
logging.critical("System failure!")