import math

file = open("module.txt")
sum = 0
for line in file:
    fuelMass = math.floor(float(line)/3) - 2
    sum += math.floor(float(line) / 3) - 2
    while fuelMass > 0:
        fuelMass = math.floor(float(fuelMass) / 3) - 2
        if fuelMass > 0:
            sum += fuelMass
print(sum)