from Vector import Vector

# dot product if V1el1*V2el1 + V1el2*V2el2...
# it is interesting because numpy uses vectors
# and the dot function is here often so here i leanrned its use
if __name__ == "__main__":
    u = Vector([0, 0])
    v = Vector([1, 1])
    print("expected: 0")
    print(u.dot(v))

    u = Vector([1, 1])
    v = Vector([1, 1])
    print("expected: 2")
    print(u.dot(v))

    u = Vector([-1, 6])
    v = Vector([3, 2])
    print("expected: 9")
    print(u.dot(v))
