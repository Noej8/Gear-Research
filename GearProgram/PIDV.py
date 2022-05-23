import math


class PID:

    def __init__(self, P, I, D):

        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.t_prev = -0.1
        self.e_prev = 0
        self.I_prev = 0

    def VPID(self, t, SP, PV):

        e = math.sqrt(math.pow((SP[0] - PV[0]), 2) + math.pow((SP[1] - PV[1]), 2))
        if e < .01 and e > 0:
            e = 0
        else:
            e = math.sqrt(math.pow((SP[0] - PV[0]), 2) + math.pow((SP[1] - PV[1]), 2))
        #print(e)

        P = self.Kp * e
        I = self.I_prev + self.Ki * e * (t - self.t_prev)
        D = self.Kd * (e - self.e_prev) / (t - self.t_prev)

        self.e_prev = e
        self.t_prev = t
        self.I_prev = I

        MV = P + I + D

        return MV