def fibo(quantity):
    """ this fuction takes a quantity number as parameter, then it generates that amount of fibonacci numbers and returns them on a list"""
    fibo_series = []
    a = 0
    b = 1
    i = 0
    while i < quantity:
        if i == 0:
            fibo_series.append(1)
        else:
            fibo_series.append(a + b)
            a = b
            b = fibo_series[-1]
        i += 1
    return fibo_series


def main():
    print "So, how many fibonacci numbers would you like to be generated?"
    quantity = int(raw_input("> "))
    print fibo(quantity)


if __name__ == '__main__':
    main()
