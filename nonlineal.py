import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# METODOS ABIERTOS
# Metodo de la biseccion

def f(x, pol):
    return eval(pol)

def graficar_funcion(pol, xr):
    x = np.linspace(-10, 10, 100)
    y = []
    for i in x:
        y.append(f(i, pol))
    
    plt.title("Función")
    plt.plot(x, y)
    plt.plot(xr, 0, marker='o', color='r')
    plt.show()
    
def biseccion(a, b, tol, pol):
    cota_inf = [a] # Lista para guardar la cota inferior
    cota_sup = [b] # Lista para guardar la cota superior
    x = [] # Lista para guardar los valores de x
    fx = [] # Lista para guardar los valores de f(x)
    err = [] # Lista para guardar los errores en %
    tol = int(tol)
    x.append(a)
    fx.append(round(f(a, pol), tol+1))

    e = 1
    err.append(round(e*100, 4))

    #if f(a, pol) * f(b, pol) > 0 and iter[0] == 1:
    #    print("No hay raiz en el intervalo")
    #    return iter, cota_inf, cota_sup, x, fx, err
    #else: 
    while e > 10**(-1*tol):
        c = (a + b) / 2
        e = abs((b - a) / 2)
        x.append(round(c, tol+1))
        fx.append(round(f(c, pol),tol+1))
        if f(a, pol) * f(c, pol) < 0:
            b = c
        else:
            a = c

        cota_sup.append(round(b, tol+1))
        cota_inf.append(round(a, tol+1))
        
        err.append(round(e*100, 4))
    return cota_inf, cota_sup, x, fx, err
#funcion = 'x**10 -1'
#bis = biseccion(0, 1.4, 3, funcion)

#print(bis[3][-1])
#graficar_funcion(funcion, bis[2][-1])
#for b in bis:
    print(b)
    print("\n")
def falsa_posicion(a, b, tol, pol):
    
    cota_inf = [a] # Lista para guardar la cota inferior
    cota_sup = [b] # Lista para guardar la cota superior
    x = [] # Lista para guardar los valores de x
    fx = [] # Lista para guardar los valores de f(x)
    err = [] # Lista para guardar los errores en %
    tol = int(tol)
    x.append(round(a, tol+1))
    fx.append(f(a, pol))

    e = abs((b - a) / b)
    err.append(round(e*100, 4))

    #if f(a, pol) * f(b, pol) > 0 and iter[0] == 1:
    #    print("No hay raiz en el intervalo")
    #    return iter, cota_inf, cota_sup, x, fx, err
    #else: 
    while e > 10**(-1*tol):
        c = b - (f(b, pol) * (b - a)) / (f(b, pol) - f(a, pol))

        x.append(round(c, tol+1))
        fx.append(f(c, pol))
        e = abs((c - a) / c)
        if f(a, pol) * f(c, pol) < 0:    
            b = c
        else:
            a = c

        
        cota_sup.append(round(b, tol+1))
        cota_inf.append(round(a, tol+1))
        
        err.append(round(e*100, 4))
        
    return cota_inf, cota_sup, x, fx, err

def falsa_posicion2(xl,xu,es,func):
    xr = xu
    xl = xl
    list_xr=[]
    list_xl=[]
    list_xr.append(xr)
    list_xl.append(xl)

    x = []
    fx = []
    err = []
    tol = int(es)
    x.append(xl)
    fx.append(round(f(xl, func), tol+1))
    x.append(xr)
    fx.append(round(f(xr, func), tol+1))
    e = 1
    err.append(round(e*100, 4))
    while e > 10**(-1*tol):
        xr = xu
        xu = xr - (f(xr, func) * (xl - xr)) / (f(xl, func) - f(xr, func))
        x.append(round(xu, tol+1))
        fx.append(round(f(xu, func), tol+1))
        e = abs((xu - xl) / xu)
        err.append(round(e*100, 4))
        if f(xl, func) * f(xu, func) < 0:
            xl = xu
        else:
            xu = xl
        list_xr.append(xr)
        list_xl.append(xl)
    return list_xl, list_xr, x, fx, err

def punto_fijo(x0, tol, pol):
    x = []
    fx = []
    err = []
    tol = int(tol)
    x.append(x0)
    fx.append(round(f(x0, pol), tol+1))
    e = 1
    err.append(round(e*100, 4))
    while e > 10**(-1*tol):
        x0 = f(x0, pol)
        x.append(round(x0, tol+1))
        fx.append(round(f(x0, pol), tol+1))
        e = abs((x0 - x[-2]) / x0)
        err.append(round(e*100, 4))
    return x, fx, err

# derivada
def d(n, pol):
    x = Symbol('x')
    f = lambda x: eval(pol)
    return derivative(f, n, 0.0001)
    

def newton_raphson(x0, tol, pol):
    
    x = [] # Lista para guardar los valores de x
    fx = [] # Lista para guardar los valores de f(x)
    dx = [] # Lista para guardar los valores de f'(x)
    err = [] # Lista para guardar los errores en %

    tol = int(tol)
    x.append(round(x0, tol+1))
    fx.append(round(f(x0, pol), tol+1))

    dx.append(round(d(x0, pol), tol+1))
    e = 100
    err.append(e)

    while e > 10**(-1*tol):
        x0 = x0 - (fx[-1] / dx[-1])
        e = abs((x0-x[-1])/x0)
        x.append(round(x0, tol+1))
        fx.append(round(f(x0, pol), tol+1))
        dx.append(round(d(x0, pol), tol+1))
        err.append(round(e, tol+1))
    

    return x, fx, dx, err




# Metodo de la secante
def secante(x0, x1, tol, pol):
    x = [] # Lista para guardar los valores de x
    fx = [] # Lista para guardar los valores de f(x)
    err = [] # Lista para guardar los errores en %

    tol = int(tol)
    x.append(round(x0, tol+1))
    fx.append(f(x0, pol))
    x.append(round(x1, tol+1))
    fx.append(round(f(x1, pol), tol+1))
    e = 1
    err.append(round(e*100, tol+1))

    while e > 10**(-1*tol):
        x0 = x0 - (f(x0, pol) * (x1 - x0)) / (f(x1, pol) - f(x0, pol))
        e = abs(x[-1] - x[-2])
        x.append(round(x0, tol+1))
        fx.append(round(f(x0, pol), tol+1))
        err.append(round(e*100, tol+1))
    return x, fx, err


#funcion = 'x**10-1'
#bis = biseccion(0, 1.4, 3.0, funcion)
#print(bis[2][-1])
#graficar_funcion(funcion, bis[2][-1])
#for b in bis:
#    print((b))
#    print("\n")

#fp = falsa_posicion(0, 2, 3, funcion)
#print(fp[2][-1])
#graficar_funcion(funcion, fp[2][-1])
#for f in fp:
    print(f)
    print("\n")

