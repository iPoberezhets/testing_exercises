from functions.level_1.one_gender import genderalize


def test__genderalize__male():
    verb_male = 'тестировал'
    verb_female = 'тестировала'
    gender = 'male'

    assert genderalize(verb_male, verb_female, gender) == verb_male


def test__genderalize__female():
    verb_male = 'тестировал'
    verb_female = 'тестировала'
    gender = 'female'

    assert genderalize(verb_male, verb_female, gender) == verb_female