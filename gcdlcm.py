#GCD/LCM calculator
import sys
try:
    a=int(sys.argv[1])
    b=int(sys.argv[2])
except ValueError:
    print "Please enter valid positive integers"
else:
    if a<1 or b<1:
        print "Please enter valid positive integers"
    else:
        def gcd(x,y):
            if y==0: return x
            else: return gcd(y, x-y*int(x/y))
        def lcm(x,y):
            return (x*y)/gcd(x,y)
        print "GCD is " + str(gcd(a,b))
        print "LCM is " + str(lcm(a,b))
    
