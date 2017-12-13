# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:11:17 2017

@author: Danielson
"""
## distance difference, random starting coordinates for each

import agentframework
import random
import operator
import matplotlib.pyplot
import csv
import matplotlib.animation 

neighbourhood = 20
num_of_agents = 10
num_of_iterations = 100
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

f = open('IO_pract.txt', newline='')  #open the file 
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) #read file as csv

environment = [] #create a list

#make the environment
for row in dataset: # create a list for each row in csv file
    rowlist = []
    for value in row: # populate/append the list with the value of each row
        rowlist.append(value)
    environment.append(rowlist) #populate environment list with rowlist 
    
#make agent list
for i in range (num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

carry_on = True	

#update function
def update(frame_number):
#fig.clear()
    fig.clear()   
    global carry_on
#show environment?
    matplotlib.pyplot.imshow(environment)
#for i in range number of agents
    for i in range(num_of_agents):
        random.shuffle(agents)
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)    
        
    
    for agents in agents:
        if agent.store >10:
            carry_on = False
            print("stopping condition")


    """if random.random() < 0.1:
        carry_on = False
        print("stopping condition")"""
   
#scatterplot agents
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


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

matplotlib.pyplot.show()



matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()




"""print (agents[i].y)
print (agents[i].x)
print (agents[2].x)
print (agents[2].y)"""



