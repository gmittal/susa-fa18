from dotenv import load_dotenv
import os
import pandas as pd
import praw
load_dotenv()

SUBREDDIT = 'emojipasta'
data = pd.read_csv('reddit-analyze.csv')
comments = data.loc[data['subreddit'] == SUBREDDIT]
reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    password=os.getenv('PASSWORD'),
    username=os.getenv('USERNAME'),
    user_agent=os.getenv('USER_AGENT'))

toxic, severe_toxic, obscene, threat, insult, identity_hate, time = [], [], [], [], [], [], []
i = 0
for idx, row in comments.iterrows():
    i += 1
    print(i/1000)
    toxic.append(row.toxic)
    severe_toxic.append(row.severe_toxic)
    obscene.append(row.obscene)
    threat.append(row.threat)
    insult.append(row.insult)
    identity_hate.append(row.identity_hate)
    time.append(reddit.submission(id=row.id).created_utc)
    print(time[-1])
d = {
    'toxic': toxic,
    'severe_toxic': severe_toxic,
    'obscene': obscene,
    'threat': threat,
    'insult': insult,
    'identity_hate': identity_hate,
    'timestamp': time}
pd.DataFrame(d).to_csv('{0}.csv'.format(SUBREDDIT), index=False)
