import unittest
import logging
import logging.config
from airtest.core.api import *
from common.common_func import get_config_data, init_phone, connect_phone, disconnect_phone, reset_adb, mkdir, init_excel
from time import sleep

mkdir('./log')
CON_LOG = './config_file/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

class MyUnit(unittest.TestCase):

    data = get_config_data()

    @classmethod
    def setUpClass(cls):
        cls.workbook, cls.worksheet = init_excel()
        reset_adb()
        connect_phone()
        init_phone()


    def setUp(self):
        logging.info('setUp')
        start_app(self.data['app_package'])
        sleep(30)


    def tearDown(self):
        logging.info('tearDown')
        keyevent("BACK")
        sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.workbook.close()
        disconnect_phone()


