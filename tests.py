# -*- coding: utf-8 -*-
import unittest
from hanspell import spell_checker
from hanspell.constants import CheckResult
from textwrap import dedent as trim


class SpellCheckerTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_basic_check(self):
        result = spell_checker.check(u'안녕 하세요. 저는 한국인 입니다. 이문장은 한글로 작성됬습니다.')

        assert result.errors == 4
        assert result.checked == u'안녕하세요. 저는 한국인입니다. 이 문장은 한글로 작성됐습니다.'

    def test_words(self):
        result = spell_checker.check(u'한아이가 장난깜을 갖고놀고있다. 그만하게 할가?')
        assert result.errors == 4
        
        items = result.words
        assert items[u'한'] == CheckResult.WRONG_SPACING
        assert items[u'아이가'] == CheckResult.WRONG_SPACING
        assert items[u'장난감을'] == CheckResult.STATISTICAL_CORRECTION
        assert items[u'갖고'] == CheckResult.WRONG_SPACING
        assert items[u'놀고'] == CheckResult.WRONG_SPACING
        assert items[u'있다.'] == CheckResult.WRONG_SPACING
        assert items[u'그만하게'] == CheckResult.PASSED
        assert items[u'할까?'] == CheckResult.WRONG_SPELLING

    def test_list(self):
        results = spell_checker.check([u'안녕 하세요.', u'저는 한국인 입니다.'])
        assert results[0].checked == u'안녕하세요.'
        assert results[1].checked == u'저는 한국인입니다.'

    def test_long_paragraph(self):
        paragraph = trim("""
        ubit.info(유빗인포)는 코나미 리듬게임, 유비트의 플레이 데이터 관리 및 열람 서비스입니다. 등록 후에 자신과 친구의 기록을 p.eagate.573.jp에 접속할 필요 없이 본 웹 사이트에서 바로 확인할 수 있습니다.
        등록 후에는 "https://ubit.info/별칭"으로 자신의 개인 페이지가 생성되며 이 주소(별칭)를 아는 사람만 접속할 수 있습니다. 다른 친구에게 기록을 보여주고 싶다면 본인의 인포 주소를 알려주면 됩니다.
        이 사이트는 최신 브라우저 환경만을 제대로 지원합니다. 만약 크롬, 파이어폭스 등의 최신 브라우저 안정버전(stable)을 사용하고 있는데도 페이지 레이아웃이 깨지는 경우 사이트 관리자에게 문의해주세요.
        등록 과정은 간단합니다. 상단 메뉴에서 등록을 클릭한 후 양식에 맞게 입력하시면 자동으로 공개설정이 완료됨과 동시에 유빗인포 계정이 생성됩니다.
        """)

        result = spell_checker.check(paragraph)


if __name__ == '__main__':
    unittest.main()
