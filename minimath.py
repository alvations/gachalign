import math

def norm_cdf(z):
  """ Just in case you haven't installed scipy, use the norm distribution 
  functions as of Gale-Church'srcfile (1993). """
  # Equation 26.2.17 from Abramowitz and Stegun (1964:p.932)
  
  t = 1/float(1+0.2316419*z) # t = 1/(1+pz) , z=0.2316419
  probdist = 1 - 0.3989423*math.exp(-z*z/2) * ((0.319381530 * t)+ \
                                         (-0.356563782* math.pow(t,2))+ \
                                         (1.781477937 * math.pow(t,3)) + \
                                         (-1.821255978* math.pow(t,4)) + \
                                         (1.330274429 * math.pow(t,5)))
  return probdist

def norm_logsf(z):
  """ Take log of the survival fucntion for normal distribution. """
  try:
    return math.log(1 - norm_cdf(z))
  except ValueError:
    return float('-inf')