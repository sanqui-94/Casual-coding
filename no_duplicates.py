def delete_duplicates(a_list):
	"""This function recives a list, it returns a new list based on the original list but without the duplicate elements of it"""
	new_list = []
	for i in a_list:
		if not i in new_list:
			new_list.append(i)
	return new_list

def main():
	print "Please, introduce a list of things you want:"
	raw_list = raw_input("> ")
	a_list = raw_list.split()
	print "your new list would be this:"
	print delete_duplicates(a_list)

if __name__ == '__main__':
	main()