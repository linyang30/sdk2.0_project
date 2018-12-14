import unittest

test_dir='./test_case'
ts = unittest.defaultTestLoader.discover(test_dir, pattern='test_android_sdk.py')
runner = unittest.TextTestRunner()
runner.run(ts)