from hanspell import spell_checker
from hanspell.constants import CheckResult

if __name__ == '__main__':
    for i in range(1) :
        result = spell_checker.check(u'안녕 하세요. 저는 한국인 입니다. 이문장은 한글로 작성됬습니다. 외않되. 잘 되는데?')

        #print(type(result))
        #print(result.as_dict().get("original"))
        #print(result.as_dict().get("checked"))
        #print(result.as_dict().get("errors"))
        print(result.as_dict().get("words"))
        #push data to DB.
        #errors -> 에러의 총 갯수

        for key, value in result.words.items():
            print(key, value)
            

        

    