import yaml
from airtest.core.api import *
import time
import logging
import subprocess
import re
import xlsxwriter
from PIL import Image
import pytesseract

def get_config_data():
    logging.info('get_config_data')
    with open('./config_file/connect_config.yaml', 'r') as file:
        data = yaml.load(file)
    return data

def connect_phone():
    logging.info('connect_phone')
    sleep(1)
    data = get_config_data()
    command = 'adb connect ' + str(data['phone_ip']) + ':' + str(data['phone_port'])
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    out = str(p.stdout.readlines())
    pattern = re.compile('already connected to ' + str(data['phone_ip']) + ':' + str(data['phone_port']))
    result_list = pattern.findall(out)
    result = result_list[0] if len(result_list) > 0 else 'None'
    if result == 'already connected to ' + str(data['phone_ip']) + ':' + str(data['phone_port']):
        logging.info('connect phone success')
        sleep(1)
    else:
        connect_phone()

def reset_adb():
    logging.info('reset_adb')
    sleep(1)
    command_kill_server = 'adb kill-server'
    command_start_server = 'adb start-server'
    subprocess.Popen(command_kill_server, shell=True, stdout=subprocess.PIPE)
    sleep(1)
    p = subprocess.Popen(command_start_server, shell=True, stdout=subprocess.PIPE)
    out = str(p.stdout.readlines())
    result = re.findall(r'daemon started successfully', out)
    if result[0] == 'daemon started successfully':
        logging.info('reset adb success')
        sleep(1)
    else:
        reset_adb()

def disconnect_phone():
    logging.info('disconnect_phone')
    sleep(1)
    command = 'adb disconnect'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    out = str(p.stdout.readlines())
    result = re.findall(r'disconnected everything', out)
    if result[0] == 'disconnected everything':
        logging.info('disconnect phone success')
        sleep(1)
    else:
        disconnect_phone()

def init_phone():
    logging.info('init_phone')
    data = get_config_data()
    connect_device('Android://' + str(data['adb_host_ip']) + ':' + str(data['adb_host_port']) + '/' + str(
        data['device_name']) + '?ori_method=' + str(data['connect_func']))


def get_current_time():
    logging.info('get_current_time')
    now = time.strftime('%Y-%m-%d-%H-%M-%S')
    return now

def get_phone_cpu_info():
    logging.info('get_phone_cpu_info')
    command = 'adb shell dumpsys cpuinfo'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    out = str(p.stdout.readlines())
    result = str(re.findall(r'\d+% TOTAL: (\d+)% user', out)[0]) + '%'
    logging.info('cpu:'+ result)
    return result

def get_phone_memory_info():
    logging.info('get_phone_memory_info')
    command = 'adb shell dumpsys meminfo'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    out = str(p.stdout.readlines())
    total = int(re.findall(r'Total RAM: (\d+) kB', out)[0])
    used = int(re.findall(r'Used RAM: (\d+) kB', out)[0])
    result = str(round(used / total * 100)) + '%'
    logging.info('memory:' + result)
    return result

def get_phone_screen_shot(name):
    mkdir('./screenshots')
    logging.info('get_phone_screen_shot')
    image_name = './screenshots/' + name + '.png'
    snapshot(filename=image_name)

def record_phone(test_name, index, worksheet):
    sleep(5)
    logging.info('=' * 20 + 'start_' + test_name + '=' * 20)
    start_cpu_info = get_phone_cpu_info()
    start_mem_info = get_phone_memory_info()
    sleep(get_config_data()['test_time'])
    logging.info('=' * 20 + 'finish_' + test_name + '=' * 20)
    finish_cpu_info = get_phone_cpu_info()
    finish_mem_info = get_phone_memory_info()
    current_time = get_current_time()
    get_phone_screen_shot(test_name + '_' + current_time)
    game_fps, body_fps = get_fps('./screenshots/' + test_name + '_' + current_time + '.png')
    worksheet.write_string('A' + str(index), test_name)
    worksheet.write_string('B' + str(index), start_cpu_info)
    worksheet.write_string('C' + str(index), finish_cpu_info)
    worksheet.write_string('D' + str(index), start_mem_info)
    worksheet.write_string('E' + str(index), finish_mem_info)
    worksheet.write_string('F' + str(index), game_fps)
    worksheet.write_string('G' + str(index), body_fps)

def mkdir(path):
    '''自动创建文件夹'''
    logging.info('mkdir')
    folder = os.path.exists(path)
    if not folder:
        os.mkdir(path)

def init_excel():
    mkdir('./test_result')
    workbook = xlsxwriter.Workbook('./test_result/test_result_' + get_current_time() + '.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write_string('A1', 'Test Case')
    worksheet.write_string('B1', 'Start CPU')
    worksheet.write_string('C1', 'End CPU')
    worksheet.write_string('D1', 'Start Memory')
    worksheet.write_string('E1', 'End Memory')
    worksheet.write_string('F1', 'Game FPS')
    worksheet.write_string('G1', 'Body FPS')
    return workbook, worksheet

def get_fps(image_name):
    logging.info('get_fps')
    img = Image.open(image_name)
    img_game_fps = img.crop((608, 159, 746, 187))
    img_body_fps = img.crop((604, 184, 751, 207))
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    game_fps_list = re.findall(r'Game FPS: (\d+)', pytesseract.image_to_string(img_game_fps))
    body_fps_list = re.findall(r'Body FPS: (\d+)', pytesseract.image_to_string(img_body_fps))
    game_fps = game_fps_list[0] if len(game_fps_list) > 0 else 'None'
    body_fps = body_fps_list[0] if len(body_fps_list) > 0 else 'None'
    return game_fps, body_fps


