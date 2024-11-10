
a=open("account.txt","r")
for record in a:
	 number, admin = record.split()
	 print ("The account number is %s and the surname of the account admin is %s"%(number ,admin))
	
	
a.close()
