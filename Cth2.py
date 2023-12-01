from simpson import*

def f(x):
     return 5*x**2+10
    
a=float(input('batas bawah = '))
b=float(input('batas atas = '))
n=int(input('jumlah grid kelipatan 2 = '))

integral=simpson(f,a,n,b)

print('Integral = ',integral)
