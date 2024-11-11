# Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

def area_of_triangle(base,height):
    return 0.5 * base * height

# print(area_of_triangle(1,2))

# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape

def area_base_on_shape(length,height,shap):
    if shap == "rect":
        return length * height
    else:
        return 0.5*length*height


print(area_base_on_shape(1,2,"rect"))