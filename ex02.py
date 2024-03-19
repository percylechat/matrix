from Vector import Vector
from Matrix import Matrix

# https://fr.wikipedia.org/wiki/Interpolation_lin%C3%A9aire
# https://gamedev.stackexchange.com/questions/18615/how-do-i-linearly-interpolate-between-two-vectors


def lerp(obj1, obj2, scl):
    if scl > 1 or scl < 0:
        print("Wrong scalar value")
        return None
    if isinstance(obj1, Vector) & isinstance(obj2, Vector):
        if not obj1.comp_size(obj2):
            print("Wrong vector size")
            return None
        obj1.scl(1 - scl)
        obj2.scl(scl)
        obj1.add(obj2)
        return obj1
    elif isinstance(obj1, Matrix) & isinstance(obj2, Matrix):
        if not obj1.comp_size(obj2):
            print("Wrong matrix size")
            return None
        obj1.add(obj2)
        obj1.scl(scl)
        return obj1
    else:
        print("Wrong object types")
        return None


if __name__ == "__main__":
    print("expected: 0")
    res = lerp(Vector([0]), Vector([1]), 0)
    if res:
        res.printable()
    else:
        print(res)

    print("expected: 1")
    res = lerp(Vector([0]), Vector([1]), 1)
    if res:
        res.printable()
    else:
        print(res)

    print("expected: 0.5")
    res = lerp(Vector([0]), Vector([1]), 0.5)
    if res:
        res.printable()
    else:
        print(res)

    print("expected: 27.3")
    res = lerp(Vector([21]), Vector([42]), 0.3)
    if res:
        res.printable()
    else:
        print(res)

    print("expected: 2.6 and 1.3")
    res = lerp(Vector([2, 1]), Vector([4, 2]), 0.3)
    if res:
        res.printable()
    else:
        print(res)

    print("expected: 11 and 5.5, then 16.5 and 22")
    res = lerp(Matrix([[2, 1], [3, 4]]), Matrix([[20, 10], [30, 40]]), 0.5)
    if res:
        res.printable()
    else:
        print(res)

# println!("{}", lerp(Matrix::from([[2., 1.], [3., 4.]]), Matrix::from([[20.,
# 10.], [30., 40.]]), 0.5));
# // [[11., 5.5]
# // [16.5, 22.]]
