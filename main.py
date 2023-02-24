import math

#mole = 602200000000000000000000
total = 79 # Total amount of new spikes
mghz = 100
speed = mghz*100000000
#spike_list = []

def main():
  print(decimalToBinaryOperations(33319))

def decimalToBinaryOperations(x):
  if(x%2==0): return 1
  
  y = magic_decimal(x)
  if(y != int(y)):
    # Has decimal (Not a new spike)
    y = int(y)
    x2 = magic_spike(y)
    dif = x - x2
    if(dif%4 == 0):
      # Is a spike
      done = False
      dif = dif/4
      l = math.log(dif, 2)
        
      while not done:
        if(l == int(l)):
          done = True
          break
        dif = dif - 2**(int(l))
        l = math.log(dif, 2)
      
      l=math.log(dif, 2)
      return l+2
    else:
      # Not a spike
      return 1
  else:
    # No decimal
    return y

def magic_spike(x):
  #given a spike value, it will return the position that happens in
  return 2**x - 1

def magic_decimal(x):
  return (math.log(x+1) / math.log(2))



if __name__ == "__main__":
  main()

