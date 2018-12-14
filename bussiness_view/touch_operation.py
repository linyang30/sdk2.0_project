from airtest.core.api import *
from common.common_func import get_config_data
import logging

class TouchOperation:

    data = get_config_data()
    resolution = (int(data['screen_width']), int(data['screen_height']))
    threshold = 0.9

    def touch_full_profile(self):
        logging.info('touch_full_profile')
        if not exists(Template(filename='./action_image/full_profile_checked.png', threshold=self.threshold, resolution=self.resolution)):
            logging.info('full_profile')
            touch(Template(filename='./action_image/full_profile.png', threshold=self.threshold,
                           resolution=self.resolution))

    def touch_basic_profile(self):
        logging.info('touch_basic_profile')
        if not exists(Template(filename='./action_image/basic_profile_checked.png', threshold=self.threshold, resolution=self.resolution)):
            touch(Template(filename='./action_image/basic_profile.png', threshold=self.threshold,
                           resolution=self.resolution))

    def touch_min_memory(self):
        logging.info('touch_min_memory')
        if not exists(Template(filename='./action_image/min_memory_checked.png', threshold=self.threshold, resolution=self.resolution)):
            logging.info('min_memory')
            touch(Template(filename='./action_image/min_memory.png', threshold=self.threshold,
                           resolution=self.resolution))

    def touch_best_accuracy(self):
        logging.info('touch_best_accuracy')
        if not exists(Template(filename='./action_image/best_accuracy_checked.png', threshold=self.threshold, resolution=self.resolution)):
            touch(Template(filename='./action_image/best_accuracy.png', threshold=self.threshold,
                           resolution=self.resolution))


