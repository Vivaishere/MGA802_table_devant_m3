def recursive(n):
    if n == 0 :
         factorielle = 1
    else :
        factorielle = n*recursive(n-1)
    return(factorielle)