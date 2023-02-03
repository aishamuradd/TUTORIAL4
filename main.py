name=(input("What is your name?"))#asks for the name
print("Hello",(name.capitalize()),"I will help solve your quadratic :)")#capitalizes the name
a=float(input("what is your a in ax^2+bx+c=0 ?"))#to enter the value of "a"
b=float(input("what is your b in ax^2+bx+c=0 ?"))#to enter the value of "b"
c=float(input("what is your c in ax^2+bx+c=0 ?"))#to enter the value of "c"
d=((-b-(((b**2)-4*(a*c))**(1/2)))/(2*a))#negative
e=((-b+(((b**2)-4*(a*c))**(1/2)))/(2*a))#postive
print("Thank you",(name.capitalize()),"the roots are",d,"and",e,)#shows the results
quit()