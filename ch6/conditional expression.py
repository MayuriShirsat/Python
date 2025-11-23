# conditional statements
# IF ELIF ELSE ladder
a=int(input("Ener your age:"))

if(a%2==0):
    print("This is an even no.")


if(a>=18):
    print("you are an adult")
    print("you can drive")
# if indentation(extra spacing before starting of line) is present then we are inside the if
elif(a<0):
    print("Enter valid age")

elif(a==0):
    print("0 is not an age")    

else:
    print("Yor are not an adult")

print("End of program")    