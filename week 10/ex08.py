#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#EX08 - Due 04/16/2020

from bokeh.layouts import row
from bokeh.plotting import figure, output_file, show
from bokeh.models import Title, LabelSet, ColumnDataSource
import numpy as np
from math import pi
import pandas as pd
from bokeh.transform import cumsum
from bokeh.palettes import Category20c

file = open('food.txt', 'r+')
raw = file.readlines()
data = []

for a in raw:		#reads txt file into list of lists
    temp = a.split()
    data.append(temp)

#the plotting of the graphs are made possible by bokeh user guide on docs.bokeh.org
#plot line graph
output_file('beef.html')
p = figure(plot_width = 400, plot_height = 400, title = 'Beef Consumption by Year')
p.yaxis.axis_label = 'Beef Consumption'
p.line(data[0][1:], data[1][1:], line_width = 2, color = 'green')
show(p)

for i in range(1, 5):		#this changes all numbers in list to float
    data[i][1:] = [float(x) for x in data[i][1:]]

beef = data[1][1:]	#save beef and poultry into list just for ease later
poultry = data[3][1:]

#plot scatter plot
output_file('beefVsPoultry.html')
q = figure(plot_width = 400, plot_height = 400, title = 'Beef vs Poultry (Fowl) Consumption')
q.yaxis.axis_label = 'Poultry'
q.xaxis.axis_label = 'Beef'
q.circle(beef, poultry, size = 15, color = 'red', alpha = 0.5)
show(q)

meats = ['Beef', 'Pork', 'Fowl', 'Fish']

#plot bar chart
output_file('avgConsumption.html')
r = figure(plot_width = 400, plot_height = 400, title = 'Average Consumption by Food Type', x_range = meats)
r.vbar(x = meats, width = 0.5, bottom = 0, top =  [np.mean(data[1][1:]), np.mean(data[2][1:]), np.mean(data[3][1:]), np.mean(data[4][1:])], color = 'navy')
show(r)

d = {}		#convert 2005 consumption data to dictionary for pie chart
for i in range(1, 5):
    d[data[i][0]] = data[i][6]

#plot pie chart, thanks to help on stackoverflow.com/questions/29201177/how-do-i-create-a-pie-chart-using-bokeh
data1 = pd.Series(d).reset_index(name = 'value').rename(columns = {'index':'meat'})
data1['angle'] = data1['value']/data1['value'].sum() * 2 * pi
data1['color'] = Category20c[len(d)]

output_file('2005Consumption.html')
s = figure(plot_height = 400, title = 'Per-Capita Comsumption for 2005', toolbar_location = None, tools = 'hover', tooltips = '@meat: @value', x_range = (-0.5, 1.0))
s.wedge(x = 0, y = 1, radius = 0.4, start_angle = cumsum('angle', include_zero = True), end_angle = cumsum('angle'), line_color = 'white', fill_color = 'color', legend = 'meat', source = data1)
data1['value'] = data1['value'].astype(str)
data1['value'] = data1['value'].str.pad(35, side = 'left')
source = ColumnDataSource(data1)
labels = LabelSet(x = 0, y = 1, text = 'value', angle = cumsum('angle', include_zero = True), source = source, render_mode = 'canvas')
s.add_layout(labels)
show(s)
