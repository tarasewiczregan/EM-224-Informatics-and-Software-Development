#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#EX-06, Due 03-26-2020

import pandas as pd

unames = ['userID', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep = '::', header = None, names = unames, engine = 'python')

rnames = ['userID', 'movieID', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep = '::', header = None, names = rnames, engine = 'python')

mnames = ['movieID', 'title', 'genre(s)']
movies = pd.read_table('movies.dat', sep = '::', header = None, names = mnames, engine = 'python')

print('\nThe first five lines of the \'users\' data frame.\n')
print(users[:5])

print('\nThe first five lines of the \'ratings\' data frame.\n')
print(ratings[:5])

print('\nThe first five lines of the \'movies\' data frame.\n')
print(movies[:5])

mID = ratings['movieID'][ratings['rating'].idxmax()]
print('\nThe first movie with the highest rating in the movie dataframe is:\n')
print(movies.loc[movies['movieID'] == mID, 'title'].values[0])

data = pd.merge(pd.merge(ratings, users), movies)

print('\nThe first five lines of the merged data frame:\n' , data[:5])

print('\nThere are %s records in \'Users\'' % len(users.index))
print('\nThere are %s records in \'Ratings\'' % len(ratings.index))
print('\nThere are %s records in \'Movies\'' % len(movies.index))
print('\nThere are %s records in \'Data\'' % len(data.index))