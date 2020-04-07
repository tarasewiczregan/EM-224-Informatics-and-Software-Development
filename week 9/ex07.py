#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#EX07 - Due 04-09-2020

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import sentiwordnet as swn
import string
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def everything(fileName, name):
    file = open(fileName, 'r')
    first = []
    for line in file:
        if ('"' in line):	#only writes comments into list, all comment lines contain "
            temp = line.split()
            first += temp
            temp = []
    file.close()

    file = open('stopwords_en.txt', 'r')	#collects stopwords
    stopw = file.read()
    file.close()
    stops = word_tokenize(stopw)


    first = [w.lower() for w in first]	#makes everything lowercase
    table = str.maketrans('', '', string.punctuation)	#removes punctuation
    stripped = [w.translate(table) for w in first]
    words = [word for word in stripped if word.isalpha()]	#removes not alpha words
    final = [w for w in words if not w in stopw]	#removes stopwords

    sentiments = []
    count = 0
    for elem in final:
        try: sentiments.append(swn.senti_synset(elem + '.a.03'))	#calculates sentiments for words located in dictionary
        except: count += 1	#counts words uncounted for in sentiment statistics

    with open(name + '.txt', 'w') as f:
        f.write('Unrecognized word count:')
        f.write(str(count))
        for item in sentiments:
            f.write('\n')
            f.write(str(item))

    textStr = ' '.join(final)	#wordcloud creating
    wc = WordCloud(background_color = 'white' , max_words = 2000, stopwords = stops)
    wc.generate(textStr)
    wc.to_file(name + '.png')
    plt.imshow(wc)
    plt.axis('off')
    plt.show()



file = 'ProGuns.txt'
name = 'proGuns'
everything(file, name)

file = 'AgainstGuns.txt'
name = 'agaGuns'
everything(file, name)



