import unittest

from baidu_translate import BaiduTranslate
from subtitle import handle_subtitle


class TranslateTest(unittest.TestCase):
    def test_translate(self):
        print(BaiduTranslate.en_to_zh("Nice to meet you . You are right"))

