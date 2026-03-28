from functions.level_2.four_sentiment import check_tweet_sentiment
import pytest


@pytest.mark.parametrize(
        "text, goods, bads, res",
        [("i like dota2",
          {"flowers", "cats", "love", "python"},
          {"frontend", "javascript", "dota2"},
          "BAD"),
         ("i love cats",
          {"flowers", "cats", "love", "python"},
          {"frontend", "javascript", "dota2"},
          "GOOD"),
         ("the weather is good",
          {"flowers", "cats", "love", "python"},
          {"frontend", "javascript", "dota2"},
          None),
         ("i like javascript and cats",
          {"flowers", "cats", "love", "python"},
          {"frontend", "javascript", "dota2"},
          None)]
)
def test__check_tweet_sentiment__succes(text, goods, bads, res):
    assert check_tweet_sentiment(text, goods, bads) == res
