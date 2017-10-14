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

def f5():
    logger.debug("you are in p1 funcn f5 debug mode,log file p1")
    print("entering method f5")
    print("exiting method f5")
    logger.error("you are in p1 funcn f5 error mode,log file p1")