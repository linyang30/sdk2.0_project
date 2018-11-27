from common.myunit import StartEnd
import unittest
from common.common_func import get_cpu_info, get_memory_info
from airtest.core.api import *
from time import sleep

class Combination1(StartEnd):

    def test_1(self):
        touch(Template(filename='../action_image/seq.png', threshold=0.7, resolution=(1280, 720)))
        touch(Template(filename='../action_image/min_memory.png', threshold=0.7, resolution=(1280, 720)))
        sleep(20)
        get_cpu_info()
        get_memory_info()




if __name__ == '__main__':
    unittest.main()