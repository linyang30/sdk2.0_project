from common.my_unit import MyUnit
import unittest
from common.common_func import record_phone
import logging
from bussiness_view.touch_operation import TouchOperation

class TestAndroidSDK(MyUnit):

    to = TouchOperation()

    def test_full_profile_min_memory(self):
        logging.info('test_full_profile_min_memory')
        self.to.touch_full_profile()
        self.to.touch_min_memory()
        record_phone('full_profile_min_memory', 2, self.worksheet)

    def test_full_profile_best_accuracy(self):
        logging.info('test_full_profile_best_accuracy')
        self.to.touch_full_profile()
        self.to.touch_best_accuracy()
        record_phone('full_profile_best_accuracy', 3, self.worksheet)

    def test_basic_profile_min_memory(self):
        logging.info('test_basic_profile_min_memory')
        self.to.touch_basic_profile()
        self.to.touch_min_memory()
        record_phone('basic_profile_min_memory', 4, self.worksheet)

    def test_basic_profile_best_accuracy(self):
        logging.info('test_basic_profile_best_accuracy')
        self.to.touch_basic_profile()
        self.to.touch_best_accuracy()
        record_phone('basic_profile_best_accuracy', 5, self.worksheet)


if __name__ == '__main__':
    unittest.main()