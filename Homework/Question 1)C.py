#The given names
L =["Network" , "Maths" ,"Programming" ,"Physics" , "Music"]

#Define the wanted letter in the givven words
check = 'P'
#Printing the original list
print("The original list" + str(L))
result =[elem for elem in L if elem[0].lower() ==check.lower()]
#After checking the condition , printing the result
print("The matching with the P letter : " + str(result))