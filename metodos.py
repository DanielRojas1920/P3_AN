from sympy import *

def metodo_trapecio(a,b,n,f):
    h = (b-a)/n  #altura
    values = [a+(i*h) for i in range(n+1)]
    f_values = [f.eval_function(value) for value in values]
    total_area = (f_values[0]+ f_values[-1] + 2*sum(f_values[1:-1]))*(h/2)

    print(f"El área total de la función {f} es: {total_area}")
    