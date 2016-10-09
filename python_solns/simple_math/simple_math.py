# simple_math.py

def main():
    x = managed_input(int)
    y = managed_input(int)
    operation_summary(x,y)

def add(x,y):
    return x + y


def sub(x,y):
    return x - y

def multi(x,y):
    return x * y

def div(x,y):
    if y == 0:
        return 'N/A'
    else:
        return int(x/y)

def managed_input(data_type):
    inp = ''
    while not is_integer(inp):
        inp = raw_input("Please input a number")
    return int(inp)

def is_integer(strint):
    if len(strint) == 0:
        return False
    if strint[0] == '-':
        return strint[1:].isdigit()
    else:
        return strint.isdigit()

def operation_summary(x, y):
    print("{} + {} = {}".format(x, y, add(x,y)))
    print("{} - {} = {}".format(x, y, sub(x,y)))
    print("{} * {} = {}".format(x, y, multi(x,y)))
    print("{} / {} = {}".format(x, y, div(x,y)))

if __name__ == "__main__":
    main()
