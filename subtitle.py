import pysrt

from baidu_translate import BaiduTranslate

filename = 'subtitle.srt'
subs = pysrt.open(filename)
subs[0].text += '\n' + '123'
for index, sub in enumerate(subs):
    BaiduTranslate.log('-----' + str(index) + '-----')
    sub.text += '\n' + BaiduTranslate.en_to_zh(sub.text)[0]
subs.save(filename + 'en_zh.srt')
