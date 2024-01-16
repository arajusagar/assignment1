a=input() #get input from  user
length_of_a=len(a)-1 #finding length of input and subtracting 1
remove_char=a[:length_of_a-2] 
resultant=remove_char+a[length_of_a-1]
print(resultant[::-1]) #printing reverse
# performing arthimetic operation as follows
b=int(input("enter the number1 "))
c=int(input("enter the number2 "))
print("sum of b and c is ",b+c)
print("subtraction of b and c is ",b-c)
print("multiplication of b and c is ",b*c)
print("division of b and c is ",b/c)