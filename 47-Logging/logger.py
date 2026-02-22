import logging


# To change the logging level, you can use the basicConfig method of the logging module. For example, to log all messages including debug messages, you can set the logging level to DEBUG:
# logging.basicConfig(level=logging.DEBUG)

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.basicConfig(level=logging.DEBUG, format='%(filename)s - %(asctime)s - %(levelname)s - %(message)s', filename='47-Logging/logger.log', filemode='w')

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

# By default, the logging module is set to log messages with a severity level of WARNING or higher.
# So, the debug and info messages will not be displayed in the output, while the warning, error, and critical messages will be displayed.
