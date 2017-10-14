import logging
'''logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(asctime)s :%(levelname)s :%(message)s')

file_handler=logging.FileHandler('p1.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler=logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)'''
logger=logging.getLogger('p1_logger')

def f1():
    logger.debug('you are in p1 funcn f1 debug mode,log file p1')
    print("entering method f1")
    print("exiting method f1")
    logger.error("you are in p1 funcn f1 error mode,log file p1")

def f2():
    logger.debug("you are in p1 funcn f2 debug mode,log file p1")
    print("entering method f2")
    print("exiting method f2")
    logger.error("you are in p1 funcn f2 error mode,log file p1")