import unittest
import subprocess
from time import sleep
import logging
from common.common_func import getCPUstate, getMemorystate, record_win
import logging.config
from common.myunit_win import StartEnd_win

class WinTest(StartEnd_win):

    test_time = 5

    def test_ColorReaderEvent_SFML(self):

        logging.info('test_ColorizedBodyViewer_SFML')
        command = self.data['base_dir'] + 'ColorizedBodyViewer-SFML.exe'
        p1 = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        record_win(self.test_time, 'ColorReaderEvent_SFML')
        out = str(p1.stdout.readline())
        p1.kill()
        result = 'fps' in str(out)
        self.assertTrue(result, '没有有效数据')

    def test_ColorReaderEvent(self):
        logging.info('test_ColorReaderEvent')
        command = self.data['base_dir'] + 'ColorReaderEvent.exe'
        p1 = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        record_win(self.test_time, 'ColorReaderEvent')
        out = str(p1.stdout.readline())
        p1.kill()
        result = 'color frameIndex' in str(out)
        self.assertTrue(result, '没有有效数据')

if __name__ == '__main__':
    unittest.main()
