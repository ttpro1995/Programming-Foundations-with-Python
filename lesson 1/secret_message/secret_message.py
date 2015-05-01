import os  

# get file name
list_file = os.listdir("D:\Python\Programming Foundations with Python\lesson 1\secret_message\prank")

print (list_file)

# for each file 
	#rename
os.chdir("D:\Python\Programming Foundations with Python\lesson 1\secret_message\prank") # change working directory
for i in list_file:
        old_name=i
        new_name=i.translate(None,"0123456789")
        os.rename(old_name,new_name)
        print ("change "+old_name+" to "+ new_name)
                
