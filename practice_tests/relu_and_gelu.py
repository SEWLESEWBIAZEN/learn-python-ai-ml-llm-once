import numpy as np

def relu(x):
   output = np.maximum(0,x)
   print(output)
   return output

def gelu(x):   
   tan_sqrt = np.tanh(np.sqrt(2 / np.pi))
   x_pwr = ( x + (0.044715 * np.power(x,3))) 
   output = 0.5 * x * (1 + tan_sqrt * x_pwr)
   print(output)
   return output

# for testing purpose
relu(-1)
gelu(-1)