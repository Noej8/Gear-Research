import pybullet as p
from tclab import clock
import numpy as np
import math
from AstarAlg import Algorithm
from MapGen import Grids
from PIDV import PID
from PIDH import HingePID

p.connect(p.GUI)
p.setGravity(0, 0, -100)

g = Grids()
astar = Algorithm()
astar.main()

#Load in plane
rowcol = astar.g.rc
shapeSizes = astar.g.placedShapes
planeSize = astar.g.sizePlane
plane = p.loadURDF('simpleplane'+str(planeSize)+'.urdf')

#Load in boxes
newZero = [planeSize/2, planeSize/2]
index = 0
for z in shapeSizes:
    x = rowcol[index][0]-newZero[0]
    y = newZero[1]-rowcol[index][1]
    p.loadURDF('box'+str(z)+'.urdf', basePosition=[x, y, (z/2)])
    index += 1

#car
x1 = -newZero[0]+0.5
y1 = newZero[1]-0.5
car = p.loadURDF('simplecar.urdf', basePosition=[x1, y1, 0.1])
wheel_indices = [1, 3, 4, 5]
hinge_indices = [0, 2]
v = PID(200, .1, 300)
h = HingePID(1, 0, 0)
goal = [planeSize-1, planeSize-1]
path = astar.path
tfinal = 500

grid = astar.g.getGrid(1)
print(path)
for y, x in path[1:]:
    SPT = 2
    t = 0
    for t in clock(tfinal, .1):
        current, ori1 = p.getBasePositionAndOrientation(car)
        ori = np.array(p.getMatrixFromQuaternion(ori1)).reshape(3, 3)
        # target = [current[0], current[1], 0.1] if t < SPT else [x-newZero[0], newZero[1]-y, 0.1]
        target = [x-newZero[0], newZero[1]-y, 0.1]
        velocity = v.VPID(t, target, current)
        #print(t, SPT, target, current)
        #print(current, '\n', target, '\n', t, '\n')
        angle = h.HPID(t, current, target, ori)
        for joint_index in wheel_indices[::-1]:
            p.setJointMotorControl2(car, joint_index, p.VELOCITY_CONTROL, targetVelocity=velocity, force=5)
        for joint_index in hinge_indices:
            p.setJointMotorControl2(car, joint_index, p.POSITION_CONTROL, targetPosition=math.degrees(angle))
        p.stepSimulation()
        distance = math.sqrt(math.pow((target[0] - current[0]), 2) + math.pow((target[1] - current[1]), 2))
        #print(distance)
        if distance < 0.1:
            break
