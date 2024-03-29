def simpson(f,a,n,b):
    h=(b-a)/n
    sum1=0.0
    sum2=0.0

    for i in range(1,n,2):
        x=a+i*h
        sum1=sum1+f(x)
    for i in range(2,n-1,2):
        x=a+i*h
        sum2=sum2+f(x)

    integral=(h/3)*(f(a)+4*sum1+2*sum2+f(b))

    return integral
