from Matrix import Matrix


if __name__ == "__main__":
    u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print("expected: 1, 0, 0 and 0, 1, 0 and 0, 0, 1")
    u.inverse().printable()

    u = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
    print("expected: 0.5, 0, 0 and 0, 0.5, 0 and 0, 0, 0.5")
    u.inverse().printable()

    u = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
    print(
        "expected: 0.649425287, 0.097701149, -0.655172414 and -0.781609195, -0.126436782, 0.965517241 and 0.143678161, 0.074712644, -0.206896552"
    )
    u.inverse().printable()
