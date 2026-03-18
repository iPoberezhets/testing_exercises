from decimal import Decimal
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
from datetime import datetime
import pytest


def test__parse_ineco_expense__case1():
    cards = [BankCard("2222", "Author"),
             BankCard("3333", "Author"),
             BankCard("1234", "Author")]
    sms = SmsMessage("100 rub, 1234 01.01.26 21:14 Pyaterochka authcode 0000 ",
                     "Author",
                     datetime(2026, 1, 1))
    result = Expense(amount=Decimal('100'),
                     card=BankCard(last_digits='1234', owner='Author'),
                     spent_in='Pyaterochka',
                     spent_at=datetime(2026, 1, 1, 21, 14))

    assert parse_ineco_expense(sms, cards) == result


def test__parse_ineco_expense__no_card_in_cards():
    cards = [BankCard("2222", "Author")]
    sms = SmsMessage("100 rub, 1234 01.01.26 21:14 Pyaterochka authcode 0000 ",
                     "Author",
                     datetime(2026, 1, 1))
    with pytest.raises(IndexError):
        parse_ineco_expense(sms, cards)


def test__parse_ineco_expense__wrong_time_in_massage():
    cards = [BankCard("1234", "Author")]
    sms = SmsMessage("100 rub, 1234 01.01.26 21-14 Pyaterochka authcode 0000 ",
                     "Author",
                     datetime(2026, 1, 1))
    with pytest.raises(ValueError):
        parse_ineco_expense(sms, cards)


def test__parse_ineco_expense__wrong_massage():
    cards = [BankCard("1234", "Author")]
    sms = SmsMessage("100 rub, 1234 01.01.26 21:14 authcode 0000 test string",
                     "Author",
                     datetime(2026, 1, 1))
    with pytest.raises(ValueError):
        parse_ineco_expense(sms, cards)
