import yaml
from airtest.core.api import *
import time
import os
import logging
import psutil

def get_connect_data():
    logging.info('get_connect_data')
    with open('../config_file/connect_config.yaml', 'r') as file:
        data = yaml.load(file)
    return data

def connect():
    logging.info('connect device')
    data = get_connect_data()
    connect_device('Android://' + str(data['ip']) + ':' + str(data['port']) + '/' + str(
        data['device_name']) + '?ori_method=' + str(data['connect_func']))

def get_time():
    logging.info('get_time')
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    return now

def get_phone_cpu_info():
    logging.info('get_phone_cpu_info')
    out = os.popen('adb shell dumpsys cpuinfo | findstr "TOTAL"').read()
    result = out.split()[2]
    logging.info('cpu:'+ result)
    return result

def get_phone_memory_info():
    logging.info('get_phone_memory_info')
    out_total = os.popen('adb shell dumpsys meminfo | findstr /c:"Total RAM"').read()
    out_used = os.popen('adb shell dumpsys meminfo | findstr /c:"Used RAM"').read()

    total = int(out_total.split()[2])
    used = int(out_used.split()[2])

    result = round(used / total * 100)
    logging.info('memory:' + str(result) + '%')
    return str(result) + '%'

def get_phone_screen_shot(name):
    logging.info('get_phone_screen_shot')
    image_name = '../screenshots/' + get_time() + name + '.png'
    snapshot(filename=image_name)

def record_phone(test_time, test_name):
    sleep(180)
    logging.info('=' * 20 + 'start_' + test_name + '=' * 20)
    get_phone_cpu_info()
    get_phone_memory_info()
    get_phone_screen_shot('start_' + test_name)
    sleep(test_time)
    logging.info('=' * 20 + 'finish_' + test_name + '=' * 20)
    get_phone_cpu_info()
    get_phone_memory_info()
    get_phone_screen_shot('finish_' + test_name)

def get_computer_cpu_info(interval=1):
    logging.info('get_computer_cpu_info： ')
    logging.info(" CPU: " + str(psutil.cpu_percent(interval)) + "%")
    return (" CPU: " + str(psutil.cpu_percent(interval)) + "%")
    # function of Get Memory

def get_computer_memory_info():
    logging.info('get_computer_memory_info')
    phymem = psutil.virtual_memory()
    line = "Memory: %5s%% %6s/%s" % (
        phymem.percent,
        str(int(phymem.used / 1024 / 1024)) + "M",
        str(int(phymem.total / 1024 / 1024)) + "M"
    )
    logging.info(line)
    return line

def record_computer(test_time, test_name):
    sleep(5)
    logging.info('=' * 20 + 'start_' + test_name + '=' * 20)
    get_computer_cpu_info()
    get_computer_memory_info()
    sleep(test_time)
    logging.info('=' * 20 + 'finish_' + test_name + '=' * 20)
    get_computer_cpu_info()
    get_computer_memory_info()

def kill_process_win(pid):
    os.system('TASKKILL /PID %s /T /F' % pid)

if __name__ == '__main__':
    print(get_phone_cpu_info())