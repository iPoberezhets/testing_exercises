from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__bad():
    text = "i like dota2"
    good_words = {"flowers", "cats", "love", "python"}
    bad_words = {"frontend", "javascript", "dota2"}

    assert check_tweet_sentiment(text, good_words, bad_words) == "BAD"


def test__check_tweet_sentiment__good():
    text = "i love cats"
    good_words = {"flowers", "cats", "love", "python"}
    bad_words = {"frontend", "javascript", "dota2"}

    assert check_tweet_sentiment(text, good_words, bad_words) == "GOOD"


def test__check_tweet_sentiment__None():
    text = "the weather is good"
    good_words = {"flowers", "cats", "love", "python"}
    bad_words = {"frontend", "javascript", "dota2"}

    assert check_tweet_sentiment(text, good_words, bad_words) is None


def test__check_tweet_sentiment__None2():
    text = "i like javascript and cats"
    good_words = {"flowers", "cats", "love", "python"}
    bad_words = {"frontend", "javascript", "dota2"}

    assert check_tweet_sentiment(text, good_words, bad_words) is None

