from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ad = radians(ad)
ar = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar))) == ar 