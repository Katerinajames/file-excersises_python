import os
a=open("account.txt","r")
temp = open("temp_file.txt", 'w')
for record in a:
	number, admin = record.split()
	if number!="100":
		       temp.write(record) 
	else:
		new_record = " ".join([number, "Williams"])
		temp.write(new_record + '\n')
        
os.remove("account.txt")		
os.rename("temp_file.txt", "account.txt")		        
                    
     
    
          

              

          
	
	
a.close()
