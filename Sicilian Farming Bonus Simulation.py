import matplotlib.pyplot as plt
import numpy as np

woodSpend = 0
woodSpendHC = 0
woodSpeendSicilianHc = 0
farms = []
farmsHC = []
farmsSicilianHc = []
farmingSpeed = 20.3/60
villTimer = 25
timer = 540
timerAt16Vills = 0
xTimer = []
yNoHcWoodSpend = []
yHcWoodSpend = []
ySicilianHcWoodSpeend = []
yDiffSicilianNoHc = []
yDiffSicilianHc = []
xTicks = []

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
    
for i in range(2400):
    if (timer % 25 == 0 and (len(farms) < 16 or timer > 1180) and len(farms) < 65):
        farm = Farm(175)
        farmHC = Farm(250)
        farmSicilianHc = Farm(344)

        farms.append(farm)
        farmsHC.append(farmHC)
        farmsSicilianHc.append(farmSicilianHc)

        woodSpendHC += 60
        woodSpend += 60
        woodSpeendSicilianHc += 60
    else:
        if len(farms) == 16 and timerAt16Vills == 0:
            timerAt16Vills = timer
        elif timerAt16Vills + 75 == timer:
            farmingSpeed = 23/60

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
                o.reset(250)
                woodSpendHC += 60

    for o in farmsSicilianHc:
        if (o.building):
            if o.buildtime == 14:
                o.building = False
            else:
                o.buildtime += 1
        else:
            if o.food > 0:
                o.food -= farmingSpeed
            else:
                o.reset(344)
                woodSpeendSicilianHc += 60
    
    if(timer % 1 == 0):
        minutos = int(timer / 60)
        if (minutos < 10):
            minutos = "0" + str(minutos)
        segundos = timer % 60
        if(segundos < 10):
            segundos = "0" + str(segundos)
        mensaje = "Wood Spend HC: "
        xTimer.append((str(minutos)+ ":"+ str(segundos)))
        yNoHcWoodSpend.append(woodSpend)
        yHcWoodSpend.append(woodSpendHC)
        ySicilianHcWoodSpeend.append(woodSpeendSicilianHc)
        yDiffSicilianNoHc.append(woodSpend - woodSpeendSicilianHc)
        yDiffSicilianHc.append(woodSpendHC - woodSpeendSicilianHc)
        if(timer % 120 == 0):
            xTicks.append((str(minutos)+ ":"+ str(segundos)))

    timer += 1

#plt.plot(xTimer,yNoHcWoodSpend, label="No Hc")
#plt.plot(xTimer,yHcWoodSpend, label="Hc")
#plt.plot(xTimer,ySicilianHcWoodSpeend, label="Sicilian")
plt.plot(xTimer, yDiffSicilianHc, label="Difference vs Hc")
plt.plot(xTimer, yDiffSicilianNoHc, label="Difference vs No Hc")
plt.xticks(xTicks)
plt.yticks(np.arange(0,5800,250))
plt.grid(axis="y")
plt.xlabel("In Game Time")
plt.ylabel("Wood Speend")
plt.title("Comparison Farming vs Sicilian Bonus")
plt.legend()

plt.show()

