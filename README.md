# PySubtitle
---

# Warning

该项目仅供在观看英美电影时,学习生僻单词使用,无法保证翻译正确性与流畅性. 我去除了3000个常用单词的翻译, 如果你需要自己定制个人的词库,只需要更改词库words-3000.txt

程序还有许多小问题, 在翻译过程中也还不够只能,另外由于本身设计原因,需要针对每个时间轴都调用一次API进行翻译,所以速度会比较慢.

欢迎提交PR改进这个小玩具.

# Features:

- Support translate in 27 languages
- Support Interspersed/double-line subtitles

# Snapshots

####  V0.0.1

![](https://dn-joway.qbox.me/1465909608178_1.pic_hd.jpg)
![](https://dn-joway.qbox.me/1465909620922_2.pic_hd.jpg)

#### V0.0.2

Support for skip translate common words in 3000 words list .

![](https://dn-joway.qbox.me/1465917259951_1.pic_hd.jpg)
![](https://dn-joway.qbox.me/1465917299225_2.pic_hd.jpg)

The subtitle file will be handled like this :


    200
    00:09:10,327 --> 00:09:12,227
    'Cause that would be a pretty severe signaling(信号) risk.

    201
    00:09:12,329 --> 00:09:14,763
    I(我) mean, you don't(别) have to be in PR(PR) know that insiders(业内人士)

    202
    00:09:14,865 --> 00:09:17,733
    only dump stock like that when they know something is wrong.

    203
    00:09:17,835 --> 00:09:19,634
    The bulk(大量的) of my compensation(补偿) here would be options,(选项，)




You can also make the text separately in two lines:


    127
    00:05:37,281 --> 00:05:40,115
    No, let's drive to the
    one on Forest Avenue.
    不，让我们开车去
    森林大道上的一个。

    128
    00:05:40,217 --> 00:05:42,217
    It's further from that jacket.
    它离那件夹克更进一步。

    129
    00:05:42,319 --> 00:05:45,821
    Claude, you're on pager
    duty until we get back.
    克劳德，你的传呼机
    等到我们回来。

    130
    00:05:46,957 --> 00:05:49,558
    Jared, can I borrow that jacket?
    贾里德，我能借那件夹克吗？



## Install

- git clone git@github.com:joway/PySubtitle.git
- cd PySubtitle
- pip install -r requirements.txt

## Run


- auto translate to zh

    ```python
    python subtitle.py xxx.srt
    ```

- specially translate to other languages

    ```python
    python subtitle.py xxx.srt en -t en
    ```

- double language subtitles

    ```python
    python subtitle.py xxx.srt -d
    ```

# Dependence

Python 3.x


# How it works

Powered by [Baidu Translate API](http://api.fanyi.baidu.com/api/trans/product/index)

# TODO

- web
- custom setting