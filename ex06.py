from Vector import Vector


# a×b=(a2​b3​−a3​b2​,a3​b1​−a1​b3​,a1​b2​−a2​b1​)
def cross_product(obj1: Vector, obj2: Vector):
    if len(obj1.components) != 3 or len(obj2.components) != 3:
        return None
    return Vector(
        [
            (obj1.components[1] * obj2.components[2])
            - (obj1.components[2] * obj2.components[1]),
            (obj1.components[2] * obj2.components[0])
            - (obj1.components[0] * obj2.components[2]),
            (obj1.components[0] * obj2.components[1])
            - (obj1.components[1] * obj2.components[0]),
        ]
    )


if __name__ == "__main__":
    u = Vector([0, 0, 1])
    v = Vector([1, 0, 0])
    print("expected: 0, 1 and 0")
    cross_product(u, v).printable()

    u = Vector([1, 2, 3])
    v = Vector([4, 5, 6])
    print("expected: -3, 6 and -3")
    cross_product(u, v).printable()

    u = Vector([4, 2, -3])
    v = Vector([-2, -5, 16])
    print("expected: 17, -58 and -16")
    cross_product(u, v).printable()
