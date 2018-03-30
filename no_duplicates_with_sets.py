def delete_duplicates(a_list):
    """this function will recive a list as parameter, then it will remove
    every duplicate inside that list, we will be using sets on this one"""
    a_set = set()
    for i in a_list:
    	a_set.add(i)
    return list(a_set)


def main():
	print "Please, introduce a list of things you want:"
	raw_list = raw_input("> ")
	a_list = raw_list.split()
	print "your new list would be this:"
	print delete_duplicates(a_list)


if __name__ == '__main__':
	main()
