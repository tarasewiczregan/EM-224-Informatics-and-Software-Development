#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#In Class 7 - Due 04-02-2020

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

file = open('nasaArticle.txt', 'r')
nasa = file.read()
file.close()

tokens = word_tokenize(nasa)
tokens = [w.lower() for w in tokens]
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
words = [word for word in stripped if word.isalpha()]

file = open('stopwords_en.txt', 'r')
stopw = file.read()
file.close()
stops = word_tokenize(stopw)

nasa2  = [w for w in words if not w in stops]

textStr = ' '.join(nasa2)
wc = WordCloud(background_color = 'white', max_words = 2000, stopwords = stops)
wc.generate(textStr)
wc.to_file('nasa.png')
plt.imshow(wc)
plt.axis('off')
plt.show()
