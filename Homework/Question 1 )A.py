#Making a list of graduated students
graduation =["Ali" ,"Maxim" , "Alaa" , "Basel0 "," Sara" , "Diana"]

#Enter the student name
name =input("Enter the student name :")

#Check if the entered name is in the graduated list of students

if name in graduation :
	print(name ,"Isgraduated")
else :
	print(name , "Not graduated")