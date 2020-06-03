# py-hanspell

[![Build Status](https://travis-ci.org/ssut/py-hanspell.svg?branch=master)](https://travis-ci.org/ssut/py-hanspell)
[![PyPI version](https://badge.fury.io/py/py-hanspell.svg)](http://badge.fury.io/py/py-hanspell)

py-hanspell은 네이버 맞춤법 검사기를 이용한 파이썬용 한글 맞춤법 검사 라이브러리입니다.

파이썬 2.7 및 3.4 모두 호환됩니다.

---

## 설치

설치하는 방법으로는 두 가지 방법이 있습니다.

우선 pip를 이용해 설치하는 방법이 있습니다. 
커맨드 라인에 다음 명령어를 입력하시면 자동으로 설치가 진행됩니다

```bash
$ pip install py-hanspell
```

다음으로 이 GitHub 저장소에서 직접 내려받아 설치하는 방법입니다. 이 저장소를 로컬에 clone 하거나 우측에 보이는 메뉴에서 zip 파일로 다운받은 후에 로컬 커맨드 라인에

```bash
$ python setup.py install
```

를 입력하시거나, 또는 hanspell 폴더를 자신의 프로젝트 폴더 안에 포함시키면 됩니다.

### 필요한 라이브러리

- requests

## 사용 방법

```python
>>> from hanspell import spell_checker
>>> result = spell_checker.check(u'안녕 하세요. 저는 한국인 입니다. 이문장은 한글로 작성됬습니다.')
>>> result.as_dict()  # dict로 출력
{'checked': '안녕하세요. 저는 한국인입니다. 이 문장은 한글로 작성됐습니다.',
 'errors': 4,
 'original': '안녕 하세요. 저는 한국인 입니다. 이문장은 한글로 작성됬습니다.',
 'result': True,
 'time': 0.07065701484680176,
 'words': {'안녕하세요.': 2,
           '저는': 0,
           '한국인입니다.': 2,
           '이': 2,
           '문장은': 2,
           '한글로': 0,
           '작성됐습니다.': 1}}
>>> result
Checked(result=True, original='안녕 하세요. 저는 한국인 입니다. 이문장은 한글로 작성됬습니다.', checked='안녕하세요. 저는 한국인입니다. 이 문장은 한글로 작성됐습니다.', errors=4, words=OrderedDict([('안녕하세요.', 2), ('저는', 0), ('한국인입니다.', 2), ('이', 2), ('문장은', 2), ('한글로', 0), ('작성됐습니다.', 1)]), time=0.10472893714904785)
```

### `list`로 주고받기

```python
>>> from hanspell import spell_checker
>>> spell_checker.check([u'안녕 하세요.', u'저는 한국인 입니다.'])
[Checked(result=True, original='안녕 하세요.', checked='안녕하세요.', errors=1, words=OrderedDict([('안녕하세요.', 2)]), time=0.03297615051269531),
 Checked(result=True, original='저는 한국인 입니다.', checked='저는 한국인입니다.', errors=1, words=OrderedDict([('저는', 0), ('한국인입니다.', 2)]), time=0.029018878936767578)]
```


### Checked

| attribute | - | 
|--------|--------|
|result|맞춤법 검사 성공여부를 나타냅니다.|
|original|검사 전의 문장입니다.|
|checked|맞춤법 검사 후의 문장입니다.|
|errors|맞춤법 오류 수를 나타냅니다.|
|words|[Checked.words](#words)|
|time|총 요청 시간을 나타냅니다.|

### <a name="words"></a>Checked.words

위 사용 방법에 나와있는 words 부분은 교정된 최종 문장을 공백으로 나눈(split) 결과입니다.

결과는 key가 단어, value가 [CheckResult](#results)를 나타냅니다.

아래 코드를 참고하세요.

```python
>>> for key, value in result.words.items():
...    print(key, value)
안녕하세요. 2
저는 0
한국인입니다. 2
이 2
문장은 2
한글로 0
작성됐습니다. 1
```

### <a name="results"></a>CheckResult

아래 코드로 import 하신 후 비교에 사용할 수 있는 상수입니다.

```python
from hanspell.constants import CheckResult
```

| .CONST | - | 
|--------|--------|
|.PASSED|맞춤법 검사 결과 문제가 없는 단어 또는 구절|
|.WRONG_SPELLING|맞춤법에 문제가 있는 단어 또는 구절|
|.WRONG_SPACING|띄어쓰기에 문제가 있는 단어 또는 구절|
|.AMBIGUOUS|표준어가 의심되는 단어 또는 구절|
|.STATISTICAL_CORRECTION|통계적 교정에 따른 단어 또는 구절|


## 라이브러리 사용에 대한 안내

이 라이브러리는 네이버 한글 맞춤법 검사기를 바탕으로 만들어진 라이브러리입니다.

모든 결과 및 데이터에 대한 저작권 및 책임은 네이버 주식회사에 있으며, 라이브러리를 상업적으로 사용하거나 불법적인 용도로 활용한 부분에 대해서는 그 어떠한 부분에 대해서도 개발자는 책임지지 않습니다.

## 변경내역

- **버전 1.1**: list 타입으로 주고받는 기능 지원, 처리속도 향상
- **버전 1.0**: 첫 버전 릴리즈


## 라이선스(License)

py-hanspell은 MIT License로 제공됩니다. 라이선스 전문은 아래와 같습니다:

```
The MIT License (MIT)

Copyright (c) 2015 SuHun Han

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
