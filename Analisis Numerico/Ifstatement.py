from math import atan, exp, log, radians, sqrt, tan, pow

#rango=[1,2]
##rango=[0, 1]
###rango=[.5,1]
####rango=[-2,-1]
rango=[-2, -1]
error=float(100)
prev=0
##preformula=(atan(0)+0-1)
#preformula=(exp(0-1)-log(abs(1)))
###preformula=float(((rango[0] ** 2)+1) ** .5)-tan(rango[0])
###formula=float(((rango[1] ** 2)+1)** .5)-tan(rango[1])
####preformula=(rango[0]**4)-1-(3*exp(0-rango[0]))
####formula=(rango[1]**4)-1-(3*exp(0-rango[1]))
preformula=((rango[0]**5)-rango[0]+3)
formula=((rango[1]**5)-rango[1]+3)
print("F(",rango[0],") = ",preformula,", F(",rango[1],") = ",formula)
#if (preformula > float(1) and formula < float(0)) or (preformula < float(1) and formula > float(1)):
while error > 1:
    x=((rango[0]+rango[1])/2)
###    formula=sqrt(pow(x,2)+1)-(tan(x))
#    formula=(exp(0-x)-log(abs(x)))
####    formula=(x**4)-1-(3*exp(0-x))
    formula=((x**5)-x+3)
    if formula < 0 and preformula > 0:
        rango[1]=x
    if formula > 0 and preformula < 0:
        rango[1]=x
    if formula > 0 and preformula > 0:
        rango[0]=x
    if formula < 0 and preformula < 0:
        rango[0]=x
    print("resultado de la formula en",x," es: ",formula)
    y=((rango[0]+rango[1])/2)
    error=float(abs((((y-x)/y)*100)))
    print(rango)
    print ("rango de error: ",error,"%")
#    preformula=(exp(0-rango[0]-log(abs(rango[0]))))
###    preformula=sqrt(pow(rango[0],2)+1)-(tan(rango[0]))
####    preformula=(x**4)-1-(3*exp(0-x))
    preformula=((rango[0]**5)-rango[0]+3)
x=((rango[0]+rango[1])/2)
print(x)
formula=((x**5)-x+3)
###formula=sqrt(pow(x,2)+1)-(tan(x))
if formula < 0 and preformula > 0:
    rango[1]=x
if formula > 0 and preformula < 0:
    rango[1]=x
if formula > 0 and preformula > 0:
    rango[0]=x
if formula < 0 and preformula < 0:
    rango[0]=x
print (formula)
print(rango)