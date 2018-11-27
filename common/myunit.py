import unittest
import logging
import logging.config
from airtest.core.api import *
from common.common_func import get_connect_data, connect
from time import sleep

CON_LOG = '../config_file/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

class StartEnd(unittest.TestCase):

    data = get_connect_data()

    def setUp(self):
        logging.info('setUp')
        connect()
        start_app(self.data['app_package'])
        sleep(30)

    def tearDown(self):
        logging.info('tearDown')
        sleep(5)
        stop_app(self.data['app_package'])
