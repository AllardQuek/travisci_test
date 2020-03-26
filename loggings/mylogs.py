import logging 

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

# * Remember FileHandler! To tell new logger which file to log to
file_handler = logging.FileHandler('mylogs.log')
file_handler.setLevel(logging.ERROR)    # Set level for data to be written to file (ignore logs below ERROR level)
file_handler.setFormatter(formatter)

# * Create a StreamHandler to allow logs to be displayed in console while writing higher level logs to file
stream_handler = logging.StreamHandler()    # No need to setLevel as already set above with logger
stream_handler.setFormatter(formatter)      # To set same format as logs written to file

logger.addHandler(file_handler)
logger.addHandler(stream_handler)           # Remember to add any new Handlers created

def divide(n1, n2):
    logger.debug('Now I can see debug info too')
    try:
        return(n1 / n2)
    except ZeroDivisionError:
        # logger.error('Cannot divide by zero!')      Will only log error message but not traceback
        logger.exception('Cannot divide by zero')   # Will log both message and traceback
    
print(divide(6,0))
