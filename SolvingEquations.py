from math import *

def eq(x):
    return (x**3) - (3*x**2) - (3*x) - 4
    #return sin(10*x) + cos(3*x)

def eq_(x):
    return (3*(x**2)) - (6*x) - 3

def bisection():
    x1 = 420
    x2 = 69
    if eq(x1)*eq(x2) < 0:
        while True:
            b = (x1+x2)/2
            if eq(b) > 0:
                if eq(x1) > 0:
                    x1 = b
                if eq(x1) < 0:
                    x2 = b
            if eq(b) < 0:
                if eq(x1) > 0:
                    x2 = b
                if eq(x1) < 0:
                    x1 = b
            elif abs(eq(b)) < (10**-8):
                print(b)
                break
    else:
        print("Enter different values")

def NewtonRaphson():
    x1 = 69
    while abs(eq(x1)) > (10**-6):
        x1 = x1 - (eq(x1)/eq_(x1))
    
    print(x1)

def eq1(x,y):
    return (x**2) + (x*y) - 10

def eq1_x(x,y):
    return (2*x) + y

def eq1_y(x,y):
    return x

def eq2(x,y):
    return (y**2) + (3*x)*(y**2) - 63

def eq2_x(x,y):
    return 3*(y**2)

def eq2_y(x,y):
    return (2*y) + (6*x*y)

def TwoVariables():
    x0 = 420
    y0 = 69
    tol = (10**-6)
    while (abs(eq1(x0,y0)) > tol) and (abs(eq2(x0,y0)) > tol):
        Dk = (eq1_x(x0,y0))*eq2_y(x0,y0) - (eq1_y(x0,y0))*eq2_x(x0,y0)
        dx = -((eq1(x0,y0)*eq2_y(x0,y0)) - (eq2(x0,y0)*eq1_y(x0,y0)))/Dk
        dy = -((eq1_x(x0,y0)*eq2(x0,y0)) - (eq2_x(x0,y0)*eq1(x0,y0)))/Dk
        x0,y0 = (x0+dx),(y0+dy)
    print(x0,y0)

while True:
    a = int(input("Enter an integer, 1.Bisection 2.NewtonRaphson 3.TwoVariables 4.Exit"))
    if a == 1:
        bisection()
    elif a == 2:
        NewtonRaphson()
    elif a == 3:
        TwoVariables()
    elif a == 4:
        break
    else:
        print("Enter Valid Number")