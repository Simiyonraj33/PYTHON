import math

# 1.Sqaure root
number=49
print("\n""Square root of",number,"is",math.sqrt(number),"\n")

# 2.Power
base=5
exponent=3
print(base,"raised to the power",exponent,"is",math.pow(base,exponent),"\n")

# 3.Trigonometric functions(angle in degrees)
angle_deg=30
angle_rad=math.radians(angle_deg)
print("Sin(",angle_deg,"):",math.sin(angle_rad))
print("Cos(",angle_deg,"):",math.cos(angle_rad))
print("Tan(",angle_deg,"):",math.tan(angle_rad),"\n")

# 4.Logarithmn of a number
print("Natural log of 10:",math.log(10))
print("Base 10 log of 1000:",math.log10(1000),"\n")

# 5.Rounding and floor ceil
num=3.765
print("Rounded:",round(num))
print("Floor:",math.floor(num))
print("Ceil:",math.ceil(num),"\n")

# =====Advanced math operations=====

# 6.Factorial of a number
print("\n---Advanced Math Operations---\n")
n=5
r=2
permutations=math.factorial(n)/math.factorial(n-r)
print("Permutations of",n,"itemstaken",r,"at a time:",int(permutations),"\n")

# 7.Compound Interest Calculation(real-time finance example)
p=10000
r=0.05
t=5
A=p*math.pow((1+r),t)
print("Compound amount after",t,"years at 5% interest:$",A)
