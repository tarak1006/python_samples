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
def f6():
    logger.debug("you are in p3 funcn f6 debug mode,log file p1")
    print("entering method f6")
    print("exiting method f6")
    logger.error("you are in p3 funcn f6 error mode,log file p1")