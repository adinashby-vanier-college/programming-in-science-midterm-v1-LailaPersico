import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    result = 0.0
    
    for i in range(radius):

        result += round((math.pi) * (math.pow(radius, 2)), 2)
    
        return result

print(area_of_circle(3))
            

# Q2: Hollow Right Triangle
# *
# **
# * *
# ****

def hollow_right_triangle(n): 
    result = ""

    for i in range(n):
        if n < 4:
            result += "The triangle height should be at least 4." + "\n"
        elif i == 0:
            result += "*" + "\n"
        elif i == n-1:
            result += ("*" * n) + "\n"
        else:
            result += ("*" + (" " * (i-1)) + "*") + "\n"
        

    return result.rstrip()

print(hollow_right_triangle(4))



# Q3: Inverted Pyramid
#*****
# ***
#  *
def inverted_pyramid(n): 

    result = ""

    for i in range(n):
        if n < 3:
            result += "The pyramid height should be at least 3." + "\n"
        elif i == n:
            result += "*"
        else:
            result += (" " * i)
            result += ("*" * (n-i)) 
            result += ("*" * (n- (i+1))) + "\n"

    return result.rstrip()

print(inverted_pyramid(3))

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