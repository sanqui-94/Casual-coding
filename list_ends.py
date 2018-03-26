
def listangar(a_list):
    """this method recives a list and returns the first an last elements as a list"""
    listanga = [a_list[0],a_list.pop()]
    return listanga

def main():
    """Test the script on a trivial way"""
    lista = [4,5,6,3,54,5,3,3,2]
    print listangar(lista)

if __name__ == '__main__':
    main()


