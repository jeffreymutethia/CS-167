"""
Author(s): Lauren Yumibe , Jeff Mutethia
Date: 10/5/19
Assignment/Problem Number: 6
Assignment/Problem Title: Plotting Populations
"""

#1.Population Growth
def tribble_table(initial_pop, n_days):
    print(' Day','|','Population')
    print('----------------')
    data = []
    population = initial_pop
    for i in range(n_days+1):
        population = int(initial_pop*(1.1**i))
        data.append(population)
        
        print('{0:<4} | {1:>6}'.format(i, population))
    print() #prints extra line to put space in between both tables
       
#2.Predator-Prey Interaction
def vampire_table(initial_humans, initial_vampires, nightly_kill, n_days):   
    print(' Day','|','Humans','|','Vampires')
    print('------------------------')
    
    human_data = []
    vampire_data = []
    humans = initial_humans
    human_data.append(initial_humans)
    vampires = initial_vampires
    vampire_data.append(initial_vampires)
    kill = nightly_kill
    
    print('{0:<4} | {1:>6} | {2:>6}'.format('0',humans,vampires))
    
    for i in range(n_days):  
        humans = humans - int(0.5*vampires)
        human_data.append(humans)
        vampires = int(1.5*vampires)-kill
        vampire_data.append(vampires)
        
        print('{0:<4} | {1:>6} | {2:>6}'.format(i+1,humans,vampires))

#3.MatPlot    
import matplotlib.pyplot as pyplot

def tribble_plot(initial_pop, n_days):
    population = initial_pop
    data = []
    
    for i in range(n_days):
        population = int(population*1.1)
        data.append(population)
        
    pyplot.plot(range(n_days),data)
    pyplot.xlabel('Days')
    pyplot.ylabel('Tribbles')
    pyplot.show()

def vampire_plot(initial_humans, initial_vampires, nightly_kill, n_days):
    human_data = []
    vampire_data = []
    humans = initial_humans
    vampires = initial_vampires
    kill = nightly_kill
    
    for i in range(n_days):
        humans = humans - int(0.5*vampires)
        human_data.append(humans)
        vampires = int(1.5*vampires)-kill
        vampire_data.append(vampires)
        
    pyplot.plot(range(n_days),human_data)
    pyplot.xlabel('Days')
    pyplot.ylabel('Human Population (Blue)')
    pyplot.plot(range(n_days),vampire_data)
    pyplot.show()



tribble_table(100,10)
vampire_table(10000,6,2,10)
tribble_plot(100,10)
vampire_plot(10000,6,2,10)



