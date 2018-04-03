import random

def password_generator():
    """This method will be in charge of generating the random passwords"""
    password = ''
    for i in xrange(7):
        password += chr(random.randint(33, 126))
    
    return password


def main():
    print "Hello, on this occasion we will be serving as a Password Generator"
    while True:  # Another forbiden loop
        print "Do you want a random Password"
        input_ = raw_input("(Y/N)\n")

        if input_ == 'Y':
            input_2 = raw_input("Do you need a Strong Password?(Y/N)\n")
            if input_2 == 'Y':
                strong_password = password_generator() + password_generator()
                print "This is your Strong password"
                print "%s" % strong_password
            else:
                print "This is your generated password"
                print "%s" % password_generator()
        else:
            print "Bye bye"
            break

if __name__ == '__main__':
    main()
