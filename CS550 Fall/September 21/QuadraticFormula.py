
import sys
import math

# Accept floats b and c as command-line arguments. Compute the
# the roots of the polynomial ax^2 + bx + c using the quadratic
# formula. Write the roots to standard output.

a = float (sys.argv[1])
b = float (sys.argv[2])
c = float (sys.argv[3])

discriminant = b*b - 4.0*a*c
d = math.sqrt(discriminant)

print((-b + d) / 2.0*a)
print((-b - d) / 2.0*a)