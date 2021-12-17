def prime(x):
    i=2
    x=int(x)
    while i<=x:
        j=2
        k=0
        while j<i:
            if i%j==0:
                k=1
            j+=1
        if k==0:
            print i
        i+=1
