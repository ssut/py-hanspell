# -*- coding: utf-8 -*-
from collections import namedtuple

# 조사와 어미도 단어로 처리함. 마땅한 영단어가 생각이 안 나서..
_checked = namedtuple('Checked',
    ['result', 'original', 'checked', 'errors', 'words', 'time'])
class Checked(_checked):
    def __new__(cls, result=False, original='', checked='', errors=0, words=[], time=0.0):
        return super(Checked, cls).__new__(
            cls, result, original, checked, errors, words, time)
