#modules for working with triangles


def is_valid_triangle(angle_a, angle_b, angle_c):
    if int(angle_a) + int(angle_b) + int(angle_c) == 180:
        return True
    else:
        return False

def classify_by_side(angle_a, angle_b, angle_c):
    if angle_a == angle_b == angle_c:
        return "equilateral"
    elif angle_a == angle_b or angle_b == angle_c or angle_a == angle_c:
        return "isosceles"
    else:
        return "scalene"

def classify_by_angle(angle_a, angle_b, angle_c):
    if angle_a > 90 or angle_b > 90 or angle_c > 90:
        return "obtuse"
    elif angle_a == 90 or angle_b == 90 or angle_c == 90:
        return "right"
    else: 
        return "acute"

def classify_triangle(angle_a,angle_b,angle_c):

    if is_valid_triangle(angle_a, angle_b, angle_c) == False:
        return "INVALID"

    side = classify_by_side(angle_a,angle_b,angle_c)
    angle = classify_by_angle(angle_a,angle_b,angle_c)

    if side == "equilateral":
        return "equilateral"
    else:
        return angle + " " + side
    