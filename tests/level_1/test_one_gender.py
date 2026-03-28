from functions.level_1.one_gender import genderalize
import pytest


@pytest.mark.parametrize(
    "verb_male, verb_female, gender, res",
    [('тестировал', 'тестировала', 'male', 'тестировал'), 
     ('тестировал', 'тестировала', 'female', 'тестировала')]
)
def test__genderalize__cases(verb_male, verb_female, gender, res):
    assert genderalize(verb_male, verb_female, gender) == res
