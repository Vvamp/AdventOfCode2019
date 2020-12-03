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

# Find All Points For Line A
for move in lineA_Directions:
    dir = move[0]
    steps = int(move[1:])
    for cur_step in range(1, steps+1):
            if dir == 'U':
                curPoint = (curPoint[0], curPoint[1]+1)
            elif dir == 'D':
                curPoint = (curPoint[0], curPoint[1]-1)
            elif dir == 'L':
                curPoint = (curPoint[0]-1, curPoint[1])
            elif dir == 'R':
                curPoint = (curPoint[0]+1, curPoint[1])
            else:
                raise IOError
                exit(1) 
            lineA_Points.append(curPoint)

# Find all points for line B
curPoint = copy.deepcopy(originPoint)
for move in lineB_Directions:
    dir = move[0]
    steps = int(move[1:])
    for cur_step in range(1, steps+1):
            if dir == 'U':
                curPoint = (curPoint[0], curPoint[1]+1)
            elif dir == 'D':
                curPoint = (curPoint[0], curPoint[1]-1)
            elif dir == 'L':
                curPoint = (curPoint[0]-1, curPoint[1])
            elif dir == 'R':
                curPoint = (curPoint[0]+1, curPoint[1])
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


results = []

for match in matches:
    results.append(distance(match))

print("Shortest manhattan distance: ", end="")
print(min(results))
    


