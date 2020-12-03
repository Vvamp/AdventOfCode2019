import math 
file = open('input.txt', 'r')
lines = file.readlines() 
file.close()

sum = 0
for line in lines:
    if line.replace('\n', '') == '':
        continue
    modules_mass = int(line)

    fuel_required =  math.floor(modules_mass / 3) - 2
    if fuel_required < 0:
        fuel_required = 0
    else:
        lines.append(str(fuel_required))
    sum += fuel_required
print("Total Fuel Needed: ", sum)