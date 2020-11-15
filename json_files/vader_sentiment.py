import pandas as pd
import os
import sys
import numpy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
files = os.listdir()
files = [file for file in  files if file[-4:] == '.csv']
analyzer = SentimentIntensityAnalyzer()
def get_score(s):
    if type(s) == str:
        return analyzer.polarity_scores(s)['compound']
    else:
        return 0.0
def get_weight(retweets):
    return numpy.log(retweets+1+numpy.e)
path = os.getcwd()
summary = []
dfs = []
for file in files:
    df = pd.read_csv(os.path.join(path, file))
    if "text" in df.columns:
        df['score'] = df['text'].map(get_score)
        dfs.append(df)
        df['weights'] = df['retweets'].map(get_weight)
        df['weighted_score'] = df['score']*df['weights']
        df["weighted_score"].describe()
        score = df.weighted_score.describe()
        score.rename(file[:-4],inplace=True)
        summary.append(score)
        score.to_csv(os.path.join(path, "score_for_"+file))
df_summary = pd.DataFrame(summary)
df_summary.sort_values("mean",ascending=False,inplace=True)
df_summary.to_csv(os.path.join(path,"data_summary.csv"))