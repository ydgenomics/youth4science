import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

cos_C = (a*a + b*b - c*c) / (2 * a * b)
cos_C = max(-1.0, min(1.0, cos_C))
rad = math.acos(cos_C)
de = math.degrees(rad)
print("Angle C in degrees:", de)