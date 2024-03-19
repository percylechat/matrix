from Matrix import Matrix

# https://www.methodemaths.fr/determinant_matrice/
# cf developpement selon ligne ou colonne

# TODO
"""You must be able to explain during evaluation:
• What happens when det(A) = 0
• What the determinant represents geometrically in the vector
space after using the matrix for a linear transformation.
If you don’t know this, you should have watched 3blue1brown and
you didn’t, you bad student."""

"""quand detA = 0 pas dinverse de matrice et rang inferieur au nombre de lignes ou colonnes de la matrice
det represente mouvement dans espace ou transfo= par exemple 1 = souvent rotation ou augmentation par rapport a l espace
"""
"""NE PAS OUBLIER determinant est (valeur scalaire) donc multiplication !!! """

if __name__ == "__main__":
    u = Matrix([[1, -1], [-1, 1]])
    print("expected: 0")
    print(u.determinant())

    u = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
    print("expected: 8")
    print(u.determinant())

    u = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
    print("expected: -174")
    print(u.determinant())

    u = Matrix([[8, 5, -2, 4], [4, 2.5, 20, 4], [8, 5, 1, 4], [28, -4, 17, 1]])
    print("expected: 1032")
    print(u.determinant())
