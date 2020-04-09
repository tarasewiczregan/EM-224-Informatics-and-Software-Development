#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#In Class 8 - Due 04-09-2020

#stackoverflow showed me how to strip things using apply, and the Counter

import matplotlib.pyplot as plt
import pandas as pd
from nltk.tokenize import word_tokenize
import string
from collections import Counter

df = pd.read_csv('hoboken_tweets.csv')

file = open('stopwords_en.txt', 'r')
stopw = file.read()
file.close()
stops = word_tokenize(stopw)

df['text'] = df['text'].str.lower()	#makes words lowercase in text column

df['text1'] = df['text'].apply(lambda x: ' '.join([w for w in str(x).split() if not w in stops]))
df['text'] = df['text1'].apply(lambda x: ' '.join([w for w in str(x).split() if w.isalpha()]))

topWords = Counter(' '.join(df['text']).split()).most_common(10)	#finds most common words from dataframe

print('\nThe following words were tweeted the most, with counts shown:')
for a, b in topWords:
    print(a, b)

print('\nThe following five screen names tweeted the most, with number of tweets shown:')
print(df['screen_name'].value_counts().nlargest(10))

print('\nGraph for most common words:')
plt.bar(range(len(topWords)), [val[1] for val in topWords], align = 'center')
plt.xticks(range(len(topWords)), [val[0] for val in topWords])
plt.xticks(rotation = 70)
plt.show()

temp1 = df['screen_name'].value_counts().keys().tolist()	#long way around getting top users into list
temp2 = df['screen_name'].value_counts().tolist()
topUsers = [[temp1[0], temp2[0]] , [temp1[1], temp2[1]] , [temp1[2], temp2[2]] , [temp1[3], temp2[3]] , [temp1[4], temp2[4]] , [temp1[5], temp2[5]] , [temp1[6], temp2[6]] , [temp1[7], temp2[7]] , [temp1[8], temp2[8]] , [temp1[9], temp2[9]]]

print('\nGraph for most common users:')
plt.bar(range(len(topUsers)), [val[1] for val in topUsers], align = 'center')
plt.xticks(range(len(topUsers)), [val[0] for val in topUsers])
plt.xticks(rotation = 70)
plt.show()
