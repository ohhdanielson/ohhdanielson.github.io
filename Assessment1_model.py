# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:11:17 2017

@author: Danielson
"""
#import statements
import agentframework_ABM
import random
import operator
import matplotlib.pyplot
import csv
import matplotlib.animation 

neighbourhood = 20
num_of_agents = 10
num_of_iterations = 100

#create an empty list for agents
agents = []

#create an empty list for the environment
environment = [] 

#open text file and read as a csv
f = open('raster.txt', newline='')  
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#make the environment
for row in dataset: 
    rowlist = []
    for value in row: 
        rowlist.append(value)
    environment.append(rowlist) 
    
#populate agent list
for i in range (num_of_agents):
    agents.append(agentframework_ABM.Agent(environment, agents))

carry_on = True

#update function
def update(frame_number):
    fig.clear()   
    global carry_on
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        random.shuffle(agents)
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(agents[i].x,agents[i].y)
     
#Animate line        
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (carry_on):
        yield a            
        a = a + 1

carry_on = True

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#animation - stopping condition - set to stop at num_of_iterations
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)

#scatterplot agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
