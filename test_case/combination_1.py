from common.myunit import StartEnd
import unittest
from common.common_func import get_cpu_info, get_memory_info, get_connect_data
from airtest.core.api import *
from time import sleep

class Combination1(StartEnd):

    data = get_connect_data()
    resolution = (int(data['screen_width']), int(data['screen_height']))
    threshold = 0.7

    def test_1(self):
        touch(Template(filename='../action_image/seq.png', threshold=self.threshold, resolution=self.resolution))
        touch(Template(filename='../action_image/min_memory.png', threshold=self.threshold, resolution=self.resolution))
        sleep(60)
        get_cpu_info()
        get_memory_info()




if __name__ == '__main__':
    unittest.main()