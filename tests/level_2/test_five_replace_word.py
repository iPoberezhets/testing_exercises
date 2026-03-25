from functions.level_2.five_replace_word import replace_word


def test__resplace_word__replaced():
    text = """Карусель, карусель начинает рассказ.
              Это сказки, песни и веселье!
              Карусель, карусель — это радость для нас,
              Прокатись на нашей карусели!"""
    replace_from = "карусель"
    replace_to = "качельки"
    replaced_text = """качельки, качельки начинает рассказ.
                       Это сказки, песни и веселье!
                       качельки, качельки — это радость для нас,
                       Прокатись на нашей карусели!"""

    replace_word(text, replace_from, replace_to) == replaced_text


def test__resplace__no_replaced():
    text = "раз два три"
    replace_from = "четыре"
    replace_to = "4"

    replace_word(text, replace_from, replace_to) == text


def test__resplace__empty():
    text = ""
    replace_from = ""
    replace_to = ""

    replace_word(text, replace_from, replace_to) == text
