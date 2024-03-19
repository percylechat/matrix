from Matrix import Matrix

if __name__ == "__main__":

    u = Matrix([[1, 0], [0, 1]])
    print("expected: 2")
    print(u.trace())

    u = Matrix([[2, -5, 0], [4, 3, 7], [-2, 3, 4]])
    print("expected: 9")
    print(u.trace())

    u = Matrix([[-2, -8, 4], [1, -23, 4], [0, 6, 4]])
    print("expected: -21")
    print(u.trace())
