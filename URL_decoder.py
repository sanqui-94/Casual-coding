# Diccionario para realizar la traduccion, convierte los codigos ASCII en notacion hexadecimal a su representacion en caracteres. 
Dic = {'41': 'A', '42': 'B', '43': 'C', '44': 'D', '45': 'E', '46': 'F', '47': 'G', '48': 'H', '49': 'I','4A': 'J', '4B': 'K', '4C': 'L','4D': 'M', '4E': 'N',
 '4F': 'O', '50': 'P', '51': 'Q', '52': 'R','53': 'S', '54': 'T','55': 'U', '56': 'V', '57': 'W', '58': 'X','59': 'Y', '5A': 'Z',
 '61': 'a', '62': 'b', '63': 'c', '64': 'd', '65': 'e', '66': 'f', '67': 'g', '68': 'h', '69': 'i','6A': 'j', '6B': 'k', '6C': 'l', '6D': 'm', '6E': 'n',
 '6F': 'o', '70': 'p', '71': 'q', '72': 'r', '73': 's', '74': 't', '75': 'u', '76': 'v', '77': 'w', '78': 'x', '79': 'y', '7A': 'z',
 '30': '0', '31' : '1', '32' : '2', '33' : '3', '34' : '4', '35' : '5', '36' : '6', '37' : '7', '38' : '8', '39' : '9',
 '20' : ' ', '21' : '!', '23' : '#', '24' : '$', '25' : '%', '26' : '&', '28' : '(', '29' : ')', '2A' : '*', '2B' : '+', '2D' : '-', '2E' : '.',  '2F' : '/', 
 '3A' : ':', '3C' : '<', '3D' : '=', '3E' : '>', '3F' : '?', '40' : '@', '5B' : '[' , '5D' : ']', '5E' : '^', '7B' : '{', '7D' : '}'}



entrada = raw_input("Introduce the String (encoded) you want to decode.\n") # we recive the desired string to decode.

#l = []
#flag = False #boolean flag used for appending the hex codes that will be decoded. 
#aux = "" #auxiliar string, it will be used as a container.
#
#for c in entrada:
#	aux = aux + c
#	if flag:
#
#		l.append(aux)
#		aux = ""
#		flag = False
#	else:
#		flag = True
#
#for x in l:
#	print Dic[x],

entrada2 = entrada.split(" ")

for x in entrada2:
	print Dic[x],