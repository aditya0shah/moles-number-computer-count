import math


mole = 602200000000000000000000
total = 79
spike_list = []


#There are 79 unique peaks in the number
def main():
  print(function(778578))
  # sum = 0
  # sum += even()
  # sum += peaks()
  
  print(sum)
  print(mole)
  #print(f"sum: {sum}")


def spike_list():
    for i in range(79):
        spike_list.append(2**i-1)
    



    


def even():
  return (mole / 2)

def function(x):
  spikes = "232 4 232 5 2324232 6 232423252324232"
  y = magic_decimal(x)
  if(y != int(y)):
    # Has decimal (Not a new spike)
    y = int(y)
    x2 = magic_spike(y)
    dif = x - x2
    if(dif%4 == 0):
      # Is a spike
      dif = dif/4
      l = math.log(dif, 2)
      if(l == int(l)):
        return l+2
      else:
        for a in range(1, int(l)+1):
          if(2^a > l): break
          if(l%(2^a) != 0):
            return a+1
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

#def odd():
  
  # 2^x - 1 is magic equation

  # so there is a pattern where for odd numbers, there is a spike after 2x+1 where x is prev number.
  # spike at 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047
  #return magic(k)


if __name__ == "__main__":
  main()

