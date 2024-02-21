import numpy
import matplotlib.pyplot as plotter
import Simulation
import seaborn

#Deffine some lists to hold the data
win_matrix = numpy.zeros((21,21))
diff_matrix = numpy.zeros((21,21))
the_thing = numpy.round(numpy.linspace(0,1,21),2)

def plotting(win,diff):
    plotter.figure()
    for row in win:
        plotter.plot(the_thing,row)
    plotter.xlabel("% of nations going Nukes")
    plotter.ylabel("Optimal Score")
    plotter.show()
    seaborn.heatmap(diff,center=0,xticklabels=(the_thing),yticklabels=the_thing)
    plotter.xlabel("Our Nuke %")
    plotter.ylabel("Their Nuke %")
    plotter.show()
    print(numpy.max(diff_matrix))
    print(diff_matrix[20][20])
    print(diff_matrix[10][10])
    

#simulation 1: two equal opponents with varying attack ratios
for i in range(0,21):
    for j in range(0,21):
        bad_guy_ratio = i/20
        good_guy_ratio = j/20
        outcome = Simulation.run_simulation(good_guy_ratio,bad_guy_ratio,60,60,1,1)
        win_matrix[i][j] = outcome[0]
        diff_matrix[i][j] = outcome[0] - outcome[1]
     
#plot it
plotting(win_matrix,diff_matrix)

#simulation 2: against a stronger opponent with varying attack ratios
for i in range(0,21):
    for j in range(0,21):
        bad_guy_ratio = i/20
        good_guy_ratio = j/20
        outcome = Simulation.run_simulation(good_guy_ratio,bad_guy_ratio,60,60,1,1,8000)
        win_matrix[i][j] = outcome[0]
        diff_matrix[i][j] = outcome[0] - outcome[1]

#plot it
plotting(win_matrix,diff_matrix)


#simulation 3: against a weaker opponent
for i in range(0,21):
    for j in range(0,21):
        bad_guy_ratio = i/20
        good_guy_ratio = j/20
        outcome = Simulation.run_simulation(good_guy_ratio,bad_guy_ratio,60,60,1,1,3000)
        win_matrix[i][j] = outcome[0]
        diff_matrix[i][j] = outcome[0] - outcome[1]
        
#plot it
plotting(win_matrix,diff_matrix)

#simulation 4: Similar Opponents, Firing more often
for i in range(0,21):
    for j in range(0,21):
        bad_guy_ratio = i/20
        good_guy_ratio = j/20
        outcome = Simulation.run_simulation(good_guy_ratio,bad_guy_ratio,20,60,(1/3),1)
        win_matrix[i][j] = outcome[0]
        diff_matrix[i][j] = outcome[0] - outcome[1]
     
#plot it
plotting(win_matrix,diff_matrix)

#simulation 5: Similar Opponents, Firing less often
for i in range(0,21):
    for j in range(0,21):
        bad_guy_ratio = i/20
        good_guy_ratio = j/20
        outcome = Simulation.run_simulation(good_guy_ratio,bad_guy_ratio,90,60,1,1)
        win_matrix[i][j] = outcome[0]
        diff_matrix[i][j] = outcome[0] - outcome[1]
     
#plot it
plotting(win_matrix,diff_matrix)