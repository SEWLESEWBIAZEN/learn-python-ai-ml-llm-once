def fabonacci(max):
    a,b,counter=0,1,0
    while True:
        if(counter>max):
            return
        yield a
        a,b =b, a+b        
        counter+=1

f=fabonacci(10)
for x in f:
    print(x, " ", end="")