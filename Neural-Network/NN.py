import math
class Perceptron:
    def __init__(self, w, b, a, th):
        self.w = w  # Weights
        self.b = b  # Bias
        self.a = a  # Learning Rate
        self.th = th    # Threshold
    
    def weighted_sum(self, x):
        yin = self.b
        for i in range(len(x)):
            yin += self.w[i] * x[i]
        return round(yin, 3)
    
    def print_wb(self):
        print("Weights ", end="")
        for i in range(len(self.w)):
            print(f"w{i} = {self.w[i]}", end=" ")
        print(f"Bias b = {self.b}")
    
    def update_wb(self, x, t):
        for i in range(len(x)):
            self.w[i] = self.w[i] + (self.a * t * x[i])
        self.b = self.b + self.a * t
    
    def binary(self, yin):
        if(yin >= self.th):
            return 1
        else:
            return 0
        
    def bipolar(self, yin):
        if(yin >= self.th):
            return 1
        else:
            return -1
    
    def sigmoid(self, yin):
        val = 1/(1+ math.exp(-yin))
        if(val >= self.th):
            return 1
        else:
            return 0
        
    def train(self, x, t, epochs):
        for j in range(epochs):
            print(f"==========Epoch {j+1}==========")
            for i in range(len(x)):
                print(f"Input = {x[i]}")
                yin = self.weighted_sum(x[i])
                # y = self.binary(yin)
                y = self.bipolar(yin)
                # y = self.sigmoid(yin)
                print(f"yin = {yin} | y = {y} | target = {t[i]}")
                if(y==t[i]):
                    print("No updation, ", end="")
                    self.print_wb()
                else:
                    self.update_wb(x[i], t[i])
                    print("Weights updated, ",end="")
                    self.print_wb()
                print()
            print("================================\n\n")
        print("==========Perceptron trained==========")
        print("** Final weights are, ",end = "")
        self.print_wb()
        print("======================================")

# Inputs

# Sample input 1
# w = [0, 0, 0, 0]
# b = 0
# a = 1
# th = 0
# x = [[-1,-1,1,1],[-1,-1,-1,1],[1,-1,1,-1],[1,1,-1,-1]]
# t = [-1,-1,1,1]
# epochs = 2

# AND Gate - Bipolar inputs and outputs
# Use bipolar activation function
w = [0.3, 0.4]
b = 0
a = 1
th = 0
x = [[-1,-1],[-1,1],[1,-1],[1,1]]
t = [-1,-1,-1,1]
epochs = 3

p1 = Perceptron(w, b, a, th)
p1.train(x, t, epochs)

# OR Gate - Binary inputs and outputs
# Use binary activation function
w = [0, 0]
b = 0
a = 0.5
th = 1
x = [[0,0],[0,1],[1,0],[1,1]]
t = [0,1,1,1]
epochs = 3

p2 = Perceptron(w, b, a, th)
p2.train(x, t, epochs)