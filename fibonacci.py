#Fibonacci series
x=None
while x==None:
    try:
        x=int(raw_input("What is the desired length of the Fibonacci sequence?"))
        if x<1:
            print "Please enter a positive integer"
            x=None
        elif x>50:
            print "Small numbers please"
            x=None
    except ValueError:
        print "Please enter a valid number"
if x==1:
    print "1"
elif x==2:
    print "1",
    print "1",
else:
    a=1
    b=1
    print a,
    print b,
    for i in range(3,x+1,1):
        c=a+b
        print c,
        a=b
        b=c
        i=i+1

