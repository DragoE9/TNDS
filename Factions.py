import math

class Faction:
    """
    Class Representing a N-Day Faction
    """
    def __init__(self,att_freq:int,nuke_ratio:float,attack_commit:float,num_nations:int=5000,nukes:int=0,sheilds:float=0,score:int=0,radiation:float=0,elapsed_time:int=0,attack:bool=False):
        """
        num_nations: the number of nations in the faction (int)
        nukes: the number of nukes the faction has (int)
        sheilds: the number of sheilds the faction has (int)
        score: faction score (float)
        radiation: faction radiation (float)
        production: faction available production (int)
        att_freq: the amount of minutes the faction waits between attacks (int)
        nuke_ratio: the fraction of it's production the faction commits to nukes, between 0 and 1 (float)
        attack_commit: the fraction of it's nukes the faction sends in each volley, between 0 and 1 (float)
        elapsed_time: the time that has elapsed since last attack, in minutes (int)
        attack: Weather or not the faction will launch an attack this timestep (bool)
        """
        self.num_nations = num_nations
        self.nukes = nukes
        self.sheilds = sheilds
        self.score = score
        self.radiation = radiation
        self.production = num_nations*10
        self.att_freq = att_freq
        self.nuke_ratio = nuke_ratio
        self.attack_commit = attack_commit
        self.elapsed_time = elapsed_time
        self.attack = attack
        
    def do_purchase(self):
        """
        Call this method to have the faction convert its production into stuff
        """
        self.nukes += math.floor((self.production*self.nuke_ratio)/2.75)
        self.production -= math.floor(self.production*self.nuke_ratio)
        self.sheilds += math.floor(self.production/5.5)
        self.production = 0
    
    def do_timestep(self,delta_t):
        """
        Call this method to increment the time, and decide weather or not to attack
        """
        self.elapsed_time += delta_t
        if self.elapsed_time >= self.att_freq:
            self.attack = True
            self.elapsed_time = 0
            
    def conclude_attack(self):
        """
        To be called once a faction finishes its attack to reset it's attack value
        """
        self.attack = False
        
    def get_production(self):
        """
        faction gains production
        """
        self.production += 15*(self.num_nations - math.floor(0.005*self.radiation))
        
    def launch(self):
        """
        Attack an enemy faction
        Returns number of launches missiles
        """
        launches = math.floor(self.nukes*self.attack_commit)
        self.nukes -= launches
        return launches
    
    def deffend(self,incoming):
        """
        Removes sheilds from faction in response to sheilding action
        """
        self.sheilds -= incoming
        
    def suffer(self,hits):
        """
        The faction suffers hits
        """
        self.radiation += 0.25*hits
        self.score -= (0.25*0.25)*hits
        
    def land_hits(self,hits):
        self.score += hits
        
def attack(attacker,defender):
    """
    Function which resolves attacks when they occur
    """
    launches = attacker.launch()
    if launches >= defender.sheilds:
        hits = launches - defender.sheilds
        defender.deffend(defender.sheilds)
        defender.suffer(hits)
        attacker.land_hits(hits)
    else:
        defender.deffend(launches)