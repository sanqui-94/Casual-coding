import random


def main():
    """This script generates random numbers and asks to the user to guess the 
    generated number"""
    print "Hello there, it's time for you to guess numbers, ready?"
    print "Try to guess the number i'm thinking"

    while True:  # uuhh a forbiden loop
        r_input = raw_input("> ")
        if r_input == 'exit':
            break
        else:
            number = int(r_input)
            random_number = random.randint(1, 9)
            if number == random_number:
                print "exactly right"
            elif number > random_number:
                print "too high"
            else:
                print "too low"
    print "Bye bye"

if __name__ == '__main__':
    main()
