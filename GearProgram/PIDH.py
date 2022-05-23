import numpy as np
import math
#from plotter import Plotter


#plotter = Plotter()


class HingePID:
    # PID for car hinges

    def __init__(self, P, I, D):
        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.t_prev = -0.1
        self.e_prev = 0
        self.I_prev = 0

    def HPID(self, t, current, target, ori):

        pt = np.array(target)
        pc = np.array(current)
        #print(pt, pc)
        p = ori.transpose() @ (pt - pc)
        #print(p)
        theta = math.atan2(p[1], p[0])
        #print(np.rad2deg(theta))
        #plotter.update(t, theta)
        e = theta

        P = self.Kp * e
        I = self.I_prev + self.Ki * e * (t - self.t_prev)
        D = self.Kd * (e - self.e_prev) / (t - self.t_prev)

        self.e_prev = e
        self.t_prev = t
        self.I_prev = I

        angle = P + I + D
        return angle
