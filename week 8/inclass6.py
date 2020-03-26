#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#In-Class 06 - Due 3/26/2020

import pandas as pd

babyNames = pd.read_csv('US_Baby_Names_right.csv')
print('Data Structure Information:\n')
print(babyNames.info())

del babyNames['Unnamed: 0']
del babyNames['Id']

print('\nThe following gender is more common, with count shown:')
print(babyNames['Gender'].value_counts().nlargest(1))

print('\nThe following five names are most common, with counts shown:')
print(babyNames['Name'].value_counts().nlargest())

namesOnly = babyNames.groupby('Name').sum()
print('\nThe number of names in the dataset is:')
print(len(namesOnly))

print('\nStandard Deviation of Name Occurrence:')
print(namesOnly.Count.std())

print('\nBasic Descriptive Statistics on Names:')
print(babyNames['Name'].describe())