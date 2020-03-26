import logging 

# Change logging configuration; 
LOG_FORMAT = "%(asctime)s: %(levelname)s - %(message)s"
logging.basicConfig(filename='root.log', 
                    level=logging.DEBUG, 
                    format=LOG_FORMAT,
                    filemode="w")
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

def multiply(n1, n2):
    logging.debug('now I can see debug info too')
    return(n1 * n2)
    
print(multiply(2,3))
