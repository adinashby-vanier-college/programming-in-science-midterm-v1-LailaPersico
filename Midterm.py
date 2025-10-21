import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    return 0.0
    result = 0
    result += round((math.pi) * (math.pow(r**2)), 2)
    return result
print(area_of_circle(5))
            

# Q2: Hollow Right Triangle
# *         
# **
# * *
# ****

def hollow_right_triangle(n):
    return ""
result = ""

for i in range(n):
    if i == 0:
            result += "*" + "\n"
    else:
            result += ("*" + (" " * (i-1))) + "\n"
    return result.rstrip()

print(hollow_right_triangle(4))



# Q3: Inverted Pyramid
def inverted_pyramid(n):
    return ""

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()