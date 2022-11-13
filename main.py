import math

print(
  "The General Form is: ax²+bx+c, where a, b, and c are real numbers with a != 0, make sure to put it in this form exactly"
)

a = int(input("Enter Value of a: "))
b = int(input("Enter Value of b: "))
c = int(input("Enter Value of c: "))

just = ((b**2) - (4 * a * c))

x = (-b + math.sqrt(just))
value_x = x / (2 * a)

xv2 = (-b - math.sqrt(just))
value_xv2 = xv2 / (2 * a)

if value_x == value_xv2:
  print(f'x = {value_x}')
elif value_x != value_xv2:
  print(f'x = {value_x} or {value_xv2}')
