import os

import logging


log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../logs/"))
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
log_file = os.path.abspath(os.path.join(log_dir, 'logs.txt'))

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=log_file,
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
