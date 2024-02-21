import Factions

def run_simulation(good_nuke_ratio,bad_nuke_ratio,good_attack_interval,bad_attack_interval,good_attack_commit,bad_attack_commit,enemy_nations=5000,stop_time=1440):
    """
    Runs the simulation
    Returns a tuple of the following information
        score of the good guys: float
        score of the bad guys: float
    """
    #Deffine the variables and the factions
    good_guys = Factions.Faction(good_attack_interval,good_nuke_ratio,good_attack_commit)
    bad_guys = Factions.Faction(bad_attack_interval,bad_nuke_ratio,bad_attack_commit,num_nations=enemy_nations)
    t = 0
    dt = 2
    while t <= stop_time:
        #Production Happens
        good_guys.get_production()
        bad_guys.get_production()
        good_guys.do_purchase()
        bad_guys.do_purchase()
        #Attacks Occur and Resolve, if necessary
        if good_guys.attack == True:
            Factions.attack(good_guys,bad_guys)
            good_guys.conclude_attack()
        if bad_guys.attack == True:
            Factions.attack(bad_guys,good_guys)
            bad_guys.conclude_attack()
        #If one faction is dead, end simulation    
        if good_guys.radiation == good_guys.num_nations*100 or bad_guys.radiation == bad_guys.num_nations*100:
            break
        #Otherwise, do the timestep
        t += dt
        good_guys.do_timestep(dt)
        bad_guys.do_timestep(dt)
    #Report the final values
    return (good_guys.score,bad_guys.score)

if __name__ == "__main__":
    print(run_simulation(0.5,0.5,60,60,1,1))