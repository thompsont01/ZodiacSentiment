import re
def clean_tweet(tweet):
  s = re.sub(r".*(?:\@|https?\://)\S+", "", tweet).replace("#", "")
  s = s.replace('\r',' ').replace('\n',' ')
  return " ".join(s.split())