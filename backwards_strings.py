def reverser(a_list):
    """This function will reverse a list"""
    words_reversed = []
    for word in xrange(len(a_list)):
    	words_reversed.append(a_list[-word - 1])
    return words_reversed

def main():
    print "Now you should input a string, the order of the words will be reversed"
    le_input = raw_input("> ").split()
    print "The result is this!"
    print reverser(le_input)


if __name__ == '__main__':
    main()
