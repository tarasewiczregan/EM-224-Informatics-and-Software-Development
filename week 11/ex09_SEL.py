#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#EX09, Due 04-29-2020
#THIS ONE USES SELENIUM INSTEAD OF REQUESTS/URLLIB

from bs4 import BeautifulSoup
from selenium import webdriver
import string
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.util import ngrams
from collections import Counter

#collects and launches news site, wsj.com
driver = webdriver.Chrome()
url = 'https://www.wsj.com/'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')

headlines = []
tops = soup.find_all(class_ = 'WSJTheme--headline--7VCzo7Ay')	#common element of all headlines on page

for w in tops:
    title = w.find('a').contents[0]	#line of html code where the text for headline exists
    title = title.replace('\n', ' ').strip()
    if title not in headlines: headlines.append(title)	#adds to list of headlines, accounting for any possible duplicates

#displays headlines
for w in headlines:
    print(w)

#the following sections prepare the headlines and remove stopwords, nonalpha
head2 = [w for line in headlines for w in line.split()]

file = open('stopwords_en.txt', 'r')
stopw = file.read()
file.close()
stops = word_tokenize(stopw)

head2 = [w.lower() for w in head2]
table = str.maketrans('', '', string.punctuation)
head2 = [w.translate(table) for w in head2]
head2 = [w for w in head2 if w.isalpha()]
head2 = [w for w in head2 if not w in stops]

#collects and counts the frequency of bigrams, adds any reoccuring bigrams to the collection of words from headlines
big = list(ngrams(head2, 2))
counter = Counter(big)
for i in counter:
    if (counter[1] > 1): head2.append('_'.join(counter[0][0] + counter[0][1]))

#prepares, displays, and saves the wordcloud created from headlines
textStr = ' '.join(head2)
wc = WordCloud(background_color = 'white', max_words = 2000, stopwords = stops)
wc.generate(textStr)
wc.to_file('wcSEL.png')
plt.imshow(wc)
plt.axis('off')
plt.show()
