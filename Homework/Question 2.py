#Definig a function which convert the decimal number to binary
def DecimalToBinary(num) :
	if num>=1 :
		DecimalToBinary(num//2)
		print(num%2 , end =" ")
#Running the program
if __name__ =='__main__' :
	x = int (input("Enter a number :"))
	DecimalToBinary(x)