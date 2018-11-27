import yaml
from airtest.core.api import *
import time
import os
import logging

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

def get_cpu_info():
    logging.info('get_cpu_info')
    out = os.popen('adb shell dumpsys cpuinfo | findstr "TOTAL"').read()
    result = out.split()[0]
    logging.info('cpu:'+ result)
    return result

def get_memory_info():
    logging.info('get_memory_info')
    out_total = os.popen('adb shell dumpsys meminfo | findstr /c:"Total RAM"').read()
    out_used = os.popen('adb shell dumpsys meminfo | findstr /c:"Used RAM"').read()

    total = int(out_total.split()[2])
    used = int(out_used.split()[2])

    result = round(used / total * 100)
    logging.info('memory:' + str(result) + '%')
    return str(result) + '%'

def get_screen_shot(name):
    logging.info('get_screen_shot')
    image_name = '../screenshots/' + get_time() + 'name' + '.png'
    snapshot(filename=image_name)

if __name__ == '__main__':
    print(get_cpu_info())