import logging
'''
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(asctime)s :%(levelname)s :%(message)s')

file_handler=logging.FileHandler('main.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler=logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
'''


from logging.config import dictConfig

logging_config = dict(
    version = 1,
    formatters = { 'f': {'format':'%(asctime)s : %(levelname)s :%(message)s'}  },
    handlers = {  'h': {'class': 'logging.StreamHandler', 'formatter': 'f',  'level': logging.WARNING  },
        'f_main':{'class':'logging.FileHandler',
             'filename':'main_script.log',
             'formatter':'f',
             'level':logging.DEBUG},
        'f_p1': {'class': 'logging.FileHandler',
                   'filename': 'p1.log',
                   'formatter': 'f',
                   'level': logging.DEBUG},
        'f_p2': {'class': 'logging.FileHandler',
                   'filename': 'p2.log',
                   'formatter': 'f',
                   'level': logging.DEBUG}
        },
loggers={
  'main_logger':{
    'level': logging.DEBUG,
    'handlers': ['h','f_main'],
   'propagate':'yes'},
'p1_logger':{
    'level': logging.DEBUG,
    'handlers': ['h','f_p1'],
   'propagate':'yes'},
'p2_logger':{
    'level': logging.DEBUG,
    'handlers': ['h','f_p2'],
   'propagate':'yes'}
},
    #root = {
     #   'handlers': ['h'],
      #  'level': logging.DEBUG,
       # },
)

dictConfig(logging_config)

logger = logging.getLogger('main_logger')
from p1 import m1,m3
from p1.p2 import modul_2
from p1.p3 import m4
m1.f1()
m1.f2()
modul_2.f3()
modul_2.f4()
m4.f6()
m3.f5()
logger.debug('you are in debug mode in main script, log file main')
logger.info('you are in info mode in main script,log file main')
logger.warning('you are in warning mode in main script,log file main')
logger.error('you are in error mode in main script,log file main')
logger.critical('you are in critical mode in main script,log file main')
