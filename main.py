mole = 602200000000000000000000
k = 1000


def main():
  sum = 0
  #sum += even()
  sum += odd()
  print(sum)
  #print(f"sum: {sum}")


def even():
  return (mole / 2)


def magic(x):
  #given a spike value, it will return the position that happens in
  return 2**x - 1


def odd():
  
  # 2^x - 1 is magic equation

  # so there is a pattern where for odd numbers, there is a spike after 2x+1 where x is prev number.
  # spike at 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047
  return magic(k)


if __name__ == "__main__":
  main()
