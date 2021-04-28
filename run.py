import matplotlib.pyplot as plt
import numpy as np
import sympy

c = 4
x = np.linspace(-2,2,20)
a = 2-x
b = 3+x

beta = np.arccos((np.square(a)+np.square(c)-np.square(b))/(2*a*c))
cx = 6-a*np.cos(beta)
cy = a*np.sin(beta)
R = np.sqrt(np.square(cx) + np.square(13-cy))
print(x)
print(R)
print(cx)
print(cy)
#plt.plot(x,R)
#plt.show()

x = -1.3
c = 4
a = 2-x
b = 3+x
beta = np.arccos((np.square(a)+np.square(c)-np.square(b))/(2*a*c))
cx = 6-a*np.cos(beta)
cy = a*np.sin(beta)

#plt.plot(np.array([6,cx,2]),np.array([0,cy,0]))
#plt.plot(np.array([cx,0]),np.array([cy,13]))
#plt.show()

A = sympy.Symbol('A')
B = sympy.Symbol('B')
l = sympy.Symbol('l')
x = sympy.Symbol('x')
h = sympy.Symbol('h')

beta = sympy.acos(((l-x)**2+(B-A)**2-x**2)/(2*(l-x)*(B-A)))
cx = B-(l-x)*sympy.cos(beta)
cy = (l-x)*sympy.sin(beta)
R = (cx**2 + (h-cy)**2)**0.5
print(sympy.simplify(R))
dRdx = sympy.diff(R,x)
print("dRdx = ")
print(dRdx)

x1 = 2;
x2 = 6;
A = 6;
B = 4;
C = 2;
H = 10;
l1 = 5;
l2 = 9

alpha = np.arccos((np.square((l1-x1))+np.square(A-B)-np.square(x1))/(2*(A-B)*(l1-x1)))
px = A-(l1-x1)*np.cos(alpha)
py = (l1-x1)*np.sin(alpha)

gamma = np.arctan(py/(px-C))

beta = np.arccos((np.square(l2-x2)+np.square((px-C)/np.cos(gamma))-np.square(x2))/(2*((px-C)/np.cos(gamma))*(l2-x2)))-gamma

qx = px - (l2-x2)*np.cos(beta)
qy = py + (l2-x2)*np.sin(beta)

plt.plot([A,px,B],[0,py,0])
plt.plot([px,qx,C],[py,qy,0])
plt.plot([qx,0],[qy,H])
plt.show()
