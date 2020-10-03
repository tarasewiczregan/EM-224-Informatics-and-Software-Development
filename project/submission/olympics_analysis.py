#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#Final Project, Due 05-12-2020

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from textwrap import wrap

#opens and reads the csv file, only keeps the usual columns for this project
df = pd.read_csv('athlete_events.csv', usecols = ['Team', 'Year', 'Season', 'Sport', 'Medal'])

#sports per year
year = df.drop_duplicates(subset = ['Year', 'Sport'])	#eliminates repeating sports in the same year
year_counts = year['Year'].value_counts()	#collects the counts of each year to get how many sports were played
year_counts = dict(year_counts)
year_counts = sorted(year_counts.items())
x, y = zip(*year_counts)	#prepares data for plot
plt.plot(x, y, 'bo-', markersize = 4)	#line plot with points
plt.grid(True)
plt.title('\n'.join(wrap('Number of Sports Played at Olympics Through the Years (1896 to 2016)')))
plt.tight_layout()
plt.show()

#sports per year - summer games
summer = year[year['Season']!='Winter']	#gets only lines with summer
summer_counts = summer['Year'].value_counts()
summer_counts = dict(summer_counts)
summer_counts = sorted(summer_counts.items())
x, y = zip(*summer_counts)
plt.plot(x, y, 'bo-', markersize = 4)
plt.grid(True)
plt.title('\n'.join(wrap('Number of Sports Played at Summer Olympics Through the Years (1896 to 2016)')))
plt.tight_layout()
plt.show()

#sports per year - winter games
winter = year[year['Season']!='Summer']
winter_counts = winter['Year'].value_counts()
winter_counts = dict(winter_counts)
winter_counts = sorted(winter_counts.items())
x, y = zip(*winter_counts)
plt.plot(x, y, 'bo-', markersize = 4)
plt.grid(True)
plt.title('\n'.join(wrap('Number of Sports Played at Winter Olympics Through the Years (1924 to 2016)')))
plt.tight_layout()
plt.show()

#top countries by medal count
medals = df.dropna(subset = ['Medal'])	#removes rows that did not win medal
top_countries = Counter((medals['Team'])).most_common(5)	#gets top five countries with medals
plt.bar(range(len(top_countries)), [val[1] for val in top_countries], align = 'center')
plt.xticks(range(len(top_countries)), [val[0] for val in top_countries])
plt.xticks(rotation = 90)
plt.title('Top Five Countries and Their Medal Counts')
plt.tight_layout()
plt.show()

#medal distribution by type and year
countries = []
for i in top_countries:	#gets the top winning countries into list
    countries.append(i[0])
for i in countries:	#for each country in the top 5...
    temp = medals[medals['Team'] == i]	#isolates the desired country rows
    medal_counts = temp['Medal'].value_counts()	#gets medal counts by medal type
    medal_counts = dict(medal_counts)
    lk = []
    lv = []
    items = medal_counts.items()
    for a in items:	#splits the medal type and counts as pie chart preparation
        lk.append(a[0]), lv.append(a[1])
    plt.pie(lv, labels = lk, autopct = '%1.1f%%', shadow = True, startangle = 140)
    plt.axis('equal')
    plt.title(i + ' Medal Distribution')
    plt.show()

    year_c = temp['Year'].value_counts()	#counts the year to get total medals won each year
    year_c = dict(year_c)
    year_c = sorted(year_c.items())
    x, y = zip(*year_c)
    plt.plot(x, y, 'bo-', markersize = 4)
    plt.grid(True)
    plt.title('\n'.join(wrap(i + ' Medal Year Distribution')))
    plt.tight_layout()
    plt.show()
