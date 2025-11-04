import math
from scipy.stats import norm

class BlackScholes:
    # s = stock price
    # x = exercise price
# r = risk-free interest rate
# t = time to experation
# o = standerd deviation of log returns or (volitility)
    # m = mode. E.g Eu, USA

    def __init__(self, s, x, r, t, o, m):
        self.s = s
        self.x = x 
        self.r = r
        self.t = t
        self.o = o
        self.m = m
    
    def __str__(self):
        print("--Results--")
        print(f"d1: {d1:.6f}")
        print(f"d2: {d2:.6f}")
        print(f"Call Price: ${c:.2f}\n")
 
        
    def EUOptionCall(self):
        d1 = self.d1(self.s, self.x, self.r, self.t, self.o)
        d2 = self.d2(d1)
        c = self.s * self.N(d1) - self.x * math.exp(-self.r * self.t) * self.N(d2)
        return c
    
    @staticmethod
    def impliedVolitlity(marketPrice, s, x, r, t):
        #This seems extremely hard to divmoa
        TOLERANCE = 0.0001
        lowV = 0.0001
        highV = 5.0
        maxInterations = 1000
        
        for i in range(maxInterations):
            midV = (highV + lowV)/2
            model = BlackScholes(s, x, r, t, o = midV, m = 'EU')

            estPrice = model.main()

            estV = estPrice - marketPrice

            if(abs(estV) < TOLERANCE):
                return midV
            
            if(estV > 0):
                highV = midV
            
            elif(estV < 0):
                lowV = midV

        return 0

    def N(self, x): #N(x) from the formula
        return norm.cdf(x)

    def d1(self, s, x, r, t, o):
        return (math.log(s/x) + (r + (o**2)/2) * t)/(o * math.sqrt(t))

    def d2(self, d1):
        return d1 - (self.o * math.sqrt(self.t))

    def main(self):
        if(self.m == 'EU'):
            return self.EUOptionCall()
        return 0
        
if __name__ == '__main__':
    obj = BlackScholes()
    obj.main()
