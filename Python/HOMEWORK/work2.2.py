import math
p = math.pi
r=float(input('Enter radius: '))
h=float(input('Enter height: '))
c=2*p*r
s=p*r**2
S=2*s+c*h
BV=(4/3)*p*r**3
CV=s*h
print("Circle circumference: ", round(c,2))
print("Circle area: ", round(s,2))
print("Cylinder surface area: ", round(S,2))
print("Sphere volume: ", round(BV,2))
print("Cylinder volume: ", round(CV,2))