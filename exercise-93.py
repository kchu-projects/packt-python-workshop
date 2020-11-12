import logging


logger = logging.getLogger("logger_name")
logger.debug("Logging at debug")
logger.info("Logging at info")
logger.warning("Logging at warning")
logger.error("Logging at error")
logger.fatal("Logging at fatal")

system = "moon"
for number in range(3):
    logger.warning(f"{number} errors reported in {system}")
