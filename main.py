mole = 602200000000000000000000


def main():
    sum = 0
    sum += even()
    sum += odd()
    print(sum)

def even():
    return (mole/2)

def odd():
    # so there is a pattern where for odd numbers, there is a spike after a set of numbers.
    # for example
    return 0 


if __name__ == "__main__":
    main()