import math
def equation(a,b,c):
    delta=(b**2)-(4*a*c)
    if delta>0 :
        answers=[]
        answers.append((-b-math.sqrt(delta))/(2*a))
        answers.append((-b+math.sqrt(delta))/(2*a))
        return answers
    elif delta==0:
        return -b/(2*a)
    else:
        return "There is no answer!"
    

a=float(input("Enter the a (x^2 factor): "))
b=float(input("Enter the b (x factor): "))
c=float(input("Enter the c (constant coefficient): "))

print(equation(a,b,c))

