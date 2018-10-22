#hexstring.py tt
def biocon(decimal):
	print(decimal)
	print("BIN ********")
	binstr = "" # binstr is a string
	for i in range (8):
		bin = decimal % 2
		decimal = decimal // 2
		#print(bin)
		binstr = binstr + str(bin)
		#print(binstr)
	print("-----")
	print(binstr)
	
	def hexcon(decimal):
		print(decimal)
		print(" HEX ********")
		# divident/divisor=quotient
		hexstr = ""
		#---------------------------------
		remainder = decimal % 16
		if (remainder == 10):
			remainder = "A"
		elif (remainder == 11):
			remainder ="B"
		elif (remainder == 12):
			remainder ="C"
		elif (remainder ==13):
			remainder ="D"
		elif (remainder == 14):
			remainder ="E"			
		elif (remainder == 15):
			remainder ="F"
		#-----------------------------------
		quotient = decimal //16
		if (quotient ==10):
			quotient = "A"
			if (quotient ==11):
				quotient = "B"
			if (quotient ==12):
				quotient = "C"
			if (quotient ==13):
				quotient = "D"
			if (quotient ==14):
				quotient = "E"
			if (quotient ==15):
				quotient = "F"
       #--------------------------------------
			#print (bin)
	hexstr = str(quotient)+"   "+str(remainder)
       #***************************************
       print("-----")
       print(hexstr)
       
       def main():
       print("INPUT -1  to EXIT THE PROGRAM")
       print(INPUT A POSTIVE INTEGER LESS THAN 256")
       done = 0
       while (done>= 0):
			dec = input("INPUT AN INTEGER : ")
			bincon(dec)
			hexcon(dec)
			print("done",done)
			done = dec
			
			
main()
