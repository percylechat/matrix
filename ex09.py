from Matrix import Matrix

if __name__ == "__main__":
    u = Matrix([[1, 2, 3], [4, 5, 6]])
    print("expected: 1, 4 and 2, 5 and 3, 6")
    u.transpose().printable()
