def is_valid_triangle(angle_a, angle_b, angle_c):

    if angle_a + angle_b + angle_c == 180 and angle_a and angle_b and angle_c > 0:
        return True
    else: 
        return False

def classify_by_angle(angle_a, angle_b, angle_c):
    if is_valid_triangle(angle_a, angle_b, angle_c):
        if angle_a == 90 or angle_b == 90 or angle_c == 90:
            return "right"
        elif angle_a < 90 and angle_b < 90 and angle_c < 90:
            return "acute"
        else:
            return "obtuse"
    else:
        return "INVALID"

def classify_by_side(angle_a, angle_b, angle_c):

    if is_valid_triangle(angle_a, angle_b, angle_c):
        if angle_a == 60 and angle_b == 60 and angle_c == 60:
            return "equilateral"
        elif angle_a == angle_b or angle_a == angle_c or angle_b == angle_c:
            return "isosceles"
        else:
            return "scalene"
    else:
        return "INVALID"

def classify_triangle(angle_a, angle_b, angle_c):

    if is_valid_triangle(angle_a, angle_b, angle_c):
        triangle_by_angle = classify_by_angle(angle_a, angle_b, angle_c)
        triangle_by_side = classify_by_side(angle_a, angle_b, angle_c)
        if triangle_by_angle == 'acute' and triangle_by_side == "equilateral":
            return "equilateral"
        else:
            return triangle_by_angle + " " + triangle_by_side
    else:
        return "INVALID"