import math

no=int(input("enter the number of inputs you want to give"))

z=[]

for s in range(no):

	z.append(int(input("enter your input")))

#ip=int(input("enter your input \n"))

#listip=list(ip)

N=len(z)



for k in range(N):

	temp=0

	

	for n in range(N):

		temp+=z[n]*math.e**(-1j*2*math.pi*n*k/N)

	print(temp)

	print(abs(temp))

	

	"""

student@ssl-1:~/Desktop$ python3 code.py

enter the number of inputs you want to give4

enter your input1

enter your input2

enter your input3

enter your input4

(10+0j)

10.0

(-2.0000000000000004+1.9999999999999996j)

2.8284271247461903

(-2-9.797174393178826e-16j)

2.0

(-1.9999999999999982-2.000000000000001j)

2.8284271247461894

"""	
