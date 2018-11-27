import sys
sys.path.append('D:/sdk2.0_project')

import unittest
from common.common_func import get_time
from BSTestRunner import BSTestRunner
import logging


test_dir='../test_case'
report_dir='../test_reports'

discover=unittest.defaultTestLoader.discover(test_dir, pattern='combination_1.py')

report_name=report_dir + '/' + get_time() + ' test_report.html'



with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title='sdk2.0 Test Report',description='sdk2.0 automatic test report')
    logging.info('start run test case...')
    runner.run(discover)




