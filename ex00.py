from Vector import Vector
from Matrix import Matrix

if __name__ == "__main__":
    u = Vector([2, 3])
    print(u.add(5))
    v = Vector([2, 3, 7])
    print(u.add(v))
    u = Matrix([[1, 2], [3, 4]])
    print(u.add(v))

    u = Vector([2, 3])
    v = Vector([5, 7])
    u.add(v)
    print("expected values: 7 and 10")
    u.printable()

    u = Vector([2, 3])
    v = Vector([5, 7])
    u.sub(v)
    print("expected values: -3 and -4")
    u.printable()
    u = Matrix([[1, 2], [3, 4]])
    u = Vector([2, 3])
    v = 2
    u.scl(v)
    print("expected values: 4 and 6")
    u.printable()

    u = Matrix([[1, 2], [3, 4]])
    v = Matrix([[7, 4], [-2, 2]])
    u.add(v)
    print("expected values: 8 and 6, 1 and 6")
    u.printable()

    u = Matrix([[1, 2], [3, 4]])
    v = Matrix([[7, 4], [-2, 2]])
    u.sub(v)
    print("expected values: -6 and -2, 5 and 2")
    u.printable()

    u = Matrix([[1, 2], [3, 4]])
    v = 2
    u.scl(v)
    print("expected values: 2 and 4, 6 and 8")
    u.printable()
