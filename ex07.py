from Matrix import Matrix
from Vector import Vector

if __name__ == "__main__":
    u = Matrix([[1, 0], [0, 1]])
    v = Vector([4, 2])
    print("expected: 4, 2")
    u.mul_vec(v).printable()

    u = Matrix([[2, 0], [0, 2]])
    v = Vector([4, 2])
    print("expected: 8, 4")
    u.mul_vec(v).printable()

    u = Matrix([[2, -2], [-2, 2]])
    v = Vector([4, 2])
    print("expected: 4, -4")
    u.mul_vec(v).printable()

    u = Matrix([[1, 0], [0, 1]])
    v = Matrix([[1, 0], [0, 1]])
    print("expected: 1, 0 and 0, 1")
    u.mul_mat(v).printable()

    u = Matrix([[1, 0], [0, 1]])
    v = Matrix([[2, 1], [4, 2]])
    print("expected: 2, 1 and 4, 2")
    u.mul_mat(v).printable()

    u = Matrix([[3, -5], [6, 8]])
    v = Matrix([[2, 1], [4, 2]])
    print("expected: -14, -7 and 44, 22")
    u.mul_mat(v).printable()
