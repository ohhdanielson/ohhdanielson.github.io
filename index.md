---
title: Assessment 1
---
# Daniel Hardwick
My name is Daniel Hardwick and I work as a Geographical Information Systems Support Officer. I have worked with GIS for over 10 years and recently deicded to take my knowledge further by enrolling on the MSC in GIS programme at Leeds University. 
My current Module is "Programming for Geographical Information Analysts: Core Skills" which focuses mainly on the programming language Python, and the practical work involved has resuled in me creating an Agent based model. 

## Assessment 1 - Agent based model (ABM)

The ABM has been created within Spyder, which is a Python development environment. The program focuses on a list of ten agents, which have been assigned a number between 0-99, using the 'random' module. The agents were then plotted using the external library 'matplotlib.pyplot. matplotlib.pyplot', showing the location of each individual agent, as shown below. 

![Image of Scatterplot](https://github.com/ohhdanielson/ohhdanielson.github.io/blob/master/Agents_scatterplot.JPG?raw=true)

The random module was used once again to move each agent a random step, allowing each agent to move around randomly. Code was then used to work out the distance between each agent, allowing each agent to know who is near them, essentially allowing the agents to interact. 
A raster file was then introduced into the program, this was used as the agents environment, allowing the agents to interact with it. The environment is shown below.

![Image of Environment](https://github.com/ohhdanielson/ohhdanielson.github.io/blob/master/Agents_scatterplot_environment.JPG?raw=true)

The agents are then programmed to eat away at their environment as they move, interacting with the environment with every step.
Once the agents were sucessfully interacting with the environment, a function was created which made each agent search for nearby agents, based on a set distance, and share resources/information between themselves as they eat away at the environment.
Finally an extra function of matplotlib was used to animate the model, showing where each agent moves and how it interacts with the environment. A stopping condition which ran until the environment was completely eaten was originally used, but the final model runs until a number of iteration has been reached. The result is shown below. 

![Image of Agents_Eating_Environment](https://github.com/ohhdanielson/ohhdanielson.github.io/blob/master/ABM_eating.png?raw=true)

### **Link to repository** - [ohhdanielson ABM repository](https://github.com/ohhdanielson/ohhdanielson.github.io)

This repository contains the following files needed to run the ABM

- Assessment1_model.py - https://raw.githubusercontent.com/ohhdanielson/ohhdanielson.github.io/master/Assessment1_model.py
- agentframework_ABM.py - https://raw.githubusercontent.com/ohhdanielson/ohhdanielson.github.io/master/agentframework_ABM.py
- raster.txt - https://raw.githubusercontent.com/ohhdanielson/ohhdanielson.github.io/master/raster.txt

