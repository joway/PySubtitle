import re
import time

import pysrt
import requests

from baidu_translate import BaiduTranslate


class Subtitle(object):
    @classmethod
    def init_word_list(cls):
        words_list = set()
        with open('words-3000.txt', 'r', encoding='utf-8') as words:
            for line in words:
                words_list.add(line.split(' ')[0])
        words.close()
        return words_list

    @classmethod
    def is_word_valid(cls, word, words_list):
        todo = re.match(r"\b[a-z]+\b", word.lower(), flags=0)
        if todo:
            return todo.group(0) not in words_list
        return False

    @classmethod
    def handle_subtitle(cls, filename, target=None, to='zh', by_words=True):
        subs = pysrt.open(filename)
        words_list = cls.init_word_list()
        for sub in subs:
            if by_words:
                result = ''
                result_dict = BaiduTranslate.translate(sub.text.replace(' ', '\n'))
                for k in result_dict:
                    if cls.is_word_valid(k, words_list):
                        result += k + '(' + result_dict.get(k) + ') '
                    else:
                        result += k + ' '
                sub.text = result
                print(result)
            else:
                try:
                    result = BaiduTranslate.translate(sub.text, to=to)
                except requests.exceptions.ReadTimeout:
                    time.sleep(10)
                    BaiduTranslate.log('HTTP TIME OUT : ' + sub.text)
                    continue
                for r in result:
                    sub.text += '\n' + result[r]
        subs.save(target or filename + '.' + to + '.srt')
        return True
