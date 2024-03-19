from Matrix import Matrix

# TODO You must be able to explain during evaluation what the rank represents.
"""rank nombre de vecteurs indépendants qu on peut sortir de la patrice
c'est sa "taille" en qq sorte
exemple 2: ligne 1 et 2 on un rapport claire entre elles donc on peut les isoler/les modifier par rapport a l autre
la 3eme n a rien a voir, donc 2 de rank (1 pour les 2 lignes liées, 1 pour la ligne indé) """

if __name__ == "__main__":
    u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print("expected: 3")
    print(u.rank())

    u = Matrix([[1, 2, 0, 0], [2, 4, 0, 0], [-1, 2, 1, 1]])
    print("expected: 2")
    print(u.rank())

    u = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1], [21, 18, 7]])
    print("expected: 3")
    print(u.rank())
