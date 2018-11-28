from common.myunit import StartEnd
import unittest
from common.common_func import get_cpu_info, get_memory_info, get_connect_data, get_screen_shot, record
from airtest.core.api import *
from time import sleep
import logging

class Combination1(StartEnd):

    data = get_connect_data()
    resolution = (int(data['screen_width']), int(data['screen_height']))
    threshold = 0.7
    test_time = 60 * 30

    def test_full_profile_min_memory(self):
        logging.info('test_full_profile_min_memory')
        touch(Template(filename='../action_image/full_profile.png', threshold=self.threshold, resolution=self.resolution))
        touch(Template(filename='../action_image/min_memory.png', threshold=self.threshold, resolution=self.resolution))
        record(self.test_time, 'full_profile_min_memory')

    def test_full_profile_best_accuracy(self):
        logging.info('test_full_profile_best_accuracy')
        touch(Template(filename='../action_image/full_profile.png', threshold=self.threshold, resolution=self.resolution))
        # touch(Template(filename='../action_image/best_accuracy.png', threshold=self.threshold, resolution=self.resolution))
        record(self.test_time, 'full_profile_best_accuracy')

    def test_basic_profile_min_memory(self):
        logging.info('test_basic_profile_min_memory')
        touch(Template(filename='../action_image/basic_profile.png', threshold=self.threshold, resolution=self.resolution))
        touch(Template(filename='../action_image/min_memory.png', threshold=self.threshold, resolution=self.resolution))
        record(self.test_time, 'basic_profile_min_memory')

    def test_basic_profile_best_accuracy(self):
        logging.info('test_basic_profile_best_accuracy')
        touch(Template(filename='../action_image/basic_profile.png', threshold=self.threshold, resolution=self.resolution))
        # touch(Template(filename='../action_image/best_accuracy.png', threshold=self.threshold, resolution=self.resolution))
        record(self.test_time, 'basic_profile_best_accuracy')




if __name__ == '__main__':
    unittest.main()