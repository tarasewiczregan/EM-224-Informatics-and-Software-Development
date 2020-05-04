#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#EX-10, Due 05-07-2020

import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS

#reads the csv file
data = pd.read_csv('H_Clinton-emails.csv')


#creates a list of the content, under RawText in csv to clean up (remove stopwords) and create wordcloud
content = data['RawText'].tolist()

#create a wordcloud for top words, eliminate stopwords/cleans up
file = open('stopwords_en.txt', 'r')
stopw = file.read()
file.close()
stops = word_tokenize(stopw)

content1 = []	#collects into list of lists
for a in content:
    temp = a.split()
    content1.append(temp)

content = [] 	#one big list of the words
for a in content1:
    content.extend(a)

tokens = [w.lower() for w in content]
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
words = [w for w in stripped if w.isalpha()]
content = [w for w in words if not w in stops]

#finally create wordcloud
textStr = ' '.join(content)
wc = WordCloud(background_color = 'white', max_words = 2000, stopwords = stops, collocations = False)
wc.generate(textStr)
wc.to_file('content.png')
plt.imshow(wc)
plt.axis('off')
plt.show()



#finds the top 15 senders, all listed under MetadataFrom in csv
print('\nThe following are the top 15 senders, with counts shown:')
print(data['MetadataFrom'].value_counts().nlargest(15))


#creates a list of the top 15 senders, first removes any blanks in senders list
data.dropna(subset = ['MetadataFrom'], inplace  = True)
senders = Counter((data['MetadataFrom'])).most_common(15)

#create a graph for top senders
plt.bar(range(len(senders)), [val[1] for val in senders], align = 'center')
plt.xticks(range(len(senders)), [val[0] for val in senders])
plt.xticks(rotation = 90)
plt.tight_layout()
plt.savefig('senders.png')
plt.show()
