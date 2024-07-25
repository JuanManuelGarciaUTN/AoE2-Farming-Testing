woodSpend = 0
woodSpendHC = 0
farms = []
farmsHC = []
farmingSpeed = 20.3/60
villTimer = 25
timer = 540

class Farm():
    def __init__(self, food):
        self.initFood = food
        self.food = food
        self.building = True
        self.buildtime = 0

    def reset(self, food):
        self.food = food
        self.building = True
        self.buildtime = 0
    
for i in range(3500):
    if (timer % 25 == 0 and (len(farms) < 16 or timer > 1180)):
        farm = Farm(175)
        if(timer > 1180):
            farmHC = Farm(375)
        else:
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
                o.reset(175)
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
                if (timer > 1180):
                    o.reset(375)
                else:
                    o.reset(250)
                woodSpendHC += 60
    
    if(timer % 60 == 0):
        minutos = int(timer / 60)
        if (minutos < 10):
            minutos = "0" + str(minutos)
        segundos = timer % 60
        if(segundos < 10):
            segundos = "0" + str(segundos)
        mensaje = "Wood Spend HC: "
        if(timer > 1180):
             mensaje = "Wood Spend HP: "
        print("Time: ", minutos, ":", segundos, mensaje, woodSpendHC, "Diff: ", (woodSpend - woodSpendHC))
    timer += 1

