def dot_product(vector1, vector2):
    dp = vector1.x * vector2.x + vector1.y * vector2.y
    return dp


def scalar_projection(p, a, b):
    #  p is moving point, a b are start and end of line
    ap = p - a
    ab = b - a
    ab.normalize()
    dp = float(ap.dot(ab))
    ab *= dp
    normal_point = a + ab
    return normal_point
