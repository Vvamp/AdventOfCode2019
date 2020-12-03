file = open('input.txt', 'r')
lines = file.readlines() 
file.close()
import copy
lineA = lines[0]
lineB = lines[1] 

lineA_Directions = lineA.replace('\n', '').split(',')
lineB_Directions = lineB.replace('\n', '').split(',')
# print(lineA_Directions)

originPoint = (0,0)
lineA_Points = []
lineB_Points = []
curPoint = copy.deepcopy(originPoint)
curPointStepsA = [] 
curPointStepsB = [] 

# Find All Points For Line A
totalSteps = 1
for move in lineA_Directions:
    dir = move[0]
    steps = int(move[1:])
    for cur_step in range(1, steps+1):
        totalSteps += 1
        if dir == 'U':
            curPoint = (curPoint[0], curPoint[1]+1)
            curPointStepsA.append((curPoint[0], curPoint[1]+1, totalSteps))
        elif dir == 'D':
            curPoint = (curPoint[0], curPoint[1]-1)
            curPointStepsA.append((curPoint[0], curPoint[1]-1, totalSteps))

        elif dir == 'L':
            curPoint = (curPoint[0]-1, curPoint[1])
            curPointStepsA.append((curPoint[0]-1, curPoint[1], totalSteps))

        elif dir == 'R':
            curPoint = (curPoint[0]+1, curPoint[1])
            curPointStepsA.append((curPoint[0]+1, curPoint[1], totalSteps))

        else:
            raise IOError
            exit(1) 
        lineA_Points.append(curPoint)

# Find all points for line B
curPoint = copy.deepcopy(originPoint)
totalSteps = 1
for move in lineB_Directions:
    dir = move[0]
    steps = int(move[1:])
    for cur_step in range(1, steps+1):
        totalSteps += 1
        if dir == 'U':
            curPoint = (curPoint[0], curPoint[1]+1)
            curPointStepsB.append((curPoint[0], curPoint[1]+1, totalSteps))
        elif dir == 'D':
            curPoint = (curPoint[0], curPoint[1]-1)
            curPointStepsB.append((curPoint[0], curPoint[1]-1, totalSteps))

        elif dir == 'L':
            curPoint = (curPoint[0]-1, curPoint[1])
            curPointStepsB.append((curPoint[0]-1, curPoint[1], totalSteps))

        elif dir == 'R':
            curPoint = (curPoint[0]+1, curPoint[1])
            curPointStepsB.append((curPoint[0]+1, curPoint[1], totalSteps))

        else:
            raise IOError
            exit(1) 
        lineB_Points.append(curPoint)



matches = []
print("Points for line A: ", len(lineA_Points))
print("Points for line B: ", len(lineB_Points))
# print("Total Loops: ", len(lineA_Points)**len(lineB_Points))
# for x in lineA_Points:
#     if x in lineB_Points:
#         if x == (0,0):
#             continue
#         matches.append(x)

matches = set(lineA_Points).intersection(lineB_Points)

from math import *
 
def distance(point):
    return abs(point[0]) + abs(point[1])
print(matches)
print(matches)
results = []
betterresults = []
iindex = 0
for match in matches:
    print("Calculating ", match)
    pa = 0
    for pointstepA in curPointStepsA:
        if pointstepA[0:2] == match: 
            results.append(pointstepA[2])
            print("Found the match at line a with steps: ",pointstepA[2])
            pa = pointstepA[2]
            break
    for pointstepB in curPointStepsB:
        if pointstepB[0:2] == match: 
            results[iindex] += pointstepB[2] 
            print("Found the match at line b with steps: ",pointstepB[2])
            iindex += 1
            pb = pointstepB[2]

            break
    betterresults.append(pa + pb)

# print(min(results))
print(min(betterresults))
    


