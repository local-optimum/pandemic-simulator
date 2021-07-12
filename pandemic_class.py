import math

class Pandemic(object):
    def __init__(self, r, ifr, gent, pop = 1000000):
        #reproduction number
        self.r = r
        #infection fatality rate
        self.ifr = ifr
        #generation time
        self.generationTime = gent
        #population size
        self.pop = pop
        #epidemic growth rate (little r)
        self.growthRate = (self.r -1)/self.generationTime
        #herd immunity
        self.herd = 1-(1/self.r)
        #timestamp
        self.timestamp = 0
        #doubling time
        self.doubleTime = math.log(2)/self.growthRate

    def get_herd(self):
        return self.herd

    def get_growthRate(self):
        return self.growthRate
    
    def get_doubleTime(self):
        return self.doubleTime
    
    def __str__(self):
        return f"""\nPandemic with R rate: {self.r}\nInfection fatality rate: {self.ifr}\nGeneration time: {self.generationTime}\nFor Population Size: {self.pop}\n"""

    def reach_herd(self):
        return math.log(self.pop*self.herd,2)*self.doubleTime


covid = Pandemic(2.5, 0.0049, 5, 70000000)

print("\n\n\nCOVID MODELLING")
print(covid)
print(f"Population Percentage Infection for Herd Immunity: {str(covid.get_herd()*100)}%")
print(f"Natural Days for Cases to Double: {round(covid.get_doubleTime(),1)}")
print(f"Time taken to reach herd immunity is: {round(covid.reach_herd())} days")
print(f"Reaching herd immunity would result in: {round(covid.pop*covid.herd*covid.ifr)} deaths")
print()
print()