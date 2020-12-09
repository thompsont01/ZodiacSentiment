import os
import json
import pandas as pd
def transform_json_tweets_to_csv():
    files = os.listdir()
    files = [f for f in files if f[-4:] == 'json']
    for file in files:
        data_dicts = []
        with open(file) as f:
            zodiac = json.load(f)
        zodiac = zodiac['statuses']
        for tweet in zodiac:
            data_dicts.append(
            {
                'text':tweet['text'],
                'user':tweet['user']['screen_name'],
                'retweets':tweet['retweet_count'],
                'favorites':tweet['favorite_count'],
                'datetime':tweet['created_at']
            })
        data = pd.DataFrame.from_dict(data_dicts)
        data.to_csv(file[:-5]+'.csv')
transform_json_tweets_to_csv()

