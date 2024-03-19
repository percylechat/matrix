from Matrix import Matrix

if __name__ == "__main__":
    u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print("expected: 1, 0, 0 and 0, 1, 0 and 0, 0, 1")
    u.row_echelon().printable()

    u = Matrix([[1, 2], [3, 4]])
    print("expected: 1, 0 and 0, 1")
    u.row_echelon().printable()

    u = Matrix([[1, 2], [2, 4]])
    print("expected: 1, 2 and 0, 0")
    u.row_echelon().printable()

    u = Matrix([[8, 5, -2, 4, 28], [4, 2.5, 20, 4, -4], [8, 5, 1, 4, 17]])
    print(
        "expected: 1, 0.625, 0, 0 , -12.1666667 and 0, 0, 1, 0, -3.6666667 and 0, 0, 0, 1, 29.5"
    )
    u.row_echelon().printable()
