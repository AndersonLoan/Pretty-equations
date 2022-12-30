# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
## Name:    Andrew Spears
#           Ricardo Mejia
#           Saylor Sherrodd
#           Anderson Loan
#           Spencer Jones
#{ "b" if(A==0) else "" } {"-" if(B<0) else " +"}  {"" if (abs(B)==1) else abs(B)}x {"-" if(C<0) else " +"}  {abs(C)} = 0')
# Section:     574
# Assignment:   lab: 4.14
# Date:         9/8/2022

A=int(input('Please enter the coefficient A:'))
B=int(input(' Please enter the coefficient B:'))
C=int(input(' Please enter the coefficient C:'))
a = ""
b = ""
c = ""



a = (f'{"- " if(A<0) else ""}{"" if (abs(A)==1) else abs(A)}x^2') #A
b = (f'{" - " if(B<0) else " + "}{"" if (abs(B)==1) else abs(B)}x ') #B
c = (f'{" - " if(C<0) else "+ "}{abs(C)} ') #C

if(A == 0):
    a = ""
if(B == 0):
    b = ""
if(C == 0):
    c = ""
if( A != 0):
    print(" The quadratic equation is " + a + b + c + "= 0")
elif(B > 0 and A == 0):
    print(" The quadratic equation is " + str(B) + "x " + c + "= 0")
elif(B < 0):
    print(" The quadratic equation is " + a + b + c + "= 0")