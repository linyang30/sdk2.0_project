import unittest
import subprocess
from time import sleep
import logging
from common.common_func import record_computer, kill_process_win
import logging.config
from common.myunit_win import StartEnd_win
import os

class WinTest(StartEnd_win):

    test_time = 5

    # def test_BodyReaderPoll(self):
    #
    #     logging.info('test_BodyReaderPoll')
    #     command = self.data['base_dir'] + 'BodyReaderPoll.exe'
    #     p1 = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    #     record_computer(self.test_time, 'BodyReaderPoll')
    #     kill_process(p1.pid)
    #     out = str(p1.stdout.read())
    #
    #     logging.info(out)
    #     result = 'Body mask: width: 640 height: 480' in out
    #     self.assertTrue(result, '没有有效数据')

    def test_all_app(self):
        l = os.listdir(self.data['base_dir'])
        for i in l:
            if i.endswith('.exe'):
                logging.info(i)
                command = self.data['base_dir'] + i
                p1 = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                record_computer(self.test_time, i)
                kill_process_win(p1.pid)
                out = str(p1.stdout.read())
                logging.info(out)

if __name__ == '__main__':
    unittest.main()
