import pandas as pd
import re
def clean_tweet(tweet):
  s = re.sub(r"(?:\@|https?\://)\S+", "", tweet).replace("#", "")
  return " ".join(s.split())

import os
files = os.listdir()
for file in files:

    if file[-4:] =='.csv':
        df = pd.read_csv(file)
        if "text" in df.columns:
          df['text'] = df['text'].map(clean_tweet)
          df.to_csv(file)
