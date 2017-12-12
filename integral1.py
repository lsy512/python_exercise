import numpy as np

def integrate(f, a, b, N):
    x = np.linspace(a, b, N)
    fx = f(x)
    area = np.sum(fx)*(b-a)/N
    return area


def integrate1(f, a, b, N):
    x = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
    fx = f(x)
    area = np.sum(fx)*(b-a)/N
    return area


def jf(x1,y1,x2,y2,jg):
	k=(float)(y2-y1)/(x2-x1)
	print  k
	b=y1-k*x1
	print b
	pp=(x2-x1)/jg
	print pp
	sum2=0
	if x2<x1:
		jg=-jg
		pp=-pp
	print jg	
	for i in range(1,int(pp)):	
		temp= k*(x1+i*jg)+b
        	temp1=temp*jg
#		print temp1
        	sum2=sum2+temp1
	return sum2
 
#print jf(2,1,-1,0,0.0001)
print jf(0,0,1,1,0.0001)+jf(1,1,2,1,0.0001)+jf(2,1,3,0,0.0001)

print integrate(np.sin, 0, np.pi/2, 100)

print integrate1(np.sin, 0, np.pi/2, 100)



