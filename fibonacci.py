x=input("What is the desired length of the Fibonacci sequence?")
if x==1:
    print "1"
elif x==2:
    print "1 1"
else:
    sequence = [1,1]
    a=2
    while a<=x-1:
        c=sequence[a-2]+sequence[a-1]
        sequence.append(c)
        a=a+1
    print sequence
    
