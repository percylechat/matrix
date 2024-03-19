from Vector import Vector


def linear_combination(vectors: list, scalars: list):
    for vector_ in vectors:
        if not isinstance(vector_, Vector):
            return None
    new = []
    # for each vector we multiply all elements by corresponding scalar
    for index in range(len(scalars)):
        new.append(vectors[index].scl(scalars[index]))
        vectors[index].printable()
    print(new)
    res = Vector(vectors[0].components)
    index = 1
    # we add all vectors one by one
    # first one already there so we use it and start index at one
    while index < len(new):
        vectors[index].printable()
        res.add(vectors[index])
        index += 1
    return res


# linear combination is elem1ofVec*elem1ofScl + elem2ofVec*elem2ofScl...
if __name__ == "__main__":
    e1 = Vector([1, 0, 0])
    e2 = Vector([0, 1, 0])
    e3 = Vector([0, 0, 1])

    v1 = Vector([1, 2, 3])
    v2 = Vector([0, 10, -100])

    print("expected: 10, -2 and 0.5")
    print(linear_combination([e1, e2, e3], [10, -2, 0.5]))

    print("expected: 10, 0 and 230")
    res = linear_combination([v1, v2], [10, -2])
    res.printable()
# // [10.]
# // [-2.]
# // [0.5]
# println!("{}", linear_combination<Vector<f32>, f32>([v1, v2], [10., -2.]));
# // [10.]
# // [0.]
# // [230.]
