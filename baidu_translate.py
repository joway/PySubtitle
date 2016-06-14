import hashlib
import random

import requests

from local_settings import APPID, APPKEY

"""
签名是为了保证调用安全，使用MD5算法生成的一段字符串，生成的签名长度为 32位，签名中的英文字符均为小写格式

为保证翻译质量，请将单次请求长度控制在 6000 bytes以内。（汉字约为2000个）

签名生成方法如下：
1、将请求参数中的 APPID(appid), 翻译query(q, 注意为UTF-8编码), 随机数(salt), 以及平台分配的密钥(可在管理控制台查看)
按照 appid+q+salt+密钥 的顺序拼接得到字符串1。
2、对字符串1做md5，得到32位小写的sign。

注意:
1、请先将需要翻译的文本转换为UTF-8编码
2、在发送HTTP请求之前需要对各字段做URL encode。
3、在生成签名拼接 appid+q+salt+密钥 字符串时，q不需要做URL encode，在生成签名之后，
发送HTTP请求之前才需要对要发送的待翻译文本字段q做URL encode。
"""

BAIDU_TRANS_API = 'http://api.fanyi.baidu.com/api/trans/vip/translate'


class BaiduTranslate(object):
    @classmethod
    def salt(cls, start=32768, end=65536):
        return random.randint(start, end)

    @classmethod
    def sign(cls, appid, query, salt, key):
        m = hashlib.md5()
        m.update((str(appid) + query + str(salt) + key).encode('utf-8'))
        # 32 位 md5值
        return m.hexdigest()

    @classmethod
    def translate(cls, query, fr='auto', to='zh'):
        salt = cls.salt()
        payload = {'q': query,
                   'from': fr,
                   'to': to,
                   'appid': APPID,
                   'salt': salt,
                   'sign': cls.sign(APPID, query, salt, APPKEY)}
        r = requests.get(BAIDU_TRANS_API, params=payload)
        return cls.parse(r.json())

    @classmethod
    def en_to_zh(cls, query):
        return cls.translate(query, fr='en', to='zh')

    @classmethod
    def zh_to_en(cls, query):
        return cls.translate(query, fr='zh', to='en')

    @classmethod
    def parse(cls, response):
        try:
            dst = response['trans_result'][0]['dst']
            src = response['trans_result'][0]['src']
        except KeyError:
            cls.log('error : ' +
                    response['error_code'] + ":  " + response['error_msg'])
            return response['error_code'], response['error_msg']
        cls.log('success : ' + response)
        return dst, src

    @classmethod
    def log(cls, msg):
        print(msg)
