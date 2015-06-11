# -*- coding: utf-8 -*-
import unittest
from hanspell import spell_checker
from hanspell.constants import CheckResult

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
        assert items[u'장난감을'] == CheckResult.AMBIGUOUS
        assert items[u'갖고'] == CheckResult.WRONG_SPACING
        assert items[u'놀고'] == CheckResult.WRONG_SPACING
        assert items[u'있다.'] == CheckResult.WRONG_SPACING
        assert items[u'그만하게'] == CheckResult.PASSED
        assert items[u'할까?'] == CheckResult.WRONG_SPELLING

    def test_list(self):
        results = spell_checker.check([u'안녕 하세요.', u'저는 한국인 입니다.'])
        assert results[0].checked == u'안녕하세요.'
        assert results[1].checked == u'저는 한국인입니다.'

if __name__ == '__main__':
    unittest.main()
