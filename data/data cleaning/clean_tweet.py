import re
def clean_tweet(tweet):
  s = re.sub(r"(?:\@|https?\://)\S+", "", tweet).replace("#", "")
  return " ".join(s.split())