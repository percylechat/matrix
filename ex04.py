from Vector import Vector

if __name__ == "__main__":
    u = Vector([0, 0, 0])
    print("expected 0, 0 and 0")
    print(u.norm1(), u.norm(), u.norm_inf())

    u = Vector([1, 2, 3])
    print("expected 6, 3.74165738 and 3")
    print(u.norm1(), u.norm(), u.norm_inf())

    u = Vector([-1, 2])
    print("expected 3, 2.236067977 and 3")
    print(u.norm1(), u.norm(), u.norm_inf())
