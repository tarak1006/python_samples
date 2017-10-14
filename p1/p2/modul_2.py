import logging
'''
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(asctime)s :%(levelname)s :%(message)s')

file_handler=logging.FileHandler('p2.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler=logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
'''
logger=logging.getLogger('p2_logger')
def f3():
    logger.debug("you are in p2 funcn f3 debug mode log file p2")
    print("entering method f3")
    print("exiting method f3")
    logger.error("you are in p2 funcn f3 error mode log file p2")

def f4():
    logger.debug("you are in p2 funcn f4 debug mode log file p2")
    print("entering method f4")
    print("exiting method f4")
    logger.error("you are in p2 funcn f4 error mode log file p2")