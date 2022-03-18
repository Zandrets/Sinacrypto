from math import log, exp, cos, sin
from numpy import arctan
error=float(100)
##x=1
###x=.5
x=3
#formula=(exp(0-x)-log(abs(x)))
#formula_dev=(0-exp(0-x)-(1/x))
##formula=(cos(x))-x
##formula_dev=(0-sin(x)-1)
###formula=1-(x ** 2)-(arctan(x))
###formula_dev=0-(2*x)-(1/(1+(x ** 2)))
formula=(x**3)-(4*(x**2))-2
formula_dev=(3*(x**2))-(8*x)
print("F(", x,")=",formula,", F'(",x,")=",formula_dev)
while error > 1:
    prev_x=x
#    formula=(exp(0-x)-log(abs(x)))
#    formula_dev=(0-exp(0-x)-(1/x))
##    formula=cos(x)-x
##    formula_dev=(0-sin(x)-1)
###    formula=1-(x ** 2)-(arctan(x))
###    formula_dev=0-(2*x)-(1/(1+(x ** 2)))
    formula=(x**3)-(4*(x**2))-2
    formula_dev=(3*(x**2))-(8*x)
    print("F(", x,")=",formula,", F'(",x,")=",formula_dev)
    x=x-(formula/formula_dev)
    print("nueva X es: ",x)
    error=(abs((x-prev_x)/x))*100
    print("error: ",error,"%")