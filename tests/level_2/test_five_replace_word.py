from functions.level_2.five_replace_word import replace_word
import pytest


@pytest.mark.parametrize(
        "text, r_from, r_to, res",
        [("Карусель, карусель начинает рассказ.",
          "карусель",
          "качельки",
          "качельки, качельки начинает рассказ."),
         ("раз два три", "четыре", "4", "раз два три"),
         ("", "", "", "")]
)
def test__resplace_word__success(text, r_from, r_to, res):
    replace_word(text, r_from, r_to) == res
