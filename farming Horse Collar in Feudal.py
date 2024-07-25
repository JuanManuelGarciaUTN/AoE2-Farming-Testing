woodSpend = 0
woodSpendHC = 0
farms = []
farmsHC = []
farmingSpeed = 20.3/60
villTimer = 25
timer = 0

class Farm():
    def __init__(self, food):
        self.initFood = food
        self.food = food
        self.building = True
        self.buildtime = 0

    def reset(self):
        self.food = self.initFood
        self.building = True
        self.buildtime = 0
    
for i in range(1500):
    if (timer % 25 == 0 and len(farms) < 16):
        farm = Farm(175)
        farmHC = Farm(250)
        farms.append(farm)
        farmsHC.append(farmHC)
        woodSpendHC += 60
        woodSpend += 60

    for o in farms:
        if (o.building):
            if o.buildtime == 14:
                o.building = False
            else:
                o.buildtime += 1
        else:
            if o.food > 0:
                o.food -= farmingSpeed
            else:
                o.reset()
                woodSpend += 60

    for o in farmsHC:
        if (o.building):
            if o.buildtime == 14:
                o.building = False
            else:
                o.buildtime += 1
        else:
            if o.food > 0:
                o.food -= farmingSpeed
            else:
                o.reset()
                woodSpendHC += 60
    
    if(timer % 60 == 0):
        minutos = int(timer / 60)
        if (minutos < 10):
            minutos = "0" + str(minutos)
        segundos = timer % 60
        if(segundos < 10):
            segundos = "0" + str(segundos)
        print("Time: ", minutos, ":", segundos, " | Wood Spend No HC: ", woodSpend, "  | Wood Spend HC: ", woodSpendHC, "Diff: ", (woodSpend - woodSpendHC))
    timer += 1

