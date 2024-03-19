from Vector import Vector


def angle_cos(obj1: Vector, obj2: Vector):
    if not obj1.comp_size(obj2):
        return None
    if obj1.norm() == 0 or obj2.norm() == 0:
        return None
    temp = obj1.dot(obj2)
    return temp / (obj1.norm() * obj2.norm())


if __name__ == "__main__":
    u = Vector([1, 0])
    v = Vector([1, 0])
    print("expected: 1")
    print(angle_cos(u, v))

    u = Vector([1, 0])
    v = Vector([0, 1])
    print("expected: 0")
    print(angle_cos(u, v))

    u = Vector([-1, 1])
    v = Vector([1, -1])
    print("expected: -1")
    print(angle_cos(u, v))

    u = Vector([2, 1])
    v = Vector([4, 2])
    print("expected: 1")
    print(angle_cos(u, v))

    u = Vector([1, 2, 3])
    v = Vector([4, 5, 6])
    print("expected: 0.974631846")
    print(angle_cos(u, v))
